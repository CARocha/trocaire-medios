# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import get_model
from django.utils import simplejson

#importaciones de los models
from forms import ConsultarForm
from trocaire.medios.models import *
from trocaire.familia.models import *
from trocaire.lugar.models import *

def _query_set_filtrado(request):
    #anio = int(request.session['fecha'])
    params = {}
    #if 'fecha' in request.session:
    #    params['fecha__year'] = anio
        
    if 'contraparte' in request.session:
        params['contraparte'] =  request.session['contraparte'] 

        if 'departamento' in request.session:
            if 'municipio' in request.session:
                if 'comarca' in request.session:
                    params['comarca'] = request.session['comarca']
                else:
                    params['comarca__municipio'] = request.session['municipio']
            else:
                params['comarca__municipio__departamento'] = request.session['departamento']
            
        unvalid_keys = []
        for key in params:
            if not params[key]:
                unvalid_keys.append(key)
        
        for key in unvalid_keys:
            del params[key]
        #despelote
        encuestas_id = []
        reducir = False
        last_key = (None, None)
        for i, key in enumerate(request.session['parametros']):
            #TODO: REVISAR ESTO
            for k, v in request.session['parametros'][key].items():
                if v is None or str(v) == 'None':
                    del request.session['parametros'][key][k]
            model = get_model(*key.split('.'))
            if len(request.session['parametros'][key]):
                reducir = True if (last_key[1] != key > 1 and last_key[0] == None) or reducir==True else False
                last_key = (i, key)
                ids = model.objects.filter(**request.session['parametros'][key]).values_list('id', flat=True)
                encuestas_id += ids
        if not encuestas_id:
            return Encuesta.objects.filter(**params)
        else:
            ids_definitivos = reducir_lista(encuestas_id) if reducir else encuestas_id
            return Encuesta.objects.filter(id__in = ids_definitivos, **params)

#===============================================================================
def consultar(request):
    if request.method == 'POST':
        form = ConsultarForm(request.POST)
        if form.is_valid():
            #request.session['fecha'] = form.cleaned_data['fecha']
            request.session['departamento'] = form.cleaned_data['departamento']
            request.session['contraparte'] = form.cleaned_data['contraparte']
            try:
                municipio = Municipio.objects.get(id=form.cleaned_data['municipio']) 
            except:
                municipio = None
            try:
                comarca = Comarca.objects.get(id=form.cleaned_data['comarca'])
            except:
                comarca = None

            request.session['municipio'] = municipio
            request.session['comarca'] = comarca

            #cosas de otros modelos!
            parametros = {'familia.escolaridad': {}, 'familia.composicion': {}, 
                          'genero.tomadecicion': {}, 'ingresos.principalesfuentes': {},
                          'ingresos.totalingreso': {}}
            parametros['familia.escolaridad']['beneficia'] = form.cleaned_data['escolaridad_beneficiario']
            parametros['familia.escolaridad']['conyugue'] = form.cleaned_data['escolaridad_conyugue']
            parametros['familia.composicion']['sexo'] = form.cleaned_data['familia_beneficiario']
            #desicion gasto mayor!
            #parametros['genero.tomadecicion']['aspectos'] = 1
            parametros['genero.tomadecicion']['respuesta'] =  form.cleaned_data['desicion_gasto_mayor']
            #ingresos
            parametros['ingresos.principalesfuentes']['fuente'] = form.cleaned_data['ingresos_fuente']#TODO: cambiarlo a fuente__in
            parametros['ingresos.totalingreso']['total__gte'] = form.cleaned_data['ingresos_total_min']
            parametros['ingresos.totalingreso']['total__lte'] = form.cleaned_data['ingresos_total_max']
            #parametros['formas_propiedad.finca']['area'] = forms.cleaned_data['finca_area_total']
            #parametros['produccion.ganadomayor']['num_vacas'] = forms.cleaned_data['finca_num_vacas']
            #parametros['finca']['conssa'] = forms.cleaned_data['finca_conssa']
            #parametros['finca']['num_productos'] = forms.cleaned_data['finca_num']
            request.session['parametros'] = parametros

            if form.cleaned_data['next_url']:
                return HttpResponseRedirect(form.cleaned_data['next_url'])
            else:
                return HttpResponseRedirect('/encuestas/generales/')
    else:
        form = ConsultarForm()
    return render_to_response('encuestas/consultar.html', locals(),
                              context_instance=RequestContext(request))

#===============================================================================

def index(request, template_name="index.html"):
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

#FUNCIONES UTILITARIAS PARA TODO EL SITIO 
def get_municipios(request, departamento):
    municipios = Municipio.objects.filter(departamento = departamento)
    lista = [(municipio.id, municipio.nombre) for municipio in municipios]
    return HttpResponse(simplejson.dumps(lista), mimetype='application/javascript')
        
def get_comarca(request, municipio):
    comarcas = Comarca.objects.filter(municipio = municipio)
    lista = [(comarca.id, comarca.nombre) for comarca in comarcas]
    return HttpResponse(simplejson.dumps(lista), mimetype='application/javascript')

def indicadores(request):
    return render_to_response('encuestas/indicadores.html',
                              context_instance=RequestContext(request))
    
def datos_sexo(request):
    encuestas = _query_set_filtrado(request).values_list('id', flat=True)    
    composicion_familia = Composicion.objects.filter(encuesta__id__in=encuestas)    
    tabla_sexo_jefe = {1: 0, 2: 0, 3: 0}
    tabla_sexo_beneficiario = {}
    for composicion in composicion_familia:
        if composicion.relacion == 1:
            tabla_sexo_jefe[composicion.sexo] += 1
        else:
            tabla_sexo_jefe[composicion.sexo_jefe] += 1
    tabla_sexo_beneficiario['masculino'] = composicion_familia.filter(sexo=1).count()
    tabla_sexo_beneficiario['femenino'] = composicion_familia.filter(sexo=2).count()                
        
    return render_to_response('encuestas/datos_sexo.html', RequestContext(request, locals()))

def agua_clorada(request):
    encuestas = _query_set_filtrado(request).values_list('id', flat=True) 
    
    #aguas_cloradas = Encuesta.objects.filter(encuesta__id__in=encuestas)  
    tabla_aguas = {}
    tabla_aguas['m_clora'] = encuestas.filter(composicion__sexo_jefe=1,agua__calidad=1).count()
    tabla_aguas['m_trata'] = encuestas.filter(composicion__sexo_jefe=1,agua__calidad=2).count()
    tabla_aguas['masculino'] = tabla_aguas['m_clora'] + tabla_aguas['m_trata']
    tabla_aguas['f_clora'] = encuestas.filter(composicion__sexo_jefe=2,agua__calidad=1).count()
    tabla_aguas['f_trata'] = encuestas.filter(composicion__sexo_jefe=2,agua__calidad=2).count()
    tabla_aguas['femenino'] = tabla_aguas['f_clora'] + tabla_aguas['f_trata']
    tabla_aguas['total'] = tabla_aguas['masculino'] + tabla_aguas['femenino']
    
    return render_to_response('encuestas/agua_clorada.html', RequestContext(request,locals()))
def reducir_lista(lista):
    '''reduce la lista dejando solo los elementos que son repetidos
       osea lo contraron a unique'''
    nueva_lista = []
    for foo in lista:
        if lista.count(foo) > 1 and foo not in nueva_lista:
            nueva_lista.append(foo)
    return nueva_lista
