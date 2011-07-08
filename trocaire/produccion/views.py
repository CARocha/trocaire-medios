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

def produccion_por_rango(request, maximo=None, minimo=0, separaciones=10, modelo=None):
    #puntas = dicc con maximo y minimo
    encuestas = _query_set_filtrado(request)
    if encuestas:
        puntas_calc = TotalIngreso.objects.filter(encuesta__in = encuestas).aggregate(maximo = Max('total'), minimo = Min('total'))
    else:
        puntas_calc = TotalIngreso.objects.all().aggregate(maximo = Max('total'), minimo = Min('total'))
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
        if encuestas:
            valores.append(TotalIngreso.objects.filter(total__gte=parametro[0], total__lt=parametro[1], encuesta__in=encuestas).count())
        else:
            valores.append(TotalIngreso.objects.filter(total__gte=parametro[0], total__lt=parametro[1]).count())
        categorias.append('%.2f a %.2f' % parametro)
    
    maximo_a_evaluar = parametros[len(parametros)-1][1] + rango
    if encuestas:
        valores.append(TotalIngreso.objects.filter(total__gte=maximo_a_evaluar, encuesta__in=encuestas).count())
    else:
        valores.append(TotalIngreso.objects.filter(total__gte=maximo_a_evaluar).count())

    valores_acumulados = lista_acumulada(valores)
    categorias.append('%.2f a mas' % maximo_a_evaluar)

    form = ConsultarForm()
    
    return render_to_response('produccion/produccion_por_rango.html', 
                              {'valores': valores,
                               'categorias': categorias,
                               'form': form,
                               'valores_acumulados': valores_acumulados},
                              context_instance=RequestContext(request))


