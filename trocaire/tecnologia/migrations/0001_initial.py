# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Riego'
        db.create_table('tecnologia_riego', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('tecnologia', ['Riego'])

        # Adding model 'AreaProtegida'
        db.create_table('tecnologia_areaprotegida', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('tecnologia', ['AreaProtegida'])

        # Adding model 'UsoTecnologia'
        db.create_table('tecnologia_usotecnologia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tecnologia', self.gf('django.db.models.fields.IntegerField')()),
            ('granos', self.gf('django.db.models.fields.IntegerField')()),
            ('anuales', self.gf('django.db.models.fields.IntegerField')()),
            ('permanentes', self.gf('django.db.models.fields.IntegerField')()),
            ('pastos', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('tecnologia', ['UsoTecnologia'])

        # Adding model 'Semilla'
        db.create_table('tecnologia_semilla', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('maiz', self.gf('django.db.models.fields.IntegerField')()),
            ('frijol', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('tecnologia', ['Semilla'])


    def backwards(self, orm):
        
        # Deleting model 'Riego'
        db.delete_table('tecnologia_riego')

        # Deleting model 'AreaProtegida'
        db.delete_table('tecnologia_areaprotegida')

        # Deleting model 'UsoTecnologia'
        db.delete_table('tecnologia_usotecnologia')

        # Deleting model 'Semilla'
        db.delete_table('tecnologia_semilla')


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
        'tecnologia.areaprotegida': {
            'Meta': {'object_name': 'AreaProtegida'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        'tecnologia.riego': {
            'Meta': {'object_name': 'Riego'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        'tecnologia.semilla': {
            'Meta': {'object_name': 'Semilla'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'frijol': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maiz': ('django.db.models.fields.IntegerField', [], {})
        },
        'tecnologia.usotecnologia': {
            'Meta': {'object_name': 'UsoTecnologia'},
            'anuales': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'granos': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pastos': ('django.db.models.fields.IntegerField', [], {}),
            'permanentes': ('django.db.models.fields.IntegerField', [], {}),
            'tecnologia': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['tecnologia']
