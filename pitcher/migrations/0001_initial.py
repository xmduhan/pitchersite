# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'TicketCountLog'
        db.create_table(u'pitcher_ticketcountlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('logTime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('seq', self.gf('django.db.models.fields.IntegerField')()),
            ('departure', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('arrival', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('flightCode', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('departureTime', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('ticketCount', self.gf('django.db.models.fields.IntegerField')()),
            ('flightId', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'pitcher', ['TicketCountLog'])


    def backwards(self, orm):
        # Deleting model 'TicketCountLog'
        db.delete_table(u'pitcher_ticketcountlog')


    models = {
        u'pitcher.ticketcountlog': {
            'Meta': {'object_name': 'TicketCountLog'},
            'arrival': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'departure': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'departureTime': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'flightCode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'flightId': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logTime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'seq': ('django.db.models.fields.IntegerField', [], {}),
            'ticketCount': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['pitcher']