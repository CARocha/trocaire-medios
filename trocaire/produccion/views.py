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

def produccion_por_rango(request, modelo, dondetoy2, cultivos, maximo=None, minimo=0, separaciones=10, template_name='produccion/produccion_por_rango.html'):
    #puntas = dicc con maximo y minimo
    encuestas = _query_set_filtrado(request)
    model = get_model('produccion', modelo)

    if encuestas:
        puntas_calc = model.objects.filter(encuesta__in = encuestas, cultivos__in=cultivos).aggregate(max_manzana = Max('manzana'), 
                min_manzana = Min('manzana'), max_produccion=Max('produccion'), min_produccion = Min('produccion'))
    else:
        puntas_calc = model.objects.filter(cultivos__in = cultivos).aggregate(max_manzana = Max('manzana'), 
                min_manzana = Min('manzana'), max_produccion=Max('produccion'), min_produccion = Min('produccion'))

    if maximo:
        maximo, minimo = int(maximo), int(minimo)
        puntas = dict(max_produccion=maximo, min_produccion=minimo, max_manzana=maximo, min_manzana=minimo)
    else:
        puntas = puntas_calc

    calculos = []
    calculos.append(__calculate_values(model, maximo, minimo, puntas, separaciones, 'produccion', cultivos, encuestas))
    calculos.append(__calculate_values(model, maximo, minimo, puntas, separaciones, 'manzana', cultivos, encuestas))

    form = ConsultarForm()
     
    return render_to_response(template_name, 
                              {'form': form, 'calculos':calculos, 
                               'model': model._meta.verbose_name,
                               'dondetoy2': dondetoy2,
                               'model_name': model._meta.module_name, 
                               'request': request},
                              context_instance=RequestContext(request))

def __calculate_values(modelo, maximo, minimo, puntas, separaciones, campo, cultivos, encuestas=None):
    SEPARACIONES = int(separaciones) if separaciones else 10
    rango = (puntas['max_' + campo]-puntas['min_' +campo])/ (SEPARACIONES)

    rangos = range(int(puntas['min_' + campo]), int(puntas['max_' + campo]), int(rango))
    parametros = zip(rangos, rangos[1:])
    parametros.append((rangos[len(rangos)-1], puntas['max_' + campo]))

    valores = []
    #categorias: para pintarlo en el eje X del grafo
    categorias = []

    for parametro in parametros:
        params = {'%s__gte' % campo: parametro[0], '%s__lt' % campo: parametro[1], 'cultivos__in': cultivos}
        if encuestas:
            valores.append(modelo.objects.filter(encuesta__in = encuestas, **params).count())
        else:
            valores.append(modelo.objects.filter(**params).count())
        categorias.append('%.2f a %.2f' % parametro)
    maximo_a_evaluar = parametros[len(parametros)-1][1] + rango
    params = {'%s__gte' % campo: maximo_a_evaluar}
    if encuestas:
        valores.append(modelo.objects.filter(encuesta__in=encuestas, **params).count())
    else:
        valores.append(modelo.objects.filter(**params).count())

    valores_acumulados = lista_acumulada(valores)
    categorias.append('%.2f a mas' % maximo_a_evaluar)

    return dict(categorias = categorias, valores_acumulados = valores_acumulados,
               valores = valores)

def generic_range(request, model, field, title, dondetoy2, serie, subtitle, eje, extra_params, maximo=0, minimo=0, separaciones=10, template_name='produccion/generic_range_view.html'):
    #puntas = dicc con maximo y minimo
    encuestas = _query_set_filtrado(request)
    model = get_model('produccion', model)
    if encuestas:
        print "cerote", extra_params
        puntas_calc = model.objects.filter(encuesta__in = encuestas, **extra_params).aggregate(maximo = Max(field), minimo = Min(field))
    else:
        print "mierda"
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
        categorias.append('%.2f a %.2f' % parametro)
    
    maximo_a_evaluar = parametros[len(parametros)-1][1] + rango
    del extra_params["%s__lt" % field]
    extra_params["%s__gte" % field] =  maximo_a_evaluar 
    if encuestas:
        valores.append(model.objects.filter(encuesta__in=encuestas, **extra_params).count())
    else:
        valores.append(model.objects.filter(**extra_params).count())

    valores_acumulados = lista_acumulada(valores)
    categorias.append('%.2f a mas' % maximo_a_evaluar)

    form = ConsultarForm()
    #WTF de django
    del extra_params["%s__gte" % field]
    
    return render_to_response(template_name, 
                              {'valores': valores,
                               'categorias': categorias,
                               'form': form,
                               'title': title,
                               'subtitle': subtitle,
                               'eje': eje,
                               'serie': serie,
                               'dondetoy2': dondetoy2,
                               'valores_acumulados': valores_acumulados,
                               'request': request},
                              context_instance=RequestContext(request))
