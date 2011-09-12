# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'FacebookUser.username'
        db.delete_column('facebook_facebookuser', 'username')

        # Adding field 'FacebookUser.name'
        db.add_column('facebook_facebookuser', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'FacebookUser.link'
        db.add_column('facebook_facebookuser', 'link', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'FacebookUser.username'
        db.add_column('facebook_facebookuser', 'username', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Deleting field 'FacebookUser.name'
        db.delete_column('facebook_facebookuser', 'name')

        # Deleting field 'FacebookUser.link'
        db.delete_column('facebook_facebookuser', 'link')


    models = {
        'facebook.facebookuser': {
            'Meta': {'object_name': 'FacebookUser'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['facebook']
