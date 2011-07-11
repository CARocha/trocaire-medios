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

def produccion_por_rango(request, modelo, maximo=None, minimo=0, separaciones=10):
    #puntas = dicc con maximo y minimo
    encuestas = _query_set_filtrado(request)
    model = get_model('produccion', modelo)

    if encuestas:
        puntas_calc = model.objects.filter(encuesta__in = encuestas).aggregate(max_manzana = Max('manzana'), 
                min_manzana = Min('manzana'), max_produccion=Max('produccion'), min_produccion = Min('produccion'))
    else:
        puntas_calc = model.objects.all().aggregate(maximo = Max('total'), minimo = Min('total'))

    if maximo:
        maximo, minimo = int(maximo), int(minimo)
        puntas = dict(maximo=maximo, minimo=minimo)
    else:
        puntas = puntas_calc

    calculos = []
    calculos.append(__calculate_values(model, maximo, minimo, puntas, separaciones, 'produccion', encuestas))
    calculos.append(__calculate_values(model, maximo, minimo, puntas, separaciones, 'manzana', encuestas))

    form = ConsultarForm()
     
    return render_to_response('produccion/produccion_por_rango.html', 
                              {'form': form, 'calculos':calculos},
                              context_instance=RequestContext(request))

def __calculate_values(modelo, maximo, minimo, puntas, separaciones, campo, encuestas=None):
    SEPARACIONES = int(separaciones) if separaciones else 10
    rango = (puntas['max_' + campo]-puntas['min_' +campo])/ (SEPARACIONES)

    rangos = range(int(puntas['min_' + campo]), int(puntas['max_' + campo]), int(rango))
    parametros = zip(rangos, rangos[1:])
    parametros.append((rangos[len(rangos)-1], puntas['max_' + campo]))

    valores = []
    #categorias: para pintarlo en el eje X del grafo
    categorias = []

    for parametro in parametros:
        params = {'%s__gte' % campo: parametro[0], '%s__lt' % campo: parametro[1]}
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
