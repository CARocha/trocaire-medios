
#importaciones de Django
from datetime import date
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.utils import simplejson
from django.db.models import Sum, Count, Avg
from django.core.exceptions import ViewDoesNotExist

#importaciones de los models
from trocaire.calidad_vida.models import *
from trocaire.crisis_alimentaria.models import *
from trocaire.diversidad_alimentaria.models import *
from trocaire.familia.models import *
from trocaire.formas_propiedad.models import *
from trocaire.genero.models import * 
from trocaire.ingresos.models import *
from trocaire.lugar.models import *
from trocaire.medios.models import *
from trocaire.participacion_ciudadana.models import *
from trocaire.produccion.models import *
from trocaire.tecnologia.models import *


# Create your views here.

def index(request, template_name="index.html"):
               
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
                              
def ingresos(request):
    numero = Encuesta.objects.all().count()
    
    
    dicc = {}
    for opcion in choice_clasificacion:
        lista = []
        for fuente in Fuentes.objects.filter(clasificacion=opcion[0]):
            for principal in fuente.principalesfuentes_set.all():
                lista.append(principal.encuesta)
        cantidad = len(lista)
        dicc[opcion[1]] = cantidad
    suma = 0    
    for k, v in dicc.items():
        suma += v
    return render_to_response('encuestas/ingreso.html', locals(),
                              context_instance=RequestContext(request))



def sumas_de_ingresos(request):
    numero_encuestas = Encuesta.objects.all().count()
    c_peridos = []
    #esta es la vista de periodos
    periodo = CultivosIPeriodos.objects.all()
    total_primera = 0
    total_postrera = 0
    total_apante = 0
    gran_total = 0
    for a in CultivosIPeriodos.objects.all():
        primera = a.cuanto_primera * a.precio_primera
        total_primera += primera
        postrera = a.cuanto_postrera * a.precio_postrera
        total_postrera += postrera
        apante = a.cuanto_apante * a.precio_apante
        total_apante += apante
    gran_total = total_primera + total_postrera + total_apante
    #esta es la vista de permanente
    permanente = CultivosIPermanentes.objects.all()
    total_perma = 0
    for p in CultivosIPermanentes.objects.all():
        c_permanente = p.cuanto * p.precio
        total_perma += c_permanente
    
    #esta es la vista de estacionales
    estacional = CultivosIEstacionales.objects.all()
    total_esta = 0
    for e in CultivosIEstacionales.objects.all():
        c_estacional = e.cuanto * e.precio
        total_esta += c_estacional
    #esta es la vista de hortaliza
    hortaliza = IHortalizas.objects.all()
    total_horta = 0
    for h in IHortalizas.objects.all():
        i_hortaliza = h.cuanto * h.precio
        total_horta += i_hortaliza
    #esta es la vista de ingreso de patio
    patio = IngresoPatio.objects.all() 
    for ok in IngresoPatio.objects.all():
        invierno = Encuesta.objects.aggregate(invierno=Sum('ingresopatio__invierno'))['invierno']
        verano = Encuesta.objects.aggregate(verano=Sum('ingresopatio__verano'))['verano']
        total_patio = invierno + verano
    #esta es la vista de ganado
    ganado = IngresoGanado.objects.all()
    total_ganado = 0
    for g in IngresoGanado.objects.all():
        i_ganado = g.vendidos * g.valor
        total_ganado += i_ganado
    #esta es la vista de lactios
    lactio = Lactios.objects.all()
    total_invierno = 0
    total_verano = 0
    total_lactio = 0
    for l in Lactios.objects.all():
        invierno = l.cantidad_invi * l.invierno_precio
        total_invierno += invierno
        verano = l.cantidad_vera * l.verano_precio
        total_verano += verano
        total_lactio = total_invierno + total_verano
    #esta es la vista de productos procesados
    producto = ProductosProcesado.objects.all()
    for b in ProductosProcesado.objects.all():
        total_procesado = Encuesta.objects.aggregate(total_procesado=Sum('productosprocesado__monto'))['total_procesado']
    #esta es la vista de otros ingresos
    ingreso = OtrosIngresos.objects.all()
    for y in OtrosIngresos.objects.all():
        t_otros = Encuesta.objects.aggregate(t_mayo=Sum('otrosingresos__mayo'),
                                            t_junio=Sum('otrosingresos__junio'),
                                            t_julio=Sum('otrosingresos__julio'),
                                            t_agosto=Sum('otrosingresos__agosto'),
                                            t_septiembre=Sum('otrosingresos__septiembre'),
                                            t_octubre=Sum('otrosingresos__octubre'),
                                            t_noviembre=Sum('otrosingresos__noviembre'),
                                            t_diciembre=Sum('otrosingresos__diciembre'),
                                            t_enero=Sum('otrosingresos__enero'),
                                            t_febrero=Sum('otrosingresos__febrero'),
                                            t_marzo=Sum('otrosingresos__marzo'),
                                            t_abril=Sum('otrosingresos__abril'))
    total_otros = 0
    for k, v in t_otros.items():
        total_otros += v
    # sumas de todos los totales  de todas las tablas de los ingresos
    grandisimo_total = gran_total + total_perma + total_esta + total_horta + total_patio + total_ganado +  total_lactio + total_procesado + total_otros
    promedio = round((grandisimo_total / numero_encuestas),2)  
        
