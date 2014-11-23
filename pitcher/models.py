# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


class TicketCountLog(models.Model):
    '''
    船票数量日志
    用于分析抢票时机，主要是数据分析和测试使用，非系统正式表
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
    class Meta:
        verbose_name = "船票数量查询日志"
        verbose_name_plural = "船票数量查询日志"



class SystemLog(models.Model):
    '''
    系统日志
    '''
    logTime = models.DateTimeField(u"日志时间", default=datetime.now)
    logMsg = models.CharField(u'消息', max_length=500)
    class Meta:
        verbose_name = "系统日志"
        verbose_name_plural = "系统日志"

class SystemConfig(models.Model):
    '''
    全局系统配置
    '''
    username = models.CharField(u'用户名', max_length=100)
    password = models.CharField(u'密码', max_length=100)


class PitchConfig(models.Model):
    '''
    抢票配置表
    '''
    flightCode = models.CharField(u'航班号', max_length=50)
    departure = models.CharField(u'出发码头', max_length=100)
    arrival = models.CharField(u'抵达码头', max_length=100)
    departureTime = models.CharField(u"开航时间", max_length=50)
    need = models.IntegerField(u'需票数', default=0)


class PitchLog(models.Model):
    '''
    抢票记录
    '''
    pitchTime = models.DateTimeField(u"抢票时间", default=datetime.now)
    flightId = models.CharField(u'航班ID', max_length=50)
    flightCode = models.CharField(u'航班号', max_length=50)
    departure = models.CharField(u'出发码头', max_length=100)
    arrival = models.CharField(u'抵达码头', max_length=100)
    departureTime = models.CharField(u"开航时间", max_length=50)
    pitchCount = models.IntegerField(u'抢到票数')
    ticketCount = models.IntegerField(u'余票')


