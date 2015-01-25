# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

# Register your models here.


# class TicketCountLogAdmin(admin.ModelAdmin):
#     '''
#     船票数量日志
#     '''
#     fields = [
#         'logTime', 'seq', 'departure', 'arrival', 'flightCode', 'departureTime', 'price', 'ticketCount', 'flightId'
#     ]
#     list_display = (
#         'logTime', 'seq', 'departure', 'arrival', 'flightCode', 'departureTime', 'price', 'ticketCount', 'flightId')
#
#
# #admin.site.register(TicketCountLog, TicketCountLogAdmin)


class SystemLogAdmin(admin.ModelAdmin):
    '''
    系统日志
    '''
    fields = [
        'task', 'logTime', 'logMsg'
    ]
    list_display = ('task', 'logTime', 'logMsg')
    list_filter = ["task"]
    date_hierarchy = 'logTime'


admin.site.register(SystemLog, SystemLogAdmin)


class SystemConfigAdmin(admin.ModelAdmin):
    '''
    全局配置
    '''
    fields = [
        'normalWaitingSecond', 'errorWaitingSecond', 'maxLoginError', 'maxException', 'timeToStop', 'preceding'
    ]
    list_display = (
        'normalWaitingSecond', 'errorWaitingSecond', 'maxLoginError', 'maxException', 'timeToStop', 'preceding')


admin.site.register(SystemConfig, SystemConfigAdmin)


class TaskAdmin(admin.ModelAdmin):
    '''
    抢票配置
    '''
    fields = [
        'taskName', 'username', 'password', 'type', 'working'
    ]
    list_display = ('taskName', 'username', 'type', 'working')


admin.site.register(Task, TaskAdmin)


class PitchConfigAdmin(admin.ModelAdmin):
    '''
    抢票配置
    '''
    fields = [
        'task', 'flight', 'need', 'priority'
    ]
    list_display = ('task', 'flight', 'need', 'priority')
    list_filter = ["task"]


admin.site.register(PitchConfig, PitchConfigAdmin)


class FlightConfigAdmin(admin.ModelAdmin):
    '''
    航班配置
    '''
    fields = [
        'flightCode', 'departure', 'arrival', 'departureTime'
    ]
    list_display = ('flightCode', 'departure', 'arrival', 'departureTime')


admin.site.register(FlightConfig, FlightConfigAdmin)


class PitchLogAdmin(admin.ModelAdmin):
    '''
    抢票记录
    '''
    fields = [
        'pitchTime', 'task', 'flightId', 'flightCode', 'departure', 'arrival', 'departureTime', 'need', 'pitchCount',
        'ticketCount'
    ]
    list_display = (
        'pitchTime', 'task', 'flightId', 'flightCode', 'departure', 'arrival', 'departureTime', 'need', 'pitchCount',
        'ticketCount'
    )
    list_filter = ["task"]

    date_hierarchy = 'pitchTime'
    #list_filter=["pitchMonth"]
    #search_fields=["pitchTime"]

admin.site.register(PitchLog, PitchLogAdmin)


class RefreshRedoAdmin(admin.ModelAdmin):
    fields = [
        'beginDay', 'beginTime', 'departure', 'arrival', 'cnt', 'state',
    ]
    list_display = (
        'beginDay', 'beginTime', 'departure', 'arrival', 'cnt', 'state',
    )
    list_filter = ["state"]


admin.site.register(RefreshRedo, RefreshRedoAdmin)
