# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Credito'
        db.create_table('crisis_alimentaria_credito', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('crisis_alimentaria', ['Credito'])

        # Deleting field 'AccesoCredito.mujer'
        db.delete_column('crisis_alimentaria_accesocredito', 'mujer')

        # Deleting field 'AccesoCredito.otro_hombre'
        db.delete_column('crisis_alimentaria_accesocredito', 'otro_hombre')

        # Deleting field 'AccesoCredito.hombre'
        db.delete_column('crisis_alimentaria_accesocredito', 'hombre')

        # Deleting field 'AccesoCredito.otra_mujer'
        db.delete_column('crisis_alimentaria_accesocredito', 'otra_mujer')

        # Adding M2M table for field hombre on 'AccesoCredito'
        db.create_table('crisis_alimentaria_accesocredito_hombre', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accesocredito', models.ForeignKey(orm['crisis_alimentaria.accesocredito'], null=False)),
            ('credito', models.ForeignKey(orm['crisis_alimentaria.credito'], null=False))
        ))
        db.create_unique('crisis_alimentaria_accesocredito_hombre', ['accesocredito_id', 'credito_id'])

        # Adding M2M table for field mujer on 'AccesoCredito'
        db.create_table('crisis_alimentaria_accesocredito_mujer', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accesocredito', models.ForeignKey(orm['crisis_alimentaria.accesocredito'], null=False)),
            ('credito', models.ForeignKey(orm['crisis_alimentaria.credito'], null=False))
        ))
        db.create_unique('crisis_alimentaria_accesocredito_mujer', ['accesocredito_id', 'credito_id'])

        # Adding M2M table for field otro_hombre on 'AccesoCredito'
        db.create_table('crisis_alimentaria_accesocredito_otro_hombre', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accesocredito', models.ForeignKey(orm['crisis_alimentaria.accesocredito'], null=False)),
            ('credito', models.ForeignKey(orm['crisis_alimentaria.credito'], null=False))
        ))
        db.create_unique('crisis_alimentaria_accesocredito_otro_hombre', ['accesocredito_id', 'credito_id'])

        # Adding M2M table for field otra_mujer on 'AccesoCredito'
        db.create_table('crisis_alimentaria_accesocredito_otra_mujer', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accesocredito', models.ForeignKey(orm['crisis_alimentaria.accesocredito'], null=False)),
            ('credito', models.ForeignKey(orm['crisis_alimentaria.credito'], null=False))
        ))
        db.create_unique('crisis_alimentaria_accesocredito_otra_mujer', ['accesocredito_id', 'credito_id'])


    def backwards(self, orm):
        
        # Deleting model 'Credito'
        db.delete_table('crisis_alimentaria_credito')

        # Adding field 'AccesoCredito.mujer'
        db.add_column('crisis_alimentaria_accesocredito', 'mujer', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Adding field 'AccesoCredito.otro_hombre'
        db.add_column('crisis_alimentaria_accesocredito', 'otro_hombre', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Adding field 'AccesoCredito.hombre'
        db.add_column('crisis_alimentaria_accesocredito', 'hombre', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Adding field 'AccesoCredito.otra_mujer'
        db.add_column('crisis_alimentaria_accesocredito', 'otra_mujer', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Removing M2M table for field hombre on 'AccesoCredito'
        db.delete_table('crisis_alimentaria_accesocredito_hombre')

        # Removing M2M table for field mujer on 'AccesoCredito'
        db.delete_table('crisis_alimentaria_accesocredito_mujer')

        # Removing M2M table for field otro_hombre on 'AccesoCredito'
        db.delete_table('crisis_alimentaria_accesocredito_otro_hombre')

        # Removing M2M table for field otra_mujer on 'AccesoCredito'
        db.delete_table('crisis_alimentaria_accesocredito_otra_mujer')


    models = {
        'crisis_alimentaria.accesocredito': {
            'Meta': {'object_name': 'AccesoCredito'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'hombre': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Hombre'", 'symmetrical': 'False', 'to': "orm['crisis_alimentaria.Credito']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mujer': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Mujer'", 'symmetrical': 'False', 'to': "orm['crisis_alimentaria.Credito']"}),
            'otra_mujer': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Mujer vive'", 'symmetrical': 'False', 'to': "orm['crisis_alimentaria.Credito']"}),
            'otro_hombre': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Hombre vive'", 'symmetrical': 'False', 'to': "orm['crisis_alimentaria.Credito']"})
        },
        'crisis_alimentaria.credito': {
            'Meta': {'object_name': 'Credito'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
        }
    }

    complete_apps = ['crisis_alimentaria']
