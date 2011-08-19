# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Product'
        db.create_table('contest_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('contest', ['Product'])

        # Adding model 'Options'
        db.create_table('contest_options', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profile.Profile'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contest.Product'])),
        ))
        db.send_create_signal('contest', ['Options'])

        # Adding model 'Draw'
        db.create_table('contest_draw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('play_date', self.gf('django.db.models.fields.DateField')()),
            ('winner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profile.Profile'])),
        ))
        db.send_create_signal('contest', ['Draw'])


    def backwards(self, orm):
        
        # Deleting model 'Product'
        db.delete_table('contest_product')

        # Deleting model 'Options'
        db.delete_table('contest_options')

        # Deleting model 'Draw'
        db.delete_table('contest_draw')


    models = {
        'contest.draw': {
            'Meta': {'object_name': 'Draw'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'play_date': ('django.db.models.fields.DateField', [], {}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profile.Profile']"})
        },
        'contest.options': {
            'Meta': {'object_name': 'Options'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profile.Profile']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contest.Product']"})
        },
        'contest.product': {
            'Meta': {'object_name': 'Product'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'profile.profile': {
            'Meta': {'object_name': 'Profile'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'document_code': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'ubigeo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ubigeo.Ubigeo']"})
        },
        'ubigeo.ubigeo': {
            'Meta': {'object_name': 'Ubigeo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ubigeo.Ubigeo']"})
        }
    }

    complete_apps = ['contest']
