# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ParamDescription.from_version'
        db.add_column('documentation_paramdescription', 'from_version',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['downloads.Release'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'FunctionDescription.from_version'
        db.add_column('documentation_functiondescription', 'from_version',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['downloads.Release'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'ClassDescription.from_version'
        db.add_column('documentation_classdescription', 'from_version',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['downloads.Release'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ParamDescription.from_version'
        db.delete_column('documentation_paramdescription', 'from_version_id')

        # Deleting field 'FunctionDescription.from_version'
        db.delete_column('documentation_functiondescription', 'from_version_id')

        # Deleting field 'ClassDescription.from_version'
        db.delete_column('documentation_classdescription', 'from_version_id')


    models = {
        'documentation.classdescription': {
            'Meta': {'ordering': "['name']", 'object_name': 'ClassDescription'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['page.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'descriptors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['documentation.TypeDescriptor']", 'symmetrical': 'False', 'through': "orm['documentation.ClassDescriptor']", 'blank': 'True'}),
            'from_version': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['downloads.Release']", 'null': 'True', 'blank': 'True'}),
            'functions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['documentation.FunctionDescription']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_data_field': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_field': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'documentation.classdescriptor': {
            'Meta': {'object_name': 'ClassDescriptor'},
            'clazz': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentation.ClassDescription']"}),
            'descriptor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentation.TypeDescriptor']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {})
        },
        'documentation.functiondescription': {
            'Meta': {'ordering': "['-is_constructor', 'name']", 'object_name': 'FunctionDescription'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'descriptors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['documentation.TypeDescriptor']", 'symmetrical': 'False', 'through': "orm['documentation.FunctionDescriptor']", 'blank': 'True'}),
            'from_version': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['downloads.Release']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_constructor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'params': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['documentation.ParamDescription']", 'null': 'True', 'through': "orm['documentation.Param']", 'blank': 'True'}),
            'returns': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentation.Type']", 'null': 'True', 'blank': 'True'})
        },
        'documentation.functiondescriptor': {
            'Meta': {'object_name': 'FunctionDescriptor'},
            'descriptor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentation.TypeDescriptor']"}),
            'function': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentation.FunctionDescription']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {})
        },
        'documentation.param': {
            'Meta': {'ordering': "['position']", 'object_name': 'Param'},
            'function': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentation.FunctionDescription']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'param': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentation.ParamDescription']"}),
            'position': ('django.db.models.fields.IntegerField', [], {})
        },
        'documentation.paramdescription': {
            'Meta': {'ordering': "['param__position']", 'object_name': 'ParamDescription'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'from_version': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['downloads.Release']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentation.Type']"})
        },
        'documentation.type': {
            'Meta': {'ordering': "['name']", 'object_name': 'Type'},
            'descriptors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['documentation.TypeDescriptor']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'documentation.typedescriptor': {
            'Meta': {'ordering': "['name']", 'object_name': 'TypeDescriptor'},
            'extends': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
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
        },
        'page.category': {
            'Meta': {'ordering': "['position']", 'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['page.Category']", 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['documentation']