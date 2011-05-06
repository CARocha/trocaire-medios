# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CPeriodos'
        db.create_table('produccion_cperiodos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal('produccion', ['CPeriodos'])

        # Adding model 'CPermanentes'
        db.create_table('produccion_cpermanentes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal('produccion', ['CPermanentes'])

        # Adding model 'CAnuales'
        db.create_table('produccion_canuales', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal('produccion', ['CAnuales'])

        # Adding model 'CHortalizas'
        db.create_table('produccion_chortalizas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal('produccion', ['CHortalizas'])

        # Adding model 'CultivosPeriodos'
        db.create_table('produccion_cultivosperiodos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cultivos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion.CPeriodos'])),
            ('primera', self.gf('django.db.models.fields.IntegerField')()),
            ('postrera', self.gf('django.db.models.fields.IntegerField')()),
            ('apante', self.gf('django.db.models.fields.IntegerField')()),
            ('p_primera', self.gf('django.db.models.fields.IntegerField')()),
            ('p_postrera', self.gf('django.db.models.fields.IntegerField')()),
            ('p_apante', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('produccion', ['CultivosPeriodos'])

        # Adding model 'CultivosPermanentes'
        db.create_table('produccion_cultivospermanentes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cultivos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion.CPermanentes'])),
            ('manzana', self.gf('django.db.models.fields.FloatField')()),
            ('produccion', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('produccion', ['CultivosPermanentes'])

        # Adding model 'CultivosAnuales'
        db.create_table('produccion_cultivosanuales', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cultivos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion.CAnuales'])),
            ('manzana', self.gf('django.db.models.fields.FloatField')()),
            ('produccion', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('produccion', ['CultivosAnuales'])

        # Adding model 'Hortalizas'
        db.create_table('produccion_hortalizas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cultivos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion.CHortalizas'])),
            ('manzana', self.gf('django.db.models.fields.FloatField')()),
            ('produccion', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('produccion', ['Hortalizas'])

        # Adding model 'ConsumoDiario'
        db.create_table('produccion_consumodiario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('maiz', self.gf('django.db.models.fields.IntegerField')()),
            ('frijol', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('produccion', ['ConsumoDiario'])

        # Adding model 'Limitaciones'
        db.create_table('produccion_limitaciones', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('produccion', ['Limitaciones'])

        # Adding model 'PrincipalLimitacion'
        db.create_table('produccion_principallimitacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opcion1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='uno', to=orm['produccion.Limitaciones'])),
            ('opcion2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dos', to=orm['produccion.Limitaciones'])),
            ('opcion3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tres', to=orm['produccion.Limitaciones'])),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('produccion', ['PrincipalLimitacion'])

        # Adding model 'PatioCultivada'
        db.create_table('produccion_patiocultivada', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invierno', self.gf('django.db.models.fields.FloatField')()),
            ('verano', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('produccion', ['PatioCultivada'])

        # Adding model 'Arboles'
        db.create_table('produccion_arboles', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('patio', self.gf('django.db.models.fields.IntegerField')()),
            ('otra', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('produccion', ['Arboles'])

        # Adding model 'CalidadPatio'
        db.create_table('produccion_calidadpatio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('calidad', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('produccion', ['CalidadPatio'])

        # Adding model 'Ganado'
        db.create_table('produccion_ganado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('produccion', ['Ganado'])

        # Adding model 'GanadoMayor'
        db.create_table('produccion_ganadomayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ganado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion.Ganado'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('produccion', ['GanadoMayor'])


    def backwards(self, orm):
        
        # Deleting model 'CPeriodos'
        db.delete_table('produccion_cperiodos')

        # Deleting model 'CPermanentes'
        db.delete_table('produccion_cpermanentes')

        # Deleting model 'CAnuales'
        db.delete_table('produccion_canuales')

        # Deleting model 'CHortalizas'
        db.delete_table('produccion_chortalizas')

        # Deleting model 'CultivosPeriodos'
        db.delete_table('produccion_cultivosperiodos')

        # Deleting model 'CultivosPermanentes'
        db.delete_table('produccion_cultivospermanentes')

        # Deleting model 'CultivosAnuales'
        db.delete_table('produccion_cultivosanuales')

        # Deleting model 'Hortalizas'
        db.delete_table('produccion_hortalizas')

        # Deleting model 'ConsumoDiario'
        db.delete_table('produccion_consumodiario')

        # Deleting model 'Limitaciones'
        db.delete_table('produccion_limitaciones')

        # Deleting model 'PrincipalLimitacion'
        db.delete_table('produccion_principallimitacion')

        # Deleting model 'PatioCultivada'
        db.delete_table('produccion_patiocultivada')

        # Deleting model 'Arboles'
        db.delete_table('produccion_arboles')

        # Deleting model 'CalidadPatio'
        db.delete_table('produccion_calidadpatio')

        # Deleting model 'Ganado'
        db.delete_table('produccion_ganado')

        # Deleting model 'GanadoMayor'
        db.delete_table('produccion_ganadomayor')


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
        'produccion.arboles': {
            'Meta': {'object_name': 'Arboles'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otra': ('django.db.models.fields.IntegerField', [], {}),
            'patio': ('django.db.models.fields.IntegerField', [], {})
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
            'frijol': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maiz': ('django.db.models.fields.IntegerField', [], {})
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
            'apante': ('django.db.models.fields.IntegerField', [], {}),
            'cultivos': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['produccion.CPeriodos']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_apante': ('django.db.models.fields.IntegerField', [], {}),
            'p_postrera': ('django.db.models.fields.IntegerField', [], {}),
            'p_primera': ('django.db.models.fields.IntegerField', [], {}),
            'postrera': ('django.db.models.fields.IntegerField', [], {}),
            'primera': ('django.db.models.fields.IntegerField', [], {})
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
