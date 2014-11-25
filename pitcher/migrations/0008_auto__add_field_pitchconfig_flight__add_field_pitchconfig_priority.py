# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PitchConfig.flight'
        db.add_column(u'pitcher_pitchconfig', 'flight',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['pitcher.FlightConfig'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'PitchConfig.priority'
        db.add_column(u'pitcher_pitchconfig', 'priority',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PitchConfig.flight'
        db.delete_column(u'pitcher_pitchconfig', 'flight_id')

        # Deleting field 'PitchConfig.priority'
        db.delete_column(u'pitcher_pitchconfig', 'priority')


    models = {
        u'pitcher.flightconfig': {
            'Meta': {'object_name': 'FlightConfig'},
            'arrival': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'departure': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'departureTime': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'flightCode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pitcher.pitchconfig': {
            'Meta': {'object_name': 'PitchConfig'},
            'flight': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['pitcher.FlightConfig']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'need': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'pitcher.pitchlog': {
            'Meta': {'object_name': 'PitchLog'},
            'arrival': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'departure': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'departureTime': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'flightCode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'flightId': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'need': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pitchCount': ('django.db.models.fields.IntegerField', [], {}),
            'pitchTime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'ticketCount': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pitcher.systemconfig': {
            'Meta': {'object_name': 'SystemConfig'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'preceding': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'working': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'pitcher.systemlog': {
            'Meta': {'object_name': 'SystemLog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logMsg': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'logTime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
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