#    for periodo in CIPeriodos.objects.all():
#        c_primera = Encuesta.objects.filter(cultivosiperiodos__cultivo = periodo).aggregate(c_primera=Sum('cultivosiperiodos__cuanto_primera'))['c_primera']
#        precio_primera = Encuesta.objects.filter(cultivosiperiodos__cultivo = periodo).aggregate(precio_primera=Sum('cultivosiperiodos__precio_primera'))['precio_primera']
#        
#        c_postrera = Encuesta.objects.filter(cultivosiperiodos__cultivo = periodo).aggregate(c_postrera=Sum('cultivosiperiodos__cuanto_postrera'))['c_postrera']
#        precio_postrera = Encuesta.objects.filter(cultivosiperiodos__cultivo = periodo).aggregate(precio_postrera=Sum('cultivosiperiodos__precio_postrera'))['precio_postrera']
#        
#        c_apante = Encuesta.objects.filter(cultivosiperiodos__cultivo = periodo).aggregate(c_apante=Sum('cultivosiperiodos__cuanto_apante'))['c_apante']
#        precio_apante = Encuesta.objects.filter(cultivosiperiodos__cultivo = periodo).aggregate(precio_apante=Sum('cultivosiperiodos__precio_apante'))['precio_apante']

#        total_primera = c_primera * precio_primera
#        total_postrera = c_postrera * precio_postrera
#        total_apante = c_apante * precio_apante
#        
#        c_peridos.append([total_primera,total_postrera,total_apante])
    
    return render_to_response('encuestas/total_ingreso.html', locals(),
                               context_instance=RequestContext(request))
 
#FUNCIONES PARA LAS URL
def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not define in VALID_VIEWS." % (vista, 'encuesta.views'))

VALID_VIEWS = {
    'ingreso': ingresos,
    'total': sumas_de_ingresos,
    
    
    
    }

#FUNCIONES UTILITARIAS PARA TODO EL SITIO                              
def saca_porcentajes(values):
    """sumamos los valores y devolvemos una lista con su porcentaje"""
    total = sum(values)
    valores_cero = [] #lista para anotar los indices en los que da cero el porcentaje
    for i in range(len(values)):
        porcentaje = (float(values[i])/total)*100
        values[i] = "%.2f" % porcentaje + '%' 
    return values

def saca_porcentajes(dato, total, formato=True):
    '''Si formato es true devuelve float caso contrario es cadena'''
    if dato != None:
        try:
            porcentaje = (dato/float(total)) * 100 if total != None or total != 0 else 0
        except:
            return 0
        if formato:
            return porcentaje
        else:
            return '%.2f' % porcentaje
    else: 
        return 0
    
    
