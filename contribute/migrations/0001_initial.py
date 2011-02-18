# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BugReport'
        db.create_table('contribute_bugreport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('overview', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contribute.User'])),
            ('reported_on', self.gf('django.db.models.fields.DateField')()),
            ('accepted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('open', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('severity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_changed', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('contribute', ['BugReport'])

        # Adding M2M table for field comments on 'BugReport'
        db.create_table('contribute_bugreport_comments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bugreport', models.ForeignKey(orm['contribute.bugreport'], null=False)),
            ('comment', models.ForeignKey(orm['contribute.comment'], null=False))
        ))
        db.create_unique('contribute_bugreport_comments', ['bugreport_id', 'comment_id'])

        # Adding model 'FeatureRequest'
        db.create_table('contribute_featurerequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('overview', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contribute.User'])),
            ('filed', self.gf('django.db.models.fields.DateField')()),
            ('accepted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_changed', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('contribute', ['FeatureRequest'])

        # Adding M2M table for field comments on 'FeatureRequest'
        db.create_table('contribute_featurerequest_comments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('featurerequest', models.ForeignKey(orm['contribute.featurerequest'], null=False)),
            ('comment', models.ForeignKey(orm['contribute.comment'], null=False))
        ))
        db.create_unique('contribute_featurerequest_comments', ['featurerequest_id', 'comment_id'])

        # Adding model 'Comment'
        db.create_table('contribute_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contribute.User'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('contribute', ['Comment'])

        # Adding model 'User'
        db.create_table('contribute_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=56)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('blacklisted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('contribute', ['User'])


    def backwards(self, orm):
        
        # Deleting model 'BugReport'
        db.delete_table('contribute_bugreport')

        # Removing M2M table for field comments on 'BugReport'
        db.delete_table('contribute_bugreport_comments')

        # Deleting model 'FeatureRequest'
        db.delete_table('contribute_featurerequest')

        # Removing M2M table for field comments on 'FeatureRequest'
        db.delete_table('contribute_featurerequest_comments')

        # Deleting model 'Comment'
        db.delete_table('contribute_comment')

        # Deleting model 'User'
        db.delete_table('contribute_user')


    models = {
        'contribute.bugreport': {
            'Meta': {'object_name': 'BugReport'},
            'accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contribute.User']"}),
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contribute.Comment']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_changed': ('django.db.models.fields.DateField', [], {}),
            'open': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'overview': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'reported_on': ('django.db.models.fields.DateField', [], {}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contribute.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contribute.User']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contribute.featurerequest': {
            'Meta': {'object_name': 'FeatureRequest'},
            'accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contribute.User']"}),
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contribute.Comment']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'filed': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_changed': ('django.db.models.fields.DateField', [], {}),
            'overview': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contribute.user': {
            'Meta': {'object_name': 'User'},
            'blacklisted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '56'})
        }
    }

    complete_apps = ['contribute']
