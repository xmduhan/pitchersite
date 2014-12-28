# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'TicketCountLog'
        db.delete_table(u'pitcher_ticketcountlog')

        # Adding model 'Pitcher'
        db.create_table(u'pitcher_pitcher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('working', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'pitcher', ['Pitcher'])

        # Deleting field 'SystemConfig.username'
        db.delete_column(u'pitcher_systemconfig', 'username')

        # Deleting field 'SystemConfig.working'
        db.delete_column(u'pitcher_systemconfig', 'working')

        # Deleting field 'SystemConfig.password'
        db.delete_column(u'pitcher_systemconfig', 'password')

        # Adding field 'SystemConfig.normalWaitingSecond'
        db.add_column(u'pitcher_systemconfig', 'normalWaitingSecond',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)

        # Adding field 'SystemConfig.errorWaitingSecond'
        db.add_column(u'pitcher_systemconfig', 'errorWaitingSecond',
                      self.gf('django.db.models.fields.IntegerField')(default=5),
                      keep_default=False)

        # Adding field 'SystemConfig.maxLoginError'
        db.add_column(u'pitcher_systemconfig', 'maxLoginError',
                      self.gf('django.db.models.fields.IntegerField')(default=5),
                      keep_default=False)

        # Adding field 'SystemConfig.maxException'
        db.add_column(u'pitcher_systemconfig', 'maxException',
                      self.gf('django.db.models.fields.IntegerField')(default=5),
                      keep_default=False)

        # Adding field 'SystemConfig.timeToStop'
        db.add_column(u'pitcher_systemconfig', 'timeToStop',
                      self.gf('django.db.models.fields.CharField')(default='12:30', max_length=100),
                      keep_default=False)

        # Adding field 'PitchConfig.pitcher'
        db.add_column(u'pitcher_pitchconfig', 'pitcher',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['pitcher.Pitcher'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'PitchLog.pitcher'
        db.add_column(u'pitcher_pitchlog', 'pitcher',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['pitcher.Pitcher'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'SystemLog.pitcher'
        db.add_column(u'pitcher_systemlog', 'pitcher',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['pitcher.Pitcher'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'TicketCountLog'
        db.create_table(u'pitcher_ticketcountlog', (
            ('arrival', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('flightId', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('seq', self.gf('django.db.models.fields.IntegerField')()),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('ticketCount', self.gf('django.db.models.fields.IntegerField')()),
            ('logTime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('departureTime', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('flightCode', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('departure', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'pitcher', ['TicketCountLog'])

        # Deleting model 'Pitcher'
        db.delete_table(u'pitcher_pitcher')

        # Adding field 'SystemConfig.username'
        db.add_column(u'pitcher_systemconfig', 'username',
                      self.gf('django.db.models.fields.CharField')(default='nonname', max_length=100),
                      keep_default=False)

        # Adding field 'SystemConfig.working'
        db.add_column(u'pitcher_systemconfig', 'working',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'SystemConfig.password'
        db.add_column(u'pitcher_systemconfig', 'password',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Deleting field 'SystemConfig.normalWaitingSecond'
        db.delete_column(u'pitcher_systemconfig', 'normalWaitingSecond')

        # Deleting field 'SystemConfig.errorWaitingSecond'
        db.delete_column(u'pitcher_systemconfig', 'errorWaitingSecond')

        # Deleting field 'SystemConfig.maxLoginError'
        db.delete_column(u'pitcher_systemconfig', 'maxLoginError')

        # Deleting field 'SystemConfig.maxException'
        db.delete_column(u'pitcher_systemconfig', 'maxException')

        # Deleting field 'SystemConfig.timeToStop'
        db.delete_column(u'pitcher_systemconfig', 'timeToStop')

        # Deleting field 'PitchConfig.pitcher'
        db.delete_column(u'pitcher_pitchconfig', 'pitcher_id')

        # Deleting field 'PitchLog.pitcher'
        db.delete_column(u'pitcher_pitchlog', 'pitcher_id')

        # Deleting field 'SystemLog.pitcher'
        db.delete_column(u'pitcher_systemlog', 'pitcher_id')


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