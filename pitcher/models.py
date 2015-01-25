# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


class Task(models.Model):
    '''
    任务
    '''
    TASK_TYPE = ( ('pitch', u'抢票'), ('refresh', u'刷新'))
    taskName = models.CharField(u'任务名', max_length=100)
    username = models.CharField(u'用户名', max_length=100)
    password = models.CharField(u'密码', max_length=100)
    type = models.CharField(u'任务类型', choices=TASK_TYPE, max_length=10, default='pitch')
    working = models.BooleanField(u'启动', default=False)

    class Meta:
        verbose_name = u'任务'
        verbose_name_plural = u'(02)任务配置'
        ordering = ['taskName']

    def __unicode__(self):
        typeName = dict(Task._meta.get_field_by_name('type')[0].choices)[self.type]
        return u'%s(%s,%s)' % (self.taskName, typeName, self.username)


class SystemLog(models.Model):
    '''
    系统日志
    '''
    task = models.ForeignKey(Task, verbose_name=u'任务', null=True, blank=True, default=None)
    logTime = models.DateTimeField(u"日志时间", default=datetime.now)
    logMsg = models.CharField(u'消息', max_length=500)

    class Meta:
        verbose_name = u'系统日志'
        verbose_name_plural = u'(05)系统日志'


class SystemConfig(models.Model):
    '''
    全局系统配置
    '''
    normalWaitingSecond = models.IntegerField(u'刷新周期(秒)', default=2)
    errorWaitingSecond = models.IntegerField(u'出错等待时间(秒)', default=5)
    maxLoginError = models.IntegerField(u'最大登录出错次数', default=5)
    maxException = models.IntegerField(u'最大异常次数', default=5)
    timeToStop = models.CharField(u'程序终止时间(HH:MM)', max_length=100)
    preceding = models.IntegerField(u'预抢天数(天)', default=0)

    class Meta:
        verbose_name = u'系统配置'
        verbose_name_plural = u'(01)系统配置'


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
        verbose_name = u'航班配置'
        verbose_name_plural = u'(06)航班配置'
        ordering = ['flightCode']


class PitchConfig(models.Model):
    '''
    抢票配置
    '''
    #flightCode = models.CharField(u'航班号', max_length=50)
    #departure = models.CharField(u'出发码头', max_length=100)
    #arrival = models.CharField(u'抵达码头', max_length=100)
    #departureTime = models.CharField(u"开航时间", max_length=50)
    task = models.ForeignKey(Task, verbose_name=u'任务', null=True, blank=True, default=None)
    flight = models.ForeignKey(FlightConfig, verbose_name=u'航班', null=True, blank=True, default=None)
    need = models.IntegerField(u'需票数', default=0)
    priority = models.IntegerField(u'优先级', default=0)

    class Meta:
        verbose_name = u'抢票配置'
        verbose_name_plural = u'(03)抢票配置'
        ordering = ['task', 'priority', '-need']


class PitchLog(models.Model):
    '''
    抢票记录
    '''
    task = models.ForeignKey(Task, verbose_name=u'任务', null=True, blank=True, default=None)
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
        verbose_name = u'抢票记录'
        verbose_name_plural = u'(04)抢票记录'

    def pitchMonth(self):
        return datetime.strftime(self.pitchTime, '%Y-%m')

    def pitchDay(self):
        return datetime.strftime(self.pitchTime, '%Y-%m-%d')


class RefreshRedo(models.Model):
    '''
    票项刷新重做日志
    1月22系统改规则了，退票后两个小时才会放出来所以这里无论做多少次都不会成功的
    只能把出错信息记录下，之后再不停刷，直到成功
    '''
    STATE_AVAILABLE = ((u'redoing', u'等待重做'), (u'finished', u'重做完成'), (u'failed', u'重做失败'))
    inTime = models.DateTimeField(u"出错时间", default=datetime.now)
    beginDay = models.CharField(u'出发日期', max_length=100)
    beginTime = models.CharField(u'出发时间', max_length=100)
    departure = models.CharField(u'出发码头', max_length=100)
    arrival = models.CharField(u'抵达码头', max_length=100)
    cnt = models.IntegerField(u'需票数')
    state = models.CharField(u'状态', choices=STATE_AVAILABLE, max_length=100)


    class Meta:
        verbose_name = u'重做信息'
        verbose_name_plural = u'(07)重做信息'


