# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'EstrategiaCrisis'
        db.create_table('crisis_alimentaria_estrategiacrisis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('crisis_alimentaria', ['EstrategiaCrisis'])

        # Adding model 'Crisis'
        db.create_table('crisis_alimentaria_crisis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('escases', self.gf('django.db.models.fields.IntegerField')()),
            ('causa', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('crisis_alimentaria', ['Crisis'])

        # Adding M2M table for field enfrentar on 'Crisis'
        db.create_table('crisis_alimentaria_crisis_enfrentar', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('crisis', models.ForeignKey(orm['crisis_alimentaria.crisis'], null=False)),
            ('estrategiacrisis', models.ForeignKey(orm['crisis_alimentaria.estrategiacrisis'], null=False))
        ))
        db.create_unique('crisis_alimentaria_crisis_enfrentar', ['crisis_id', 'estrategiacrisis_id'])

        # Adding model 'AccesoCredito'
        db.create_table('crisis_alimentaria_accesocredito', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hombre', self.gf('django.db.models.fields.IntegerField')()),
            ('mujer', self.gf('django.db.models.fields.IntegerField')()),
            ('otro_hombre', self.gf('django.db.models.fields.IntegerField')()),
            ('otra_mujer', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('crisis_alimentaria', ['AccesoCredito'])


    def backwards(self, orm):
        
        # Deleting model 'EstrategiaCrisis'
        db.delete_table('crisis_alimentaria_estrategiacrisis')

        # Deleting model 'Crisis'
        db.delete_table('crisis_alimentaria_crisis')

        # Removing M2M table for field enfrentar on 'Crisis'
        db.delete_table('crisis_alimentaria_crisis_enfrentar')

        # Deleting model 'AccesoCredito'
        db.delete_table('crisis_alimentaria_accesocredito')


    models = {
        'crisis_alimentaria.accesocredito': {
            'Meta': {'object_name': 'AccesoCredito'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'hombre': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mujer': ('django.db.models.fields.IntegerField', [], {}),
            'otra_mujer': ('django.db.models.fields.IntegerField', [], {}),
            'otro_hombre': ('django.db.models.fields.IntegerField', [], {})
        },
        'crisis_alimentaria.crisis': {
            'Meta': {'object_name': 'Crisis'},
            'causa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'enfrentar': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['crisis_alimentaria.EstrategiaCrisis']", 'symmetrical': 'False'}),
            'escases': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'crisis_alimentaria.estrategiacrisis': {
            'Meta': {'object_name': 'EstrategiaCrisis'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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

    complete_apps = ['crisis_alimentaria']
