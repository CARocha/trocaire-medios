# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Inmigracion'
        db.create_table('calidad_vida_inmigracion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('inmigra', self.gf('django.db.models.fields.IntegerField')()),
            ('mujer', self.gf('django.db.models.fields.IntegerField')()),
            ('hombre', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('calidad_vida', ['Inmigracion'])

        # Adding model 'Codigo'
        db.create_table('calidad_vida_codigo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('calidad_vida', ['Codigo'])

        # Adding model 'AccesoEscuela'
        db.create_table('calidad_vida_accesoescuela', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('acceso', self.gf('django.db.models.fields.IntegerField')()),
            ('fem_estudia', self.gf('django.db.models.fields.related.ForeignKey')(related_name='estudia', to=orm['calidad_vida.Codigo'])),
            ('fem_no_estudia', self.gf('django.db.models.fields.related.ForeignKey')(related_name='no_estudia', to=orm['calidad_vida.Codigo'])),
            ('mas_estudia', self.gf('django.db.models.fields.related.ForeignKey')(related_name='masculino', to=orm['calidad_vida.Codigo'])),
            ('mas_no_estudia', self.gf('django.db.models.fields.related.ForeignKey')(related_name='no_masculino', to=orm['calidad_vida.Codigo'])),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('calidad_vida', ['AccesoEscuela'])

        # Adding model 'Abastece'
        db.create_table('calidad_vida_abastece', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('calidad_vida', ['Abastece'])

        # Adding model 'Agua'
        db.create_table('calidad_vida_agua', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sistema', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad_vida.Abastece'])),
            ('calidad', self.gf('django.db.models.fields.IntegerField')()),
            ('clorada', self.gf('django.db.models.fields.IntegerField')()),
            ('tiene', self.gf('django.db.models.fields.IntegerField')()),
            ('tiempo', self.gf('django.db.models.fields.IntegerField')()),
            ('techo', self.gf('django.db.models.fields.IntegerField')()),
            ('piso', self.gf('django.db.models.fields.IntegerField')()),
            ('paredes', self.gf('django.db.models.fields.IntegerField')()),
            ('servicio', self.gf('django.db.models.fields.IntegerField')()),
            ('cuartos', self.gf('django.db.models.fields.IntegerField')()),
            ('estado', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('calidad_vida', ['Agua'])


    def backwards(self, orm):
        
        # Deleting model 'Inmigracion'
        db.delete_table('calidad_vida_inmigracion')

        # Deleting model 'Codigo'
        db.delete_table('calidad_vida_codigo')

        # Deleting model 'AccesoEscuela'
        db.delete_table('calidad_vida_accesoescuela')

        # Deleting model 'Abastece'
        db.delete_table('calidad_vida_abastece')

        # Deleting model 'Agua'
        db.delete_table('calidad_vida_agua')


    models = {
        'calidad_vida.abastece': {
            'Meta': {'object_name': 'Abastece'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'calidad_vida.accesoescuela': {
            'Meta': {'object_name': 'AccesoEscuela'},
            'acceso': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'fem_estudia': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'estudia'", 'to': "orm['calidad_vida.Codigo']"}),
            'fem_no_estudia': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'no_estudia'", 'to': "orm['calidad_vida.Codigo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mas_estudia': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'masculino'", 'to': "orm['calidad_vida.Codigo']"}),
            'mas_no_estudia': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'no_masculino'", 'to': "orm['calidad_vida.Codigo']"})
        },
        'calidad_vida.agua': {
            'Meta': {'object_name': 'Agua'},
            'calidad': ('django.db.models.fields.IntegerField', [], {}),
            'clorada': ('django.db.models.fields.IntegerField', [], {}),
            'cuartos': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'estado': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paredes': ('django.db.models.fields.IntegerField', [], {}),
            'piso': ('django.db.models.fields.IntegerField', [], {}),
            'servicio': ('django.db.models.fields.IntegerField', [], {}),
            'sistema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['calidad_vida.Abastece']"}),
            'techo': ('django.db.models.fields.IntegerField', [], {}),
            'tiempo': ('django.db.models.fields.IntegerField', [], {}),
            'tiene': ('django.db.models.fields.IntegerField', [], {})
        },
        'calidad_vida.codigo': {
            'Meta': {'object_name': 'Codigo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'calidad_vida.inmigracion': {
            'Meta': {'object_name': 'Inmigracion'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'hombre': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inmigra': ('django.db.models.fields.IntegerField', [], {}),
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

    complete_apps = ['calidad_vida']
