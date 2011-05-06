# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Participacion'
        db.create_table('participacion_ciudadana_participacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organismo', self.gf('django.db.models.fields.IntegerField')()),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('participacion_ciudadana', ['Participacion'])

        # Adding model 'ParticipacionCPC'
        db.create_table('participacion_ciudadana_participacioncpc', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organismo', self.gf('django.db.models.fields.IntegerField')()),
            ('hombre', self.gf('django.db.models.fields.IntegerField')()),
            ('mujer', self.gf('django.db.models.fields.IntegerField')()),
            ('ambos', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('participacion_ciudadana', ['ParticipacionCPC'])

        # Adding model 'Frecuencia'
        db.create_table('participacion_ciudadana_frecuencia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organismo', self.gf('django.db.models.fields.IntegerField')()),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('participacion_ciudadana', ['Frecuencia'])


    def backwards(self, orm):
        
        # Deleting model 'Participacion'
        db.delete_table('participacion_ciudadana_participacion')

        # Deleting model 'ParticipacionCPC'
        db.delete_table('participacion_ciudadana_participacioncpc')

        # Deleting model 'Frecuencia'
        db.delete_table('participacion_ciudadana_frecuencia')


    models = {
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
        },
        'participacion_ciudadana.frecuencia': {
            'Meta': {'object_name': 'Frecuencia'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organismo': ('django.db.models.fields.IntegerField', [], {}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        'participacion_ciudadana.participacion': {
            'Meta': {'object_name': 'Participacion'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organismo': ('django.db.models.fields.IntegerField', [], {}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        'participacion_ciudadana.participacioncpc': {
            'Meta': {'object_name': 'ParticipacionCPC'},
            'ambos': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'hombre': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mujer': ('django.db.models.fields.IntegerField', [], {}),
            'organismo': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['participacion_ciudadana']
