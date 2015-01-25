# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RefreshRedo'
        db.create_table(u'pitcher_refreshredo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('beginDay', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('beginTime', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('departure', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('arrival', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cnt', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'pitcher', ['RefreshRedo'])


    def backwards(self, orm):
        # Deleting model 'RefreshRedo'
        db.delete_table(u'pitcher_refreshredo')


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
            'Meta': {'ordering': "['task', 'priority', '-need']", 'object_name': 'PitchConfig'},
            'flight': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['pitcher.FlightConfig']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'need': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['pitcher.Task']", 'null': 'True', 'blank': 'True'})
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
            'task': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['pitcher.Task']", 'null': 'True', 'blank': 'True'}),
            'ticketCount': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pitcher.refreshredo': {
            'Meta': {'object_name': 'RefreshRedo'},
            'arrival': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'beginDay': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'beginTime': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cnt': ('django.db.models.fields.IntegerField', [], {}),
            'departure': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'task': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['pitcher.Task']", 'null': 'True', 'blank': 'True'})
        },
        u'pitcher.task': {
            'Meta': {'ordering': "['taskName']", 'object_name': 'Task'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'taskName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'pitch'", 'max_length': '10'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'working': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['pitcher']