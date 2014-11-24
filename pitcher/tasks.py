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

def isLogin():
    '''
    检查当前是否已经登录
    '''
    return True


def login(username, password):
    '''
    登录
    '''
    return True


def getTicketInfo(day):
    '''
    按天获取船票的信息
    day 日期格式为'yyyy-mm-dd'
    '''
    df = read_frame(TicketCountLog.objects.all())
    df.columns = [field.verbose_name for field in TicketCountLog._meta.fields]
    return df.ix[:, 2:]


def orderTicket(dailyFlightId, n):
    '''
    测试
    '''
    return True


#------------------------------------------------------------------------------

#%% 实际使用方法调用
#
#def isLogin():
#    '''
#    检查当前是否已经登录
#    '''       
#    return pitcher.isLogin()
#
#
#def login(username,password):
#    '''
#    登录
#    '''
#    return pitcher.login(username, password)
#def getTicketInfo(day):
#    '''
#    按天获取船票的信息
#    day 日期格式为'yyyy-mm-dd'
#    '''
#    # 实际脚本
#    return pitcher.getTicketInfo(day)
#
#
#def orderTicket(dailyFlightId,n):
#    '''
#    订票
#    '''
#    return pitcher.orderTicket(dailyFlightId,n)

#------------------------------------------------------------------------------

#%% 设置全局变量
normalWaitingSecond = 1
errorWaitingSecond = 3
# 读取信息信息
systemConfig = SystemConfig.objects.all()[0]
username = systemConfig.username
password = systemConfig.password
date = datetime.now() + timedelta(systemConfig.preceding)
day = datetime.strftime(date, "%Y-%m-%d")


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
        return df.irow(0)[u'余票']
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
        return df.irow(0)[u'航班ID']
    else:
        return None

#%%
ticketInfo = getTicketInfo('')
#%%
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
            pitchConfig = getPitchConfig()
            for i in range(len(pitchConfig.index)):
                # 读取当前记录要抢的航班号和需票信息
                flightCode = pitchConfig['flightCode']
                need = pitchConfig['need']
                # 读取票数剩余
                remain = getTicketRemain(ticketInfo, flightCode)
                # 如果该航班没有票跳过
                if remain == 0:
                    continue
                # 获取dailyFlightId
                dailyFlightId = getDailyFlightId(ticketInfo, flightCode)
                if dailyFlightId == None:
                    continue
                # 如果需票数小于实际剩余按实际票数抢
                if need > remain:
                    n = remain
                else:
                    n = need
                pitchResult = orderTicket(dailyFlightId, n)
                if pitchResult:
                    # 抢票成功
                    pass
                else:
                    # 抢票失败
                    pass
            # 执行过抢票程序任务完成
            return False #返回False表示程序应该终止
        # 刷新完毕等待一段时间
        time.sleep(normalWaitingSecond)
        # 检查当前时间是否超过中午12点，如果超过停止刷票
        if datetime.strftime(datetime.now(),"%H:%M") >= '12:00':
            return False #返回False表示程序应该终止
    # 程序到这里表示登录信息已经丢失
    return True


#%%

def pitcherTask():
    '''
    抢票程序主过程
    '''
    while True:
        try:
            login(username, password)
            pitchLoop()
        except Exception as e:
            writeSystemLog(u'出现异常:' + unicode(e))
        writeSystemLog(u'等待3秒... ...')
        time.sleep(3)






