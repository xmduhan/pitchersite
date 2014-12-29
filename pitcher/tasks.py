# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 20:03:38 2014

@author: Administrator
"""

#%%
import time
from datetime import datetime, timedelta
from ticketpitcher import pitcher
from pitcher.models import *
from pandas import DataFrame


class PitchTask():
    '''
    抢票任务
    '''

    def __init__(self, taskName):
        #%% 设置全局变量
        systemConfig = SystemConfig.objects.all()[0]
        self.normalWaitingSecond = systemConfig.normalWaitingSecond
        self.errorWaitingSecond = systemConfig.errorWaitingSecond
        self.maxLoginError = systemConfig.maxLoginError
        self.maxException = systemConfig.maxException
        self.timeToStop = systemConfig.timeToStop
        # 读取信息信息
        task = Task.objects.get(taskName=taskName)
        self.task = task
        self.username = task.username
        self.password = task.password
        self.working = task.working
        date = datetime.now() + timedelta(systemConfig.preceding)
        self.day = datetime.strftime(date, "%Y-%m-%d")
        self.pitchConfig = self.getPitchConfig()


    def getPitchConfig(self):
        '''
        获取要抢票的配置
        返回DataFrame数据集,数据已按优先级排好顺序
        注意：排序规则在数据模型PitchConfig中的ordering定义的
        '''
        data = []
        for pitchConfig in PitchConfig.objects.filter(need__gt=0, task=self.task):
            flight = pitchConfig.flight
            data.append([flight.flightCode, pitchConfig.need])
        return DataFrame(data, columns=['flightCode', 'need'])

    def writeSystemLog(self, msg):
        '''
        写入系统日志
        '''
        # 将信息写到数据库日志中
        log = SystemLog()
        log.logMsg = msg
        log.task = self.task
        log.save()


    def isLogin(self):
        '''
        检查当前是否已经登录
        '''
        return pitcher.isLogin()


    def login(self, username, password):
        '''
        登录
        '''
        return pitcher.login(username, password)


    def getTicketInfo(self, day):
        '''
        按天获取船票的信息
        day 日期格式为'yyyy-mm-dd'
        '''
        return pitcher.getTicketInfo(day)


    def orderTicket(self, dailyFlightId, n):
        '''
        订票
        '''
        return pitcher.orderTicket(dailyFlightId, n)


    def getTicketRemain(self, ticketInfo, flightCode):
        '''
        根据提供的船票信息数据集及航班的编码获得余票数
        ticketInfo 船票信息
        flightCode 航班的编码
        '''
        df = ticketInfo[ticketInfo[u'航班号'] == flightCode]
        if len(df.index) > 0:
            return int(df.irow(0)[u'余票'])
        else:
            return 0


    def getDailyFlightId(self, ticketInfo, flightCode):
        '''
        根据提供的船票信息数据集及航班的编码获得dailyFlightId
        ticketInfo 船票信息
        flightCode 航班的编码
        '''
        df = ticketInfo[ticketInfo[u'航班号'] == flightCode]
        if len(df.index) > 0:
            return int(df.irow(0)[u'航班ID'])
        else:
            return None


    def pitchItem(self, ticketInfo, flightCode, need):
        '''
        进行一次抢票动作
        ticketInfo  最近读取的船票信息
        flightCode  航班代码
        n           需要票的数量
        成功返回实际抢票数量，失败返回0
        '''
        ItemMessage = u'尝试抢票(航班号:%s,需票数:%d):' % (flightCode, need)
        self.writeSystemLog(ItemMessage + u'开始...')
        # 读取票数剩余
        remain = self.getTicketRemain(ticketInfo, flightCode)
        # 如果该航班没有票跳过
        if remain == 0:
            self.writeSystemLog(ItemMessage + u'已无余票.')
            return 0
        # 获取dailyFlightId
        dailyFlightId = self.getDailyFlightId(ticketInfo, flightCode)
        if dailyFlightId == None:
            self.writeSystemLog(ItemMessage + u'无法获取航班Id.')
            return 0
        # 如果需票数小于实际剩余按实际票数抢
        if need > remain:
            self.writeSystemLog(ItemMessage + u'余票不足，按实际票数抢.')
            n = remain
        else:
            n = need
        #writeSystemLog(ItemMessage + u'dailyFlightId:%s' % dailyFlightId)
        orderResult = self.orderTicket(dailyFlightId, n)
        if orderResult:
            return n
        else:
            return 0


    def savePitchLog(self, ticketInfo, flightCode, need, pitchResult):
        '''
        保存抢票记录信息
        ticketInfo   最新的船票信息数据集
        flightCode   航班号
        need         需票数
        pitchResult  实际抢票数量
        '''
        # 记录本次抢票结果
        pitchLog = PitchLog()
        pitchLog.task = self.task
        pitchLog.flightCode = flightCode
        pitchLog.need = need
        pitchLog.pitchCount = pitchResult
        df = ticketInfo[ticketInfo[u'航班号'] == flightCode]
        if len(df.index) > 0:
            row = df.irow(0)
            pitchLog.flightId = row[u'航班ID']
            pitchLog.departure = row[u'出发码头']
            pitchLog.arrival = row[u'抵达码头']
            pitchLog.departureTime = row[u'开航时间']
            pitchLog.ticketCount = row[u'余票']
        else:
            ItemMessage = u'尝试抢票(航班号:%s,需票数:%d):' % (flightCode, need)
            self.writeSystemLog(ItemMessage + u'无法获取余票及航班相关信息.')
        # 保存抢票日志
        pitchLog.save()


    def pitchLoop(self):
        '''
        刷票主循环过程
        返回True表示抢票动作没有执行，但是登录信息丢失，需要登录后继续调用该过程
        返回False表示抢票动作已执行，或者已经超过限定的抢票时间，程序应该终止
        '''
        while self.isLogin():
            ticketInfo = self.getTicketInfo(self.day)
            if len(ticketInfo.index):
                ### 已经放票了,根据配置数据开始顺序进行抢票 ###
                self.writeSystemLog(u'系统已经放票，准备开始抢票...')
                resultList = []
                for i in range(len(self.pitchConfig.index)):
                    config = self.pitchConfig.irow(i)
                    # 读取当前记录要抢的航班号和需票信息
                    flightCode = config['flightCode']
                    need = config['need']
                    ItemMessage = u'尝试抢票(航班号:%s,需票数:%d):' % (flightCode, need)
                    # 调用抢票接口
                    pitchResult = self.pitchItem(ticketInfo, flightCode, need)
                    # 将抢票结果反映在系统日志中
                    if pitchResult > 0:
                        # 抢票成功
                        self.writeSystemLog(ItemMessage + u'抢票成功!')
                    else:
                        # 抢票失败
                        self.writeSystemLog(ItemMessage + u'抢票执行失败，将跳过此项.')
                    # 将结果记录列表抢票结束后统一保存（加快速度）
                    resultList.append({'flightCode': flightCode, 'need': need, 'pitchResult': pitchResult})

                ### 保存抢票结果信息 ###
                # 重新读取余票信息
                ticketInfo = self.getTicketInfo(self.day)
                # 保存抢票结果记录信息
                for result in resultList:
                    self.savePitchLog(ticketInfo, result['flightCode'], result['need'], result['pitchResult'])

                ### 执行过抢票程序任务完成 ###
                self.writeSystemLog(u'已完成刷票动作，将停止执行.')
                return False  #返回False表示程序应该终止

            # 刷新完毕等待一段时间
            self.writeSystemLog(u'完成一次刷新，将等待%d秒...' % self.normalWaitingSecond)
            time.sleep(self.normalWaitingSecond)
            # 检查当前时间是否超过中午12点，如果超过停止刷票
            if datetime.strftime(datetime.now(), "%H:%M") >= self.timeToStop:
                self.writeSystemLog(u'程序已执行到执行时间(%s),将停止执行.' % self.timeToStop)
                return False  #返回False表示程序应该终止
        # 程序到这里表示登录信息已经丢失
        self.writeSystemLog(u'登录信息丢失将尝试重新登录.')
        return True

    def run(self):
        '''
        抢票程序主过程
        '''
        self.writeSystemLog(u'程序开始执行...')
        # 判断刷票开关是否开启，如果没有开启则退出
        if not self.working:
            self.writeSystemLog(u'刷票配置未启动，程序将退出.')
            self.writeSystemLog(u'程序执行结束.')
            return

        # 开始刷票
        loginErrorCount = 0
        ExceptionCount = 0
        pitchLoopResult = True
        while pitchLoopResult:
            try:
                loginResult = self.login(self.username, self.password)
                if loginResult:
                    # 如果登录成功清空原来登录失败的记录
                    loginErrorCount = 0
                    self.writeSystemLog(u'登录成功!')
                    pitchLoopResult = self.pitchLoop()
                else:
                    loginErrorCount += 1
                    if loginErrorCount > self.maxLoginError:
                        self.writeSystemLog(u'登录失败超过%d次，程序退出!' % self.maxLoginError)
                        return
                    else:
                        self.writeSystemLog(u'登录失败!')
                        self.writeSystemLog(u'等待%s秒... ...' % self.errorWaitingSecond)
                        time.sleep(self.errorWaitingSecond)
            except Exception as e:
                self.writeSystemLog(u'出现异常:' + unicode(e))
                ExceptionCount += 1
                if ExceptionCount > self.maxException:
                    self.writeSystemLog(u'抛出异常超过%d次，程序将退出!' % self.maxException)
                    break
                self.writeSystemLog(u'等待%s秒... ...' % self.errorWaitingSecond)
                time.sleep(self.errorWaitingSecond)

        self.writeSystemLog(u'程序执行结束!')






