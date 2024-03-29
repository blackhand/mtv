# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Profile.register_date'
        db.add_column('profile_profile', 'register_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Profile.register_date'
        db.delete_column('profile_profile', 'register_date')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'profile.profile': {
            'Meta': {'object_name': 'Profile'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'document_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '8'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'first_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_participant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_winner': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'register_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'second_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'ubigeo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ubigeo.Ubigeo']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'profile.tblusuarios': {
            'Meta': {'object_name': 'TblUsuarios', 'db_table': "u'tbl_usuarios'", 'managed': 'False'},
            'date_nacimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_registro': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'int_operador': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'pk_usuario': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'txt_apellido_materno': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'txt_apellido_paterno': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'txt_celular': ('django.db.models.fields.CharField', [], {'max_length': '27', 'blank': 'True'}),
            'txt_correo': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'txt_departamento': ('django.db.models.fields.CharField', [], {'max_length': '240', 'blank': 'True'}),
            'txt_direccion': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'txt_distrito': ('django.db.models.fields.CharField', [], {'max_length': '450', 'blank': 'True'}),
            'txt_nombre': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'txt_num_doc': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '24', 'blank': 'True'}),
            'txt_provincia': ('django.db.models.fields.CharField', [], {'max_length': '240', 'blank': 'True'}),
            'txt_telefono': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'txt_tipo_doc': ('django.db.models.fields.CharField', [], {'max_length': '90', 'blank': 'True'})
        },
        'ubigeo.ubigeo': {
            'Meta': {'object_name': 'Ubigeo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ubigeo.Ubigeo']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['profile']
