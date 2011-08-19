# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Ubigeo'
        db.create_table('ubigeo_ubigeo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ubigeo.Ubigeo'])),
        ))
        db.send_create_signal('ubigeo', ['Ubigeo'])


    def backwards(self, orm):
        
        # Deleting model 'Ubigeo'
        db.delete_table('ubigeo_ubigeo')


    models = {
        'ubigeo.ubigeo': {
            'Meta': {'object_name': 'Ubigeo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ubigeo.Ubigeo']"})
        }
    }

    complete_apps = ['ubigeo']
