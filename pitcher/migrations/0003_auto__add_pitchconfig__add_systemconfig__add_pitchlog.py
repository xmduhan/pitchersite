# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PitchConfig'
        db.create_table(u'pitcher_pitchconfig', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flightCode', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('departure', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('arrival', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('departureTime', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('need', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'pitcher', ['PitchConfig'])

        # Adding model 'SystemConfig'
        db.create_table(u'pitcher_systemconfig', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'pitcher', ['SystemConfig'])

        # Adding model 'PitchLog'
        db.create_table(u'pitcher_pitchlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pitchTime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('flightId', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('flightCode', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('departure', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('arrival', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('departureTime', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pitchCount', self.gf('django.db.models.fields.IntegerField')()),
            ('ticketCount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'pitcher', ['PitchLog'])


    def backwards(self, orm):
        # Deleting model 'PitchConfig'
        db.delete_table(u'pitcher_pitchconfig')

        # Deleting model 'SystemConfig'
        db.delete_table(u'pitcher_systemconfig')

        # Deleting model 'PitchLog'
        db.delete_table(u'pitcher_pitchlog')


    models = {
        u'pitcher.pitchconfig': {
            'Meta': {'object_name': 'PitchConfig'},
            'arrival': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'departure': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'departureTime': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'flightCode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'need': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'pitcher.pitchlog': {
            'Meta': {'object_name': 'PitchLog'},
            'arrival': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'departure': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'departureTime': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'flightCode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'flightId': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pitchCount': ('django.db.models.fields.IntegerField', [], {}),
            'pitchTime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'ticketCount': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pitcher.systemconfig': {
            'Meta': {'object_name': 'SystemConfig'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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