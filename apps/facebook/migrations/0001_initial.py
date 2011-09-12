# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FacebookUser'
        db.create_table('facebook_facebookuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facebook_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('facebook', ['FacebookUser'])


    def backwards(self, orm):
        
        # Deleting model 'FacebookUser'
        db.delete_table('facebook_facebookuser')


    models = {
        'facebook.facebookuser': {
            'Meta': {'object_name': 'FacebookUser'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['facebook']
