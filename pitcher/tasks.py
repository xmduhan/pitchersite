# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 20:03:38 2014

@author: Administrator
"""

#%%
import time
from datetime import datetime, timedelta
from ticketpitcher import pitcher
from django_pandas.io import read_frame
from pitcher.models import *





#%% 日志
def writeSystemLog(msg):
    '''
    写入系统日志
    '''
    log = SystemLog()
    log.logMsg = msg
    log.save()


#------------------------------------------------------------------------------
#%% 测试使用方法调用
#
# def isLogin():
#     '''
#     检查当前是否已经登录
#     '''
#     time.sleep(1)
#     return True
#
#
# def login(username, password):
#     '''
#     登录
#     '''
#     time.sleep(1)
#     return True
#
#
# def getTicketInfo(day):
#     '''
#     按天获取船票的信息
#     day 日期格式为'yyyy-mm-dd'
#     '''
#     time.sleep(1)
#     df = read_frame(TicketCountLog.objects.all())
#     df.columns = [field.verbose_name for field in TicketCountLog._meta.fields]
#     return df.ix[:, 2:]
#
#
# def orderTicket(dailyFlightId, n):
#     '''
#     测试
#     '''
#     time.sleep(1)
#     return True
#------------------------------------------------------------------------------

#%% 实际使用方法调用

def isLogin():
    '''
    检查当前是否已经登录
    '''
    return pitcher.isLogin()


def login(username, password):
    '''
    登录
    '''
    return pitcher.login(username, password)


def getTicketInfo(day):
    '''
    按天获取船票的信息
    day 日期格式为'yyyy-mm-dd'
    '''
    return pitcher.getTicketInfo(day)


def orderTicket(dailyFlightId, n):
    '''
    订票
    '''
    return pitcher.orderTicket(dailyFlightId, n)


#------------------------------------------------------------------------------

#%%

def getPitchConfig():
    '''
    获取要抢票的配置
    返回DataFrame数据集,注意数据已按优先级排好顺序
    '''
    return read_frame(PitchConfig.objects.filter(need__gt=0))[['flightCode', 'need']]


#%%
def getTicketRemain(ticketInfo, flightCode):
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


def getDailyFlightId(ticketInfo, flightCode):
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


#%% 设置全局变量
normalWaitingSecond = 2
errorWaitingSecond = 5
maxLoginError = 5
maxException = 30
timeToStop = '12:00'
# 读取信息信息
systemConfig = SystemConfig.objects.all()[0]
username = systemConfig.username
password = systemConfig.password
working = systemConfig.working
date = datetime.now() + timedelta(systemConfig.preceding)
day = datetime.strftime(date, "%Y-%m-%d")
pitchConfig = getPitchConfig()



#%%
def pitchItem(ticketInfo, flightCode, need):
    '''
    进行一次抢票动作
    ticketInfo  最近读取的船票信息
    flightCode  航班代码
    n           需要票的数量
    成功返回实际抢票数量，失败返回0
    '''
    ItemMessage = u'尝试抢票(航班号:%s,需票数:%d):' % (flightCode, need)
    writeSystemLog(ItemMessage + u'开始!')
    # 读取票数剩余
    remain = getTicketRemain(ticketInfo, flightCode)
    # 如果该航班没有票跳过
    if remain == 0:
        writeSystemLog(ItemMessage + u'已无余票!')
        return 0
    # 获取dailyFlightId
    dailyFlightId = getDailyFlightId(ticketInfo, flightCode)
    if dailyFlightId == None:
        writeSystemLog(ItemMessage + u'无法获取航班Id!')
        return 0
    # 如果需票数小于实际剩余按实际票数抢
    if need > remain:
        writeSystemLog(ItemMessage + u'余票不足，按实际票数抢!')
        n = remain
    else:
        n = need
    #writeSystemLog(ItemMessage + u'dailyFlightId:%s' % dailyFlightId)
    orderResult = orderTicket(dailyFlightId, n)
    if orderResult:
        return n
    else:
        return 0


def pitchLoop():
    '''
    刷票主循环过程
    返回True表示抢票动作没有执行，但是登录信息丢失，需要登录后继续调用该过程
    返回False表示抢票动作已执行，或者已经超过限定的抢票时间，程序应该终止
    '''
    while isLogin():
        ticketInfo = getTicketInfo(day)
        if len(ticketInfo.index):
            # 已经放票了,根据配置数据开始顺序进行抢票
            writeSystemLog(u'系统已经放票，准备开始抢票...')
            for i in range(len(pitchConfig.index)):
                config = pitchConfig.irow(i)
                # 读取当前记录要抢的航班号和需票信息
                flightCode = config['flightCode']
                need = config['need']
                ItemMessage = u'尝试抢票(航班号:%s,需票数:%d):' % (flightCode, need)
                # 调用抢票接口
                pitchResult = pitchItem(ticketInfo, flightCode, need)
                # 记录本次抢票结果
                pitchLog = PitchLog()
                pitchLog.flightCode = flightCode
                pitchLog.need = need
                pitchLog.pitchCount = pitchResult
                # 将票结果记录日志
                if pitchResult > 0:
                    # 抢票成功
                    writeSystemLog(ItemMessage + u'抢票成功!!!')
                else:
                    # 抢票失败
                    writeSystemLog(ItemMessage + u'抢票执行失败，将跳过此项!')
                # 刷新余票信息(顺带获取航班的一些基本信息，本来应该在前面取的，但是合并在这里比较方便，且无伤大雅)
                ticketInfo = getTicketInfo(day)
                df = ticketInfo[ticketInfo[u'航班号'] == flightCode]
                if len(df.index) > 0:
                    row = df.irow(0)
                    pitchLog.flightId = row[u'航班ID']
                    pitchLog.departure = row[u'出发码头']
                    pitchLog.arrival = row[u'抵达码头']
                    pitchLog.departureTime = row[u'开航时间']
                    pitchLog.ticketCount = row[u'余票']
                else:
                    writeSystemLog(ItemMessage + u'无法获取余票及航班相关信息!')
                # 保存抢票日志
                pitchLog.save()
            # 执行过抢票程序任务完成
            writeSystemLog(u'已完成刷票动作，将停止执行!')
            return False  #返回False表示程序应该终止
        # 刷新完毕等待一段时间
        writeSystemLog(u'完成一次刷新，将等待%d秒...' % normalWaitingSecond)
        time.sleep(normalWaitingSecond)
        # 检查当前时间是否超过中午12点，如果超过停止刷票
        if datetime.strftime(datetime.now(), "%H:%M") >= timeToStop:
            writeSystemLog(u'程序已执行到执行时间(%s),将停止执行!' % timeToStop)
            return False  #返回False表示程序应该终止
    # 程序到这里表示登录信息已经丢失
    writeSystemLog(u'登录信息丢失将尝试重新登录!')
    return True


#%%
def pitcherTask():
    '''
    抢票程序主过程
    '''
    writeSystemLog(u'程序开始执行!')
    # 判断刷票开关是否开启，如果没有开启则退出
    if not working:
        writeSystemLog(u'刷票配置未启动，程序将退出!')
        writeSystemLog(u'程序执行结束!')
        return

    # 开始刷票
    loginErrorCount = 0
    ExceptionCount = 0
    pitchLoopResult = True
    while pitchLoopResult:
        try:
            loginResult = login(username, password)
            if loginResult:
                # 如果登录成功清空原来登录失败的记录
                loginErrorCount = 0
                writeSystemLog(u'登录成功!')
                pitchLoopResult = pitchLoop()
            else:
                loginErrorCount += 1
                if loginErrorCount > maxLoginError:
                    writeSystemLog(u'登录失败超过%d次，程序退出!' % maxLoginError)
                    return
                else:
                    writeSystemLog(u'登录失败!')
                    writeSystemLog(u'等待%s秒... ...' % errorWaitingSecond)
                    time.sleep(errorWaitingSecond)
        except Exception as e:
            writeSystemLog(u'出现异常:' + unicode(e))
            ExceptionCount += 1
            if ExceptionCount > maxException:
                writeSystemLog(u'抛出异常超过%d次，程序将退出!' % maxException)
                break
            writeSystemLog(u'等待%s秒... ...' % errorWaitingSecond)
            time.sleep(errorWaitingSecond)

    writeSystemLog(u'程序执行结束!')






