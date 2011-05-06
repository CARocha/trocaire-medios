# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Fuentes'
        db.create_table('ingresos_fuentes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('clasificacion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('ingresos', ['Fuentes'])

        # Adding model 'PrincipalesFuentes'
        db.create_table('ingresos_principalesfuentes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('ingresos', ['PrincipalesFuentes'])

        # Adding M2M table for field fuente on 'PrincipalesFuentes'
        db.create_table('ingresos_principalesfuentes_fuente', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('principalesfuentes', models.ForeignKey(orm['ingresos.principalesfuentes'], null=False)),
            ('fuentes', models.ForeignKey(orm['ingresos.fuentes'], null=False))
        ))
        db.create_unique('ingresos_principalesfuentes_fuente', ['principalesfuentes_id', 'fuentes_id'])

        # Adding model 'CIPeriodos'
        db.create_table('ingresos_ciperiodos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('ingresos', ['CIPeriodos'])

        # Adding model 'CIPermanentes'
        db.create_table('ingresos_cipermanentes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('ingresos', ['CIPermanentes'])

        # Adding model 'CIEstacionales'
        db.create_table('ingresos_ciestacionales', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('ingresos', ['CIEstacionales'])

        # Adding model 'CIHortalizas'
        db.create_table('ingresos_cihortalizas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('ingresos', ['CIHortalizas'])

        # Adding model 'CultivosIPeriodos'
        db.create_table('ingresos_cultivosiperiodos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cultivo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ingresos.CIPeriodos'])),
            ('cuanto_primera', self.gf('django.db.models.fields.FloatField')()),
            ('cuanto_postrera', self.gf('django.db.models.fields.FloatField')()),
            ('cuanto_apante', self.gf('django.db.models.fields.FloatField')()),
            ('precio_primera', self.gf('django.db.models.fields.FloatField')()),
            ('precio_postrera', self.gf('django.db.models.fields.FloatField')()),
            ('precio_apante', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('ingresos', ['CultivosIPeriodos'])

        # Adding model 'CultivosIPermanentes'
        db.create_table('ingresos_cultivosipermanentes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cultivo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ingresos.CIPermanentes'])),
            ('cuanto', self.gf('django.db.models.fields.FloatField')()),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('ingresos', ['CultivosIPermanentes'])

        # Adding model 'CultivosIEstacionales'
        db.create_table('ingresos_cultivosiestacionales', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cultivo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ingresos.CIEstacionales'])),
            ('cuanto', self.gf('django.db.models.fields.FloatField')()),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('ingresos', ['CultivosIEstacionales'])

        # Adding model 'IHortalizas'
        db.create_table('ingresos_ihortalizas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hortaliza', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ingresos.CIHortalizas'])),
            ('cuanto', self.gf('django.db.models.fields.FloatField')()),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
            ('equivalencias', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('ingresos', ['IHortalizas'])

        # Adding model 'IngresoPatio'
        db.create_table('ingresos_ingresopatio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invierno', self.gf('django.db.models.fields.FloatField')()),
            ('verano', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('ingresos', ['IngresoPatio'])

        # Adding model 'Ganados'
        db.create_table('ingresos_ganados', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('ingresos', ['Ganados'])

        # Adding model 'IngresoGanado'
        db.create_table('ingresos_ingresoganado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ganado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ingresos.Ganados'])),
            ('vendidos', self.gf('django.db.models.fields.IntegerField')()),
            ('valor', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('ingresos', ['IngresoGanado'])

        # Adding model 'Productos'
        db.create_table('ingresos_productos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('ingresos', ['Productos'])

        # Adding model 'Lactios'
        db.create_table('ingresos_lactios', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ingresos.Productos'])),
            ('invierno_precio', self.gf('django.db.models.fields.FloatField')()),
            ('verano_precio', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('ingresos', ['Lactios'])

        # Adding model 'PProcesado'
        db.create_table('ingresos_pprocesado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('ingresos', ['PProcesado'])

        # Adding model 'ProductosProcesado'
        db.create_table('ingresos_productosprocesado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ingresos.PProcesado'])),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
            ('monto', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('ingresos', ['ProductosProcesado'])

        # Adding model 'OtrasActividades'
        db.create_table('ingresos_otrasactividades', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('ingresos', ['OtrasActividades'])

        # Adding model 'OtrosIngresos'
        db.create_table('ingresos_otrosingresos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actividad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ingresos.OtrasActividades'])),
            ('mayo', self.gf('django.db.models.fields.FloatField')()),
            ('junio', self.gf('django.db.models.fields.FloatField')()),
            ('julio', self.gf('django.db.models.fields.FloatField')()),
            ('agosto', self.gf('django.db.models.fields.FloatField')()),
            ('septiembre', self.gf('django.db.models.fields.FloatField')()),
            ('octubre', self.gf('django.db.models.fields.FloatField')()),
            ('noviembre', self.gf('django.db.models.fields.FloatField')()),
            ('diciembre', self.gf('django.db.models.fields.FloatField')()),
            ('enero', self.gf('django.db.models.fields.FloatField')()),
            ('febrero', self.gf('django.db.models.fields.FloatField')()),
            ('marzo', self.gf('django.db.models.fields.FloatField')()),
            ('abril', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('ingresos', ['OtrosIngresos'])

        # Adding model 'PrincipalForma'
        db.create_table('ingresos_principalforma', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('principal', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('ingresos', ['PrincipalForma'])

        # Adding model 'ProductosPrincipales'
        db.create_table('ingresos_productosprincipales', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('ingresos', ['ProductosPrincipales'])

        # Adding model 'VendeProducto'
        db.create_table('ingresos_vendeproducto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('principal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ingresos.ProductosPrincipales'])),
            ('forma', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('ingresos', ['VendeProducto'])


    def backwards(self, orm):
        
        # Deleting model 'Fuentes'
        db.delete_table('ingresos_fuentes')

        # Deleting model 'PrincipalesFuentes'
        db.delete_table('ingresos_principalesfuentes')

        # Removing M2M table for field fuente on 'PrincipalesFuentes'
        db.delete_table('ingresos_principalesfuentes_fuente')

        # Deleting model 'CIPeriodos'
        db.delete_table('ingresos_ciperiodos')

        # Deleting model 'CIPermanentes'
        db.delete_table('ingresos_cipermanentes')

        # Deleting model 'CIEstacionales'
        db.delete_table('ingresos_ciestacionales')

        # Deleting model 'CIHortalizas'
        db.delete_table('ingresos_cihortalizas')

        # Deleting model 'CultivosIPeriodos'
        db.delete_table('ingresos_cultivosiperiodos')

        # Deleting model 'CultivosIPermanentes'
        db.delete_table('ingresos_cultivosipermanentes')

        # Deleting model 'CultivosIEstacionales'
        db.delete_table('ingresos_cultivosiestacionales')

        # Deleting model 'IHortalizas'
        db.delete_table('ingresos_ihortalizas')

        # Deleting model 'IngresoPatio'
        db.delete_table('ingresos_ingresopatio')

        # Deleting model 'Ganados'
        db.delete_table('ingresos_ganados')

        # Deleting model 'IngresoGanado'
        db.delete_table('ingresos_ingresoganado')

        # Deleting model 'Productos'
        db.delete_table('ingresos_productos')

        # Deleting model 'Lactios'
        db.delete_table('ingresos_lactios')

        # Deleting model 'PProcesado'
        db.delete_table('ingresos_pprocesado')

        # Deleting model 'ProductosProcesado'
        db.delete_table('ingresos_productosprocesado')

        # Deleting model 'OtrasActividades'
        db.delete_table('ingresos_otrasactividades')

        # Deleting model 'OtrosIngresos'
        db.delete_table('ingresos_otrosingresos')

        # Deleting model 'PrincipalForma'
        db.delete_table('ingresos_principalforma')

        # Deleting model 'ProductosPrincipales'
        db.delete_table('ingresos_productosprincipales')

        # Deleting model 'VendeProducto'
        db.delete_table('ingresos_vendeproducto')


    models = {
        'ingresos.ciestacionales': {
            'Meta': {'object_name': 'CIEstacionales'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'ingresos.cihortalizas': {
            'Meta': {'object_name': 'CIHortalizas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'ingresos.ciperiodos': {
            'Meta': {'object_name': 'CIPeriodos'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'ingresos.cipermanentes': {
            'Meta': {'object_name': 'CIPermanentes'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'ingresos.cultivosiestacionales': {
            'Meta': {'object_name': 'CultivosIEstacionales'},
            'cuanto': ('django.db.models.fields.FloatField', [], {}),
            'cultivo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ingresos.CIEstacionales']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.FloatField', [], {})
        },
        'ingresos.cultivosiperiodos': {
            'Meta': {'object_name': 'CultivosIPeriodos'},
            'cuanto_apante': ('django.db.models.fields.FloatField', [], {}),
            'cuanto_postrera': ('django.db.models.fields.FloatField', [], {}),
            'cuanto_primera': ('django.db.models.fields.FloatField', [], {}),
            'cultivo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ingresos.CIPeriodos']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio_apante': ('django.db.models.fields.FloatField', [], {}),
            'precio_postrera': ('django.db.models.fields.FloatField', [], {}),
            'precio_primera': ('django.db.models.fields.FloatField', [], {})
        },
        'ingresos.cultivosipermanentes': {
            'Meta': {'object_name': 'CultivosIPermanentes'},
            'cuanto': ('django.db.models.fields.FloatField', [], {}),
            'cultivo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ingresos.CIPermanentes']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.FloatField', [], {})
        },
        'ingresos.fuentes': {
            'Meta': {'object_name': 'Fuentes'},
            'clasificacion': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'ingresos.ganados': {
            'Meta': {'object_name': 'Ganados'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'ingresos.ihortalizas': {
            'Meta': {'object_name': 'IHortalizas'},
            'cuanto': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'equivalencias': ('django.db.models.fields.FloatField', [], {}),
            'hortaliza': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ingresos.CIHortalizas']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.FloatField', [], {})
        },
        'ingresos.ingresoganado': {
            'Meta': {'object_name': 'IngresoGanado'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'ganado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ingresos.Ganados']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valor': ('django.db.models.fields.FloatField', [], {}),
            'vendidos': ('django.db.models.fields.IntegerField', [], {})
        },
        'ingresos.ingresopatio': {
            'Meta': {'object_name': 'IngresoPatio'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invierno': ('django.db.models.fields.FloatField', [], {}),
            'verano': ('django.db.models.fields.FloatField', [], {})
        },
        'ingresos.lactios': {
            'Meta': {'object_name': 'Lactios'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invierno_precio': ('django.db.models.fields.FloatField', [], {}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ingresos.Productos']"}),
            'verano_precio': ('django.db.models.fields.FloatField', [], {})
        },
        'ingresos.otrasactividades': {
            'Meta': {'object_name': 'OtrasActividades'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'ingresos.otrosingresos': {
            'Meta': {'object_name': 'OtrosIngresos'},
            'abril': ('django.db.models.fields.FloatField', [], {}),
            'actividad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ingresos.OtrasActividades']"}),
            'agosto': ('django.db.models.fields.FloatField', [], {}),
            'diciembre': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'enero': ('django.db.models.fields.FloatField', [], {}),
            'febrero': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'julio': ('django.db.models.fields.FloatField', [], {}),
            'junio': ('django.db.models.fields.FloatField', [], {}),
            'marzo': ('django.db.models.fields.FloatField', [], {}),
            'mayo': ('django.db.models.fields.FloatField', [], {}),
            'noviembre': ('django.db.models.fields.FloatField', [], {}),
            'octubre': ('django.db.models.fields.FloatField', [], {}),
            'septiembre': ('django.db.models.fields.FloatField', [], {})
        },
        'ingresos.pprocesado': {
            'Meta': {'object_name': 'PProcesado'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'ingresos.principalesfuentes': {
            'Meta': {'object_name': 'PrincipalesFuentes'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'fuente': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ingresos.Fuentes']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'ingresos.principalforma': {
            'Meta': {'object_name': 'PrincipalForma'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'principal': ('django.db.models.fields.IntegerField', [], {})
        },
        'ingresos.productos': {
            'Meta': {'object_name': 'Productos'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'ingresos.productosprincipales': {
            'Meta': {'object_name': 'ProductosPrincipales'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'ingresos.productosprocesado': {
            'Meta': {'object_name': 'ProductosProcesado'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.FloatField', [], {}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ingresos.PProcesado']"})
        },
        'ingresos.vendeproducto': {
            'Meta': {'object_name': 'VendeProducto'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'forma': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'principal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ingresos.ProductosPrincipales']"})
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

    complete_apps = ['ingresos']
