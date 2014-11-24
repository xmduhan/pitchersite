# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 20:03:38 2014

@author: Administrator
"""

#%%
import time
from datetime import datetime,timedelta
from ticketpitcher import pitcher
from django_pandas.io import read_frame
from pitcher.models import TicketCountLog, SystemLog,SystemConfig


#%% 读取信息信息
#username = 'xmjf001'
#password = '123456'
#day = '2014-12-09'
systemConfig = SystemConfig.objects.all()[0]
username = systemConfig.username
password = systemConfig.password
date = datetime.now() + timedelta(systemConfig.preceding)
day = datetime.strftime(date,"%Y-%m-%d")


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

def getTicketInfo(day):
    '''
    按天获取船票的信息
    day 日期格式为'yyyy-mm-dd'
    '''
    df = read_frame(TicketCountLog.objects.all())
    df.columns = [field.verbose_name for field in TicketCountLog._meta.fields]
    return df.ix[:, 2:]

def orderTicket(dailyFlightId,n):
    '''
    测试
    '''
    return True

#------------------------------------------------------------------------------

#%% 实际使用方法调用

def isLogin():
    '''
    检查当前是否已经登录
    '''       
    return pitcher.isLogin()


def getTicketInfo(day):
    '''
    按天获取船票的信息
    day 日期格式为'yyyy-mm-dd'
    '''
    # 实际脚本
    return pitcher.getTicketInfo(day)


def orderTicket(dailyFlightId,n):
    '''
    测试
    '''
    return pitcher.orderTicket(dailyFlightId,n)

#------------------------------------------------------------------------------



#------------------------------------------------------------------------------
#%%
#def loopPitcher():
#    while pitcher.isLogin():
#        ticketInfo = pitcher.getTicketInfo(day)
#        for i in range(len(ticketInfo.index)):
#            row = ticketInfo.irow(i)
#            log = TicketCountLog()
#            log.seq = row[u'序号']
#            log.departure = row[u'出发码头']
#            log.arrival = row[u'抵达码头']
#            log.flightCode = row[u'航班号']
#            log.departureTime = row[u'开航时间']
#            log.price = row[u'票价']
#            log.ticketCount = row[u'余票']
#            log.flightId = row[u'航班ID']
#            log.save()
        #print u'成功读取数据,等待5秒……'
        #writeSystemLog(u'Read data successfully,waiting 5 seconds ... ...')
#        writeSystemLog(u'成功读取数据,等待3秒……')
#        time.sleep(3)
#    else:
#        raise Exception(u'登录信息丢失,将重新登录')


#%%
#while True:
#    try:
#        pitcher.login(username, password)
#        loopPitcher()
#    except Exception as e:
#        writeSystemLog(u'出现异常:' + unicode(e))
    #print u'Waiting 10 seconds ... ...'
#    writeSystemLog(u'等待10秒... ...')
#    time.sleep(10)

#%%
#select * from pitcher_ticketcountlog
#where "departureTime" = '09:30'
#  and "departure" = '邮轮中心厦鼓码头'
#  and "arrival" = '三丘田码头'
#  order by "logTime";


#select  "departureTime",count(*)*3 "机会时间(秒)"
#from pitcher_ticketcountlog
#where 1 = 1
#  and "departureTime" >= '08:10' and "departureTime" <= '10:30'
#  and "departure" = '邮轮中心厦鼓码头'
#  and "arrival" = '三丘田码头'
#  and "ticketCount" > 0
#  group by "departureTime"
#  order by "departureTime";
