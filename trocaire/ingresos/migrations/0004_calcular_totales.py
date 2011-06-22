# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        #haciendo los calculos pertinentes
        print 'migrando Ingreso Patio'
        for algo in orm.IngresoPatio.objects.all():
            algo.total = algo.invierno * algo.verano
            algo.save()

        print 'migrando Ingreso Ganado'
        for algo in orm.IngresoGanado.objects.all():
            algo.total = algo.vendidos * algo.valor
            algo.save()

        print 'migrando Ingreso Hortalizas'
        for algo in orm.IHortalizas.objects.all():
            algo.total = algo.cuanto * algo.precio
            algo.save()

        print 'migrando Cultivos IEstacionas'
        for algo in orm.CultivosIEstacionales.objects.all():
            algo.total = algo.cuanto * algo.precio
            algo.save()

        print 'migrando Lactios'
        for algo in orm.Lactios.objects.all():
            algo.total_invierno = algo.cantidad_invi * algo.invierno_precio
            algo.total_verano = algo.cantidad_vera * algo.verano_precio
            algo.total = algo.total_invierno + algo.total_verano
            algo.save()

        print 'migrando CultivosPermanentes'
        for algo in orm.CultivosIPermanentes.objects.all():
            algo.total = algo.cuanto * algo.precio
            algo.save()

        print 'migrando Otros Ingresos'
        for algo in orm.OtrosIngresos.objects.all():
            try:
                algo.total = algo.mayo + algo.junio + algo.julio + algo.agosto +\
                        algo.septiembre + algo.octubre + algo.noviembre +\
                        algo.diciembre + algo.enero + algo.febrero + algo.marzo +\
                        algo.abril
            except:
                print "hacer esta manual", algo.id
            algo.save()

        print 'migrando Cultivos Periodos'
        for algo in orm.CultivosIPeriodos.objects.all():
            algo.total_primera = algo.cuanto_primera * algo.precio_primera
            algo.total_postrera = algo.cuanto_postrera * algo.precio_postrera
            algo.total_apante = algo.cuanto_apante * algo.precio_apante
            algo.total = algo.total_primera + algo.total_postrera + algo.total_apante
            algo.save()

    def backwards(self, orm):
        "Write your backwards methods here."
        pass

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {})
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
            'precio_primera': ('django.db.models.fields.FloatField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {}),
            'total_apante': ('django.db.models.fields.FloatField', [], {}),
            'total_postrera': ('django.db.models.fields.FloatField', [], {}),
            'total_primera': ('django.db.models.fields.FloatField', [], {})
        },
        'ingresos.cultivosipermanentes': {
            'Meta': {'object_name': 'CultivosIPermanentes'},
            'cuanto': ('django.db.models.fields.FloatField', [], {}),
            'cultivo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ingresos.CIPermanentes']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {})
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
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {})
        },
        'ingresos.ingresoganado': {
            'Meta': {'object_name': 'IngresoGanado'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'ganado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ingresos.Ganados']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total': ('django.db.models.fields.FloatField', [], {}),
            'valor': ('django.db.models.fields.FloatField', [], {}),
            'vendidos': ('django.db.models.fields.IntegerField', [], {})
        },
        'ingresos.ingresopatio': {
            'Meta': {'object_name': 'IngresoPatio'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invierno': ('django.db.models.fields.FloatField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {}),
            'verano': ('django.db.models.fields.FloatField', [], {})
        },
        'ingresos.lactios': {
            'Meta': {'object_name': 'Lactios'},
            'cantidad_invi': ('django.db.models.fields.FloatField', [], {}),
            'cantidad_vera': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invierno_precio': ('django.db.models.fields.FloatField', [], {}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ingresos.Productos']"}),
            'total': ('django.db.models.fields.FloatField', [], {}),
            'total_invierno': ('django.db.models.fields.FloatField', [], {}),
            'total_verano': ('django.db.models.fields.FloatField', [], {}),
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
            'septiembre': ('django.db.models.fields.FloatField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {})
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
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'medios.recolector': {
            'Meta': {'object_name': 'Recolector'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['ingresos']
