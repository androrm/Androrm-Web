# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Release'
        db.create_table('downloads_release', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('change_log', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('previous_version', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['downloads.Release'], null=True, blank=True)),
        ))
        db.send_create_signal('downloads', ['Release'])


    def backwards(self, orm):
        
        # Deleting model 'Release'
        db.delete_table('downloads_release')


    models = {
        'downloads.release': {
            'Meta': {'ordering': "['date']", 'object_name': 'Release'},
            'change_log': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'previous_version': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['downloads.Release']", 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['downloads']
