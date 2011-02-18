# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ClassDescription'
        db.create_table('documentation_classdescription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['page.Category'])),
            ('is_data_field', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_field', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('documentation', ['ClassDescription'])

        # Adding M2M table for field functions on 'ClassDescription'
        db.create_table('documentation_classdescription_functions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('classdescription', models.ForeignKey(orm['documentation.classdescription'], null=False)),
            ('functiondescription', models.ForeignKey(orm['documentation.functiondescription'], null=False))
        ))
        db.create_unique('documentation_classdescription_functions', ['classdescription_id', 'functiondescription_id'])

        # Adding model 'FunctionDescription'
        db.create_table('documentation_functiondescription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('is_constructor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('returns', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documentation.Type'], null=True, blank=True)),
        ))
        db.send_create_signal('documentation', ['FunctionDescription'])

        # Adding model 'ClassDescriptor'
        db.create_table('documentation_classdescriptor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clazz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documentation.ClassDescription'])),
            ('descriptor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documentation.TypeDescriptor'])),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('documentation', ['ClassDescriptor'])

        # Adding model 'FunctionDescriptor'
        db.create_table('documentation_functiondescriptor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('function', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documentation.FunctionDescription'])),
            ('descriptor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documentation.TypeDescriptor'])),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('documentation', ['FunctionDescriptor'])

        # Adding model 'Param'
        db.create_table('documentation_param', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('param', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documentation.ParamDescription'])),
            ('function', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documentation.FunctionDescription'])),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('documentation', ['Param'])

        # Adding model 'ParamDescription'
        db.create_table('documentation_paramdescription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documentation.Type'])),
        ))
        db.send_create_signal('documentation', ['ParamDescription'])

        # Adding model 'Type'
        db.create_table('documentation_type', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal('documentation', ['Type'])

        # Adding M2M table for field descriptors on 'Type'
        db.create_table('documentation_type_descriptors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('type', models.ForeignKey(orm['documentation.type'], null=False)),
            ('typedescriptor', models.ForeignKey(orm['documentation.typedescriptor'], null=False))
        ))
        db.create_unique('documentation_type_descriptors', ['type_id', 'typedescriptor_id'])

        # Adding model 'TypeDescriptor'
        db.create_table('documentation_typedescriptor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('extends', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
        ))
        db.send_create_signal('documentation', ['TypeDescriptor'])


    def backwards(self, orm):
        
        # Deleting model 'ClassDescription'
        db.delete_table('documentation_classdescription')

        # Removing M2M table for field functions on 'ClassDescription'
        db.delete_table('documentation_classdescription_functions')

        # Deleting model 'FunctionDescription'
        db.delete_table('documentation_functiondescription')

        # Deleting model 'ClassDescriptor'
        db.delete_table('documentation_classdescriptor')

        # Deleting model 'FunctionDescriptor'
        db.delete_table('documentation_functiondescriptor')

        # Deleting model 'Param'
        db.delete_table('documentation_param')

        # Deleting model 'ParamDescription'
        db.delete_table('documentation_paramdescription')

        # Deleting model 'Type'
        db.delete_table('documentation_type')

        # Removing M2M table for field descriptors on 'Type'
        db.delete_table('documentation_type_descriptors')

        # Deleting model 'TypeDescriptor'
        db.delete_table('documentation_typedescriptor')


    models = {
        'documentation.classdescription': {
            'Meta': {'ordering': "['name']", 'object_name': 'ClassDescription'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['page.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'descriptors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['documentation.TypeDescriptor']", 'symmetrical': 'False', 'through': "orm['documentation.ClassDescriptor']", 'blank': 'True'}),
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
        'page.category': {
            'Meta': {'ordering': "['position']", 'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['page.Category']", 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['documentation']
