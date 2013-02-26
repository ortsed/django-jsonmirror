# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'JSON_Archive.external_id'
        db.alter_column('jsonmirror_json_archive', 'external_id', self.gf('django.db.models.fields.CharField')(max_length=1000))

    def backwards(self, orm):

        # Changing field 'JSON_Archive.external_id'
        db.alter_column('jsonmirror_json_archive', 'external_id', self.gf('django.db.models.fields.PositiveIntegerField')())

    models = {
        'jsonmirror.json_archive': {
            'Meta': {'object_name': 'JSON_Archive'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
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