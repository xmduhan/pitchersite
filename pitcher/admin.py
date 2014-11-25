# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

# Register your models here.


class TicketCountLogAdmin(admin.ModelAdmin):
    '''
    船票数量日志
    '''
    fields = [
        'logTime', 'seq', 'departure', 'arrival', 'flightCode', 'departureTime', 'price', 'ticketCount', 'flightId'
    ]
    list_display = (
        'logTime', 'seq', 'departure', 'arrival', 'flightCode', 'departureTime', 'price', 'ticketCount', 'flightId')


#admin.site.register(TicketCountLog, TicketCountLogAdmin)


class SystemLogAdmin(admin.ModelAdmin):
    '''
    系统日志
    '''
    fields = [
        'logTime', 'logMsg'
    ]
    list_display = ('logTime', 'logMsg')


admin.site.register(SystemLog, SystemLogAdmin)


class SystemConfigAdmin(admin.ModelAdmin):
    '''
    全局配置
    '''
    fields = [
        'username', 'password', 'preceding', 'working'
    ]
    list_display = ( 'username', 'password', 'preceding', 'working')


admin.site.register(SystemConfig, SystemConfigAdmin)


class PitchConfigAdmin(admin.ModelAdmin):
    '''
    抢票配置
    '''
    fields = [
        'flight', 'need', 'priority'
    ]
    list_display = ('flight', 'need', 'priority')


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
        'pitchTime', 'flightId', 'flightCode', 'departure', 'arrival', 'departureTime', 'pitchCount', 'ticketCount'
    ]
    list_display = (
        'pitchTime', 'flightId', 'flightCode', 'departure', 'arrival', 'departureTime', 'pitchCount', 'ticketCount'
    )


admin.site.register(PitchLog, PitchLogAdmin)

