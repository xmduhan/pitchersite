# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 20:03:38 2014

@author: Administrator
"""

#%%
import os
import sys
import time
#path = r'E:\pydev\pitchersite' # 项目位置
path = r'/home/wx/pydev/pitchersite' # 项目位置
settings = "pitchersite.settings"
sys.path.append(path)   
os.chdir(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE",settings)
from pitcher.models import TicketCountLog
from ticketpitcher import pitcher


#%% 不停的刷新票的数量信息
username = 'xmjf001'
password = '123456'
day = '2014-12-09'

#%%
def loopPitcher():
    while pitcher.isLogin():
        ticketInfo = pitcher.getTicketInfo(day)
        for i in range(len(ticketInfo.index)):
            row = ticketInfo.irow(i)
            log = TicketCountLog()
            log.seq = row[u'序号']
            log.departure = row[u'出发码头']
            log.arrival = row[u'抵达码头']
            log.flightCode = row[u'航班号']
            log.departureTime = row[u'开航时间']
            log.price = row[u'票价']
            log.ticketCount = row[u'余票']
            log.flightId = row[u'航班ID']
            log.save()
        #print u'成功读取数据,等待5秒……'
        print u'Read data successfully,waiting 5 seconds ... ...'
        time.sleep(5)
    else:
        raise Exception(u'Login losted!Will relogin.')

#%%
while True:
    try:
        pitcher.login(username,password)
        loopPitcher()
    except Exception as e :
        print e
    print u'Waiting 10 seconds ... ...'
    time.sleep(10)

#%%
#select * from pitcher_ticketcountlog
#where "departureTime" = '09:30'
#  and "departure" = '邮轮中心厦鼓码头'
#  and "arrival" = '三丘田码头'
#  order by "logTime";
