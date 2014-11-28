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
        verbose_name_plural = "(05)船票数量查询日志"


class SystemLog(models.Model):
    '''
    系统日志
    '''
    logTime = models.DateTimeField(u"日志时间", default=datetime.now)
    logMsg = models.CharField(u'消息', max_length=500)

    class Meta:
        verbose_name = "系统日志"
        verbose_name_plural = "(04)系统日志"


class SystemConfig(models.Model):
    '''
    全局系统配置
    '''
    username = models.CharField(u'用户名', max_length=100)
    password = models.CharField(u'密码', max_length=100)
    preceding = models.IntegerField(u'预抢天数', default=0)
    working = models.BooleanField(u'启动', default=False)

    class Meta:
        verbose_name = "系统配置"
        verbose_name_plural = "(01)系统配置"


class FlightConfig(models.Model):
    '''
    航班配置
    '''
    flightCode = models.CharField(u'航班号', max_length=50)
    departure = models.CharField(u'出发码头', max_length=100)
    arrival = models.CharField(u'抵达码头', max_length=100)
    departureTime = models.CharField(u"开航时间", max_length=50)

    def __unicode__(self):
        return u'%s(%s-->%s:%s)' % (self.flightCode, self.departure, self.arrival, self.departureTime)


    class Meta:
        verbose_name = "航班配置"
        verbose_name_plural = "(05)航班配置"
        ordering = ['flightCode']


class PitchConfig(models.Model):
    '''
    抢票配置
    '''
    #flightCode = models.CharField(u'航班号', max_length=50)
    #departure = models.CharField(u'出发码头', max_length=100)
    #arrival = models.CharField(u'抵达码头', max_length=100)
    #departureTime = models.CharField(u"开航时间", max_length=50)
    flight = models.ForeignKey(FlightConfig, verbose_name=u'航班', null=True, blank=True, default=None)
    need = models.IntegerField(u'需票数', default=0)
    priority = models.IntegerField(u'优先级', default=0)

    class Meta:
        verbose_name = "抢票配置"
        verbose_name_plural = "(02)抢票配置"
        ordering = ['priority', '-need']


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
    need = models.IntegerField(u'需票数', default=0)
    pitchCount = models.IntegerField(u'抢到票数')
    ticketCount = models.IntegerField(u'余票')

    class Meta:
        verbose_name = "抢票记录"
        verbose_name_plural = "(03)抢票记录"

    def pitchMonth(self):
        return datetime.strftime(self.pitchTime, '%Y-%m')

    def pitchDay(self):
        return datetime.strftime(self.pitchTime, '%Y-%m-%d')


