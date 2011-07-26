from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.utils import simplejson
from django.db.models import Sum, Count, Avg, Max, Min, get_model

from medios.forms import ConsultarForm
from medios.views import _query_set_filtrado
from models import *

lista_acumulada = lambda valores: [sum(valores[:i]) for i in range(1, len(valores)+1)]

def generic_range(request, model, field, extra_params, maximo=None, minimo=0, separaciones=10, template_name='produccion/generic_range_view.html'):
    #puntas = dicc con maximo y minimo
    encuestas = _query_set_filtrado(request)
    model = get_model('formas_propiedad', model)
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
    
    return render_to_response(template_name, 
                              {'valores': valores,
                               'categorias': categorias,
                               'form': form,
                               'valores_acumulados': valores_acumulados},
                              context_instance=RequestContext(request))
