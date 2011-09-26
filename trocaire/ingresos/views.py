# -*- coding: utf-8 -*-
from datetime import date
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.utils import simplejson
from django.db.models import Sum, Count, Avg, Max, Min, get_model
from django.core.exceptions import ViewDoesNotExist

from medios.forms import ConsultarForm
from medios.views import _query_set_filtrado
from models import *

lista_acumulada = lambda valores: [sum(valores[:i]) for i in range(1, len(valores)+1)]

def ingresos(request):
    numero = Encuesta.objects.all().count()
    
    dicc = {}
    for opcion in CHOICE_CLASIFICACION:
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
    
    return render_to_response('ingresos/sumas_de_ingresos.html', locals(),
                               context_instance=RequestContext(request))

def generic_range(request, model, field, title, serie, dondetoy2, subtitle, eje, extra_params={}, maximo=None, minimo=0, separaciones=10, template_name='ingresos/generic_range_view.html'):
    #puntas = dicc con maximo y minimo
    encuestas = _query_set_filtrado(request)
    model = get_model('ingresos', model)
    if encuestas:
        puntas_calc = model.objects.filter(encuesta__in = encuestas, **extra_params).aggregate(maximo = Max(field), minimo = Min(field))
    else:
        puntas_calc = model.objects.filter(**extra_params).aggregate(maximo = Max(field), minimo = Min(field))
    if maximo:
        maximo, minimo = int(maximo), int(minimo)
        puntas = dict(maximo=maximo, minimo=minimo)
    else:
        puntas = puntas_calc

    SEPARACIONES = int(separaciones) if separaciones else 10
    rango = (puntas['maximo']-puntas['minimo'])/ (SEPARACIONES)
    
    rangos = range(int(puntas['minimo']), int(puntas['maximo']), int(rango))
    parametros = zip(rangos, rangos[1:])
    parametros.append((rangos[len(rangos)-1], puntas['maximo']))

    valores = []
    #categorias: para pintarlo en el eje X del grafo
    categorias = []
    
    for parametro in parametros:
        extra_params["%s__gte" % field] = parametro[0]
        extra_params["%s__lt" % field] = parametro[1]
        if encuestas:
            valores.append(model.objects.filter(encuesta__in=encuestas, **extra_params).count())
        else:
            valores.append(model.objects.filter(**extra_params).count())
        categorias.append('%.0f a %.0f' % parametro)
    
    maximo_a_evaluar = parametros[len(parametros)-1][1] + rango
    del extra_params["%s__lt" % field]
    extra_params["%s__gte" % field] =  maximo_a_evaluar 
    if encuestas:
        valores.append(model.objects.filter(encuesta__in=encuestas, **extra_params).count())
    else:
        valores.append(model.objects.filter(**extra_params).count())

    valores_acumulados = lista_acumulada(valores)
    categorias.append('%.0f a mas' % maximo_a_evaluar)

    form = ConsultarForm()
    #WTF de django
    del extra_params["%s__gte" % field]
    
    return render_to_response(template_name, 
                              {'valores': valores,
                               'categorias': categorias,
                               'form': form,
                               'dondetoy2':dondetoy2,
                               'title': title,
                               'subtitle': subtitle,
                               'eje': eje,
                               'serie': serie,
                               'valores_acumulados': valores_acumulados,
                               'request': request},
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
