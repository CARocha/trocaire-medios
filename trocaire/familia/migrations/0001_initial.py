# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Composicion'
        db.create_table('familia_composicion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sexo', self.gf('django.db.models.fields.IntegerField')()),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('estado', self.gf('django.db.models.fields.IntegerField')()),
            ('beneficio', self.gf('django.db.models.fields.IntegerField')()),
            ('relacion', self.gf('django.db.models.fields.IntegerField')()),
            ('sexo_jefe', self.gf('django.db.models.fields.IntegerField')()),
            ('num_familia', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('familia', ['Composicion'])

        # Adding model 'Descripcion'
        db.create_table('familia_descripcion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.IntegerField')()),
            ('femenino', self.gf('django.db.models.fields.IntegerField')()),
            ('masculino', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('familia', ['Descripcion'])

        # Adding model 'Escolaridad'
        db.create_table('familia_escolaridad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('beneficia', self.gf('django.db.models.fields.IntegerField')()),
            ('conyugue', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('familia', ['Escolaridad'])


    def backwards(self, orm):
        
        # Deleting model 'Composicion'
        db.delete_table('familia_composicion')

        # Deleting model 'Descripcion'
        db.delete_table('familia_descripcion')

        # Deleting model 'Escolaridad'
        db.delete_table('familia_escolaridad')


    models = {
        'familia.composicion': {
            'Meta': {'object_name': 'Composicion'},
            'beneficio': ('django.db.models.fields.IntegerField', [], {}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'estado': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_familia': ('django.db.models.fields.IntegerField', [], {}),
            'relacion': ('django.db.models.fields.IntegerField', [], {}),
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'sexo_jefe': ('django.db.models.fields.IntegerField', [], {})
        },
        'familia.descripcion': {
            'Meta': {'object_name': 'Descripcion'},
            'descripcion': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'femenino': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'masculino': ('django.db.models.fields.IntegerField', [], {})
        },
        'familia.escolaridad': {
            'Meta': {'object_name': 'Escolaridad'},
            'beneficia': ('django.db.models.fields.IntegerField', [], {}),
            'conyugue': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lugar.comarca': {
            'Meta': {'object_name': 'Comarca'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'medios.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'beneficiario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'comarca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Comarca']"}),
            'encuestador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Recolector']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"})
        },
        'medios.recolector': {
            'Meta': {'object_name': 'Recolector'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['familia']
