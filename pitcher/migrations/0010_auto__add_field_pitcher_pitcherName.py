# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Pitcher.pitcherName'
        db.add_column(u'pitcher_pitcher', 'pitcherName',
                      self.gf('django.db.models.fields.CharField')(default='1', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Pitcher.pitcherName'
        db.delete_column(u'pitcher_pitcher', 'pitcherName')


    models = {
        u'pitcher.flightconfig': {
            'Meta': {'ordering': "['flightCode']", 'object_name': 'FlightConfig'},
            'arrival': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'departure': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'departureTime': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'flightCode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pitcher.pitchconfig': {
            'Meta': {'ordering': "['priority', '-need']", 'object_name': 'PitchConfig'},
            'flight': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['pitcher.FlightConfig']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'need': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pitcher': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['pitcher.Pitcher']", 'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'pitcher.pitcher': {
            'Meta': {'object_name': 'Pitcher'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pitcherName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'working': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
            'pitcher': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['pitcher.Pitcher']", 'null': 'True', 'blank': 'True'}),
            'ticketCount': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pitcher.systemconfig': {
            'Meta': {'object_name': 'SystemConfig'},
            'errorWaitingSecond': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxException': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'maxLoginError': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'normalWaitingSecond': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'preceding': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'timeToStop': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pitcher.systemlog': {
            'Meta': {'object_name': 'SystemLog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logMsg': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'logTime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'pitcher': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['pitcher.Pitcher']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['pitcher']