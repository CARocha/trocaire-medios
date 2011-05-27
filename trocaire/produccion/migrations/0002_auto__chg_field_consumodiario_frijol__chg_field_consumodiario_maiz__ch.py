# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'ConsumoDiario.frijol'
        db.alter_column('produccion_consumodiario', 'frijol', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'ConsumoDiario.maiz'
        db.alter_column('produccion_consumodiario', 'maiz', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'CultivosPeriodos.postrera'
        db.alter_column('produccion_cultivosperiodos', 'postrera', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'CultivosPeriodos.p_primera'
        db.alter_column('produccion_cultivosperiodos', 'p_primera', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'CultivosPeriodos.p_postrera'
        db.alter_column('produccion_cultivosperiodos', 'p_postrera', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'CultivosPeriodos.p_apante'
        db.alter_column('produccion_cultivosperiodos', 'p_apante', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'CultivosPeriodos.apante'
        db.alter_column('produccion_cultivosperiodos', 'apante', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'CultivosPeriodos.primera'
        db.alter_column('produccion_cultivosperiodos', 'primera', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Arboles.patio'
        db.alter_column('produccion_arboles', 'patio', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Arboles.otra'
        db.alter_column('produccion_arboles', 'otra', self.gf('django.db.models.fields.FloatField')())


    def backwards(self, orm):
        
        # Changing field 'ConsumoDiario.frijol'
        db.alter_column('produccion_consumodiario', 'frijol', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ConsumoDiario.maiz'
        db.alter_column('produccion_consumodiario', 'maiz', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CultivosPeriodos.postrera'
        db.alter_column('produccion_cultivosperiodos', 'postrera', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CultivosPeriodos.p_primera'
        db.alter_column('produccion_cultivosperiodos', 'p_primera', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CultivosPeriodos.p_postrera'
        db.alter_column('produccion_cultivosperiodos', 'p_postrera', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CultivosPeriodos.p_apante'
        db.alter_column('produccion_cultivosperiodos', 'p_apante', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CultivosPeriodos.apante'
        db.alter_column('produccion_cultivosperiodos', 'apante', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CultivosPeriodos.primera'
        db.alter_column('produccion_cultivosperiodos', 'primera', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Arboles.patio'
        db.alter_column('produccion_arboles', 'patio', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Arboles.otra'
        db.alter_column('produccion_arboles', 'otra', self.gf('django.db.models.fields.IntegerField')())


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
        'medios.contraparte': {
            'Meta': {'object_name': 'Contraparte'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'medios.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'beneficiario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'comarca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Comarca']"}),
            'contraparte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Contraparte']", 'null': 'True', 'blank': 'True'}),
            'encuestador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Recolector']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"})
        },
        'medios.recolector': {
            'Meta': {'object_name': 'Recolector'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'produccion.arboles': {
            'Meta': {'object_name': 'Arboles'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otra': ('django.db.models.fields.FloatField', [], {}),
            'patio': ('django.db.models.fields.FloatField', [], {})
        },
        'produccion.calidadpatio': {
            'Meta': {'object_name': 'CalidadPatio'},
            'calidad': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'produccion.canuales': {
            'Meta': {'object_name': 'CAnuales'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'produccion.chortalizas': {
            'Meta': {'object_name': 'CHortalizas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'produccion.consumodiario': {
            'Meta': {'object_name': 'ConsumoDiario'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'frijol': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maiz': ('django.db.models.fields.FloatField', [], {})
        },
        'produccion.cperiodos': {
            'Meta': {'object_name': 'CPeriodos'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'produccion.cpermanentes': {
            'Meta': {'object_name': 'CPermanentes'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'produccion.cultivosanuales': {
            'Meta': {'object_name': 'CultivosAnuales'},
            'cultivos': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['produccion.CAnuales']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manzana': ('django.db.models.fields.FloatField', [], {}),
            'produccion': ('django.db.models.fields.FloatField', [], {})
        },
        'produccion.cultivosperiodos': {
            'Meta': {'object_name': 'CultivosPeriodos'},
            'apante': ('django.db.models.fields.FloatField', [], {}),
            'cultivos': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['produccion.CPeriodos']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_apante': ('django.db.models.fields.FloatField', [], {}),
            'p_postrera': ('django.db.models.fields.FloatField', [], {}),
            'p_primera': ('django.db.models.fields.FloatField', [], {}),
            'postrera': ('django.db.models.fields.FloatField', [], {}),
            'primera': ('django.db.models.fields.FloatField', [], {})
        },
        'produccion.cultivospermanentes': {
            'Meta': {'object_name': 'CultivosPermanentes'},
            'cultivos': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['produccion.CPermanentes']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manzana': ('django.db.models.fields.FloatField', [], {}),
            'produccion': ('django.db.models.fields.FloatField', [], {})
        },
        'produccion.ganado': {
            'Meta': {'object_name': 'Ganado'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'produccion.ganadomayor': {
            'Meta': {'object_name': 'GanadoMayor'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'ganado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['produccion.Ganado']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'produccion.hortalizas': {
            'Meta': {'object_name': 'Hortalizas'},
            'cultivos': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['produccion.CHortalizas']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manzana': ('django.db.models.fields.FloatField', [], {}),
            'produccion': ('django.db.models.fields.FloatField', [], {})
        },
        'produccion.limitaciones': {
            'Meta': {'object_name': 'Limitaciones'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'produccion.patiocultivada': {
            'Meta': {'object_name': 'PatioCultivada'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invierno': ('django.db.models.fields.FloatField', [], {}),
            'verano': ('django.db.models.fields.FloatField', [], {})
        },
        'produccion.principallimitacion': {
            'Meta': {'object_name': 'PrincipalLimitacion'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uno'", 'to': "orm['produccion.Limitaciones']"}),
            'opcion2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dos'", 'to': "orm['produccion.Limitaciones']"}),
            'opcion3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tres'", 'to': "orm['produccion.Limitaciones']"})
        }
    }

    complete_apps = ['produccion']
