# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'FacebookUser.created_date'
        db.add_column('facebook_facebookuser', 'created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2011, 9, 12, 1, 28, 32, 809533), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'FacebookUser.created_date'
        db.delete_column('facebook_facebookuser', 'created_date')


    models = {
        'facebook.facebookuser': {
            'Meta': {'object_name': 'FacebookUser'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['facebook']
