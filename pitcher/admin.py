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


admin.site.register(TicketCountLog, TicketCountLogAdmin)


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
        'username', 'password'
    ]
    list_display = ( 'username', 'password')


admin.site.register(SystemConfig, SystemConfigAdmin)


class PitchConfigAdmin(admin.ModelAdmin):
    '''
    抢票配置
    '''
    fields = [
        'flightCode', 'departure', 'arrival', 'departureTime', 'need'
    ]
    list_display = ('flightCode', 'departure', 'arrival', 'departureTime', 'need')


admin.site.register(PitchConfig, PitchConfigAdmin)

