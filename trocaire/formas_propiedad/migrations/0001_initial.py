# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Tierra'
        db.create_table('formas_propiedad_tierra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.IntegerField')()),
            ('mujer', self.gf('django.db.models.fields.IntegerField')()),
            ('hombre', self.gf('django.db.models.fields.IntegerField')()),
            ('ambos', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('formas_propiedad', ['Tierra'])

        # Adding model 'Ciclo'
        db.create_table('formas_propiedad_ciclo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('formas_propiedad', ['Ciclo'])

        # Adding model 'Riegos'
        db.create_table('formas_propiedad_riegos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('formas_propiedad', ['Riegos'])

        # Adding model 'Propiedad'
        db.create_table('formas_propiedad_propiedad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('conflicto', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('formas_propiedad', ['Propiedad'])

        # Adding M2M table for field ciclo on 'Propiedad'
        db.create_table('formas_propiedad_propiedad_ciclo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propiedad', models.ForeignKey(orm['formas_propiedad.propiedad'], null=False)),
            ('ciclo', models.ForeignKey(orm['formas_propiedad.ciclo'], null=False))
        ))
        db.create_unique('formas_propiedad_propiedad_ciclo', ['propiedad_id', 'ciclo_id'])

        # Adding M2M table for field zonas on 'Propiedad'
        db.create_table('formas_propiedad_propiedad_zonas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propiedad', models.ForeignKey(orm['formas_propiedad.propiedad'], null=False)),
            ('riegos', models.ForeignKey(orm['formas_propiedad.riegos'], null=False))
        ))
        db.create_unique('formas_propiedad_propiedad_zonas', ['propiedad_id', 'riegos_id'])


    def backwards(self, orm):
        
        # Deleting model 'Tierra'
        db.delete_table('formas_propiedad_tierra')

        # Deleting model 'Ciclo'
        db.delete_table('formas_propiedad_ciclo')

        # Deleting model 'Riegos'
        db.delete_table('formas_propiedad_riegos')

        # Deleting model 'Propiedad'
        db.delete_table('formas_propiedad_propiedad')

        # Removing M2M table for field ciclo on 'Propiedad'
        db.delete_table('formas_propiedad_propiedad_ciclo')

        # Removing M2M table for field zonas on 'Propiedad'
        db.delete_table('formas_propiedad_propiedad_zonas')


    models = {
        'formas_propiedad.ciclo': {
            'Meta': {'object_name': 'Ciclo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'formas_propiedad.propiedad': {
            'Meta': {'object_name': 'Propiedad'},
            'ciclo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['formas_propiedad.Ciclo']", 'symmetrical': 'False'}),
            'conflicto': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'zonas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['formas_propiedad.Riegos']", 'symmetrical': 'False'})
        },
        'formas_propiedad.riegos': {
            'Meta': {'object_name': 'Riegos'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'formas_propiedad.tierra': {
            'Meta': {'object_name': 'Tierra'},
            'ambos': ('django.db.models.fields.IntegerField', [], {}),
            'area': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'hombre': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mujer': ('django.db.models.fields.IntegerField', [], {})
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

    complete_apps = ['formas_propiedad']
