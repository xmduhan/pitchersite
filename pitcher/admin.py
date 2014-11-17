from django.contrib import admin
from models import *

# Register your models here.

class TicketCountLogAdmin(admin.ModelAdmin):
    fields = [
        'logTime', 'seq', 'departure', 'arrival', 'flightCode', 'departureTime', 'price', 'ticketCount', 'flightId'
    ]
    list_display = (
    'logTime', 'seq', 'departure', 'arrival', 'flightCode', 'departureTime', 'price', 'ticketCount', 'flightId')


admin.site.register(TicketCountLog, TicketCountLogAdmin)