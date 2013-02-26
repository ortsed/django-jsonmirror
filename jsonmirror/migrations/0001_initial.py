# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'JSON_Archive_Set'
        db.create_table('jsonmirror_json_archive_set', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.URLField')(unique=True, max_length=200)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('jsonmirror', ['JSON_Archive_Set'])

        # Adding model 'JSON_Archive'
        db.create_table('jsonmirror_json_archive', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('set', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jsonmirror.JSON_Archive_Set'])),
            ('external_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('jsonmirror', ['JSON_Archive'])


    def backwards(self, orm):
        # Deleting model 'JSON_Archive_Set'
        db.delete_table('jsonmirror_json_archive_set')

        # Deleting model 'JSON_Archive'
        db.delete_table('jsonmirror_json_archive')


    models = {
        'jsonmirror.json_archive': {
            'Meta': {'object_name': 'JSON_Archive'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'external_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['jsonmirror.JSON_Archive_Set']"})
        },
        'jsonmirror.json_archive_set': {
            'Meta': {'object_name': 'JSON_Archive_Set'},
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['jsonmirror']