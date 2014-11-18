# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


class TicketCountLog(models.Model):
    '''
    船票数量日志
    用于分析抢票时机
    '''
    logTime = models.DateTimeField(u"日志时间", default=datetime.now)
    seq = models.IntegerField(u'序号')
    departure = models.CharField(u'出发码头', max_length=100)
    arrival = models.CharField(u'抵达码头', max_length=100)
    flightCode = models.CharField(u'航班号', max_length=50)
    departureTime = models.CharField(u"开航时间", max_length=50)
    price = models.FloatField(u'票价')
    ticketCount = models.IntegerField(u'余票')
    flightId = models.CharField(u'航班ID', max_length=50)


class SystemLog(models.Model):
    '''
    系统日志
    '''
    logTime = models.DateTimeField(u"日志时间", default=datetime.now)
    logMsg = models.CharField(u'消息', max_length=500)