# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Release.source_available'
        db.add_column('downloads_release', 'source_available',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Release.source_available'
        db.delete_column('downloads_release', 'source_available')


    models = {
        'downloads.release': {
            'Meta': {'ordering': "['date']", 'object_name': 'Release'},
            'available_as_tar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'available_as_zip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'change_log': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'previous_version': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['downloads.Release']", 'null': 'True', 'blank': 'True'}),
            'source_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['downloads']