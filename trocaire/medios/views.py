# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import get_model, Sum, Q, Max, Min, Avg, Count
from django.utils import simplejson
from django.template.defaultfilters import slugify

#importaciones de los models
from forms import ConsultarForm
from trocaire.medios.templatetags.tools import *
from trocaire.medios.models import *
from trocaire.familia.models import *
from trocaire.participacion_ciudadana.models import *
from trocaire.crisis_alimentaria.models import *
from trocaire.tecnologia.models import *
from trocaire.lugar.models import *
from trocaire.ingresos.models import *
from trocaire.produccion.models import *
from trocaire.formas_propiedad.models import *
from trocaire.genero.models import *
import copy

def _query_set_filtrado(request):
    #anio = int(request.session['fecha'])
    params = {}
    if 'fecha' in request.session:
        params['fecha'] = request.session['fecha']
        
    if request.session['contraparte']:
        params['contraparte'] = request.session['contraparte'] 

    if request.session['departamento']:                     
        if request.session['municipio']:                
            if request.session['comarca']:
                params['comarca'] = request.session['comarca']
            else:                    
                params['municipio'] = request.session['municipio']
        else:                
            params['municipio__departamento'] = request.session['departamento']
            
    #validando filtro de dependencia familiar
    try:
        if request.session['indice_dep']:
            indice = request.session['indice_dep']
                              
            if indice == u'1':            
                params['composicion__dependientes__lt'] = 0.1
            elif indice == u'2':
                params['composicion__dependientes__range'] = (0.1, 1.0)
            elif indice == u'3':
                params['composicion__dependientes__range'] = (1.1, 2.0)
            elif indice == u'4':
                params['composicion__dependientes__range'] = (2.1, 3.0)
            elif indice == u'5':
                params['composicion__dependientes__gt'] = 3.0
    except:
        pass    
    
    #validando acceso a credito
    try:    
        if request.session['credito_acceso'] != 'None':
            params['credito'] = request.session['credito_acceso']
    except:
        pass
    
    unvalid_keys = []
    for key in params:
        if not params[key]:            
            #print params[key]
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
            ids = model.objects.filter(**request.session['parametros'][key]).values_list('encuesta__id', flat=True)                              
            encuestas_id += ids

    c_flag = params.get('contraparte', None) # flag para saber si se selecciono un contraparte con fin
    # de exluir a ADDAC Rancho Grande de la consulta general -> el jefe manda :P

    if not encuestas_id:
        qs = Encuesta.objects.filter(**params)
        # excluyendo a Rancho Grande a pedido de Boss XD
        if c_flag == None:
            return qs.exclude(municipio__nombre='Rancho Grande')
        return qs
    else:
        ids_definitivos = reducir_lista(encuestas_id) if reducir else encuestas_id            
        qs = Encuesta.objects.filter(id__in = ids_definitivos, **params)
        #excluyendo a Rancho Grande
        if c_flag == None:
            return qs.exclude(municipio__nombre='Rancho Grande')
        return qs

def reducir_lista(lista):
    '''reduce la lista dejando solo los elementos que son repetidos
       osea lo contraron a unique'''    
    nueva_lista = []
    for foo in lista:        
        if lista.count(foo) >= 1 and foo not in nueva_lista:
            nueva_lista.append(foo)         
    return nueva_lista

#===============================================================================
def consultar(request):
    if request.method == 'POST':
        form = ConsultarForm(request.POST)
        if form.is_valid():
            request.session['fecha'] = form.cleaned_data['fecha']
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
            
            #indice de dependencia
            request.session['indice_dep'] = form.cleaned_data['indice_dep']
            
            #acceso a credito
            request.session['credito_acceso'] = form.cleaned_data['credito_acceso']
            
            #cosas de otros modelos!
            parametros = {'familia.escolaridad': {}, 'familia.composicion': {}, 
                          'genero.tomadecicion': {}, 'ingresos.principalesfuentes': {},
                          'ingresos.totalingreso': {}}
            parametros['familia.escolaridad']['beneficia'] = form.cleaned_data['escolaridad_beneficiario']            
            parametros['familia.escolaridad']['conyugue'] = form.cleaned_data['escolaridad_conyugue']
            parametros['familia.composicion']['sexo'] = form.cleaned_data['familia_beneficiario']
            
            #algunos fixes para filtros multipresente
            if form.cleaned_data['familia_beneficiario']:
                request.session['familia_beneficiario'] = form.cleaned_data['familia_beneficiario']
            
            if form.cleaned_data['escolaridad_beneficiario']:
                request.session['escolaridad_beneficiario'] = form.cleaned_data['escolaridad_beneficiario']
            
            if form.cleaned_data['escolaridad_conyugue']:
                request.session['escolaridad_conyugue'] = form.cleaned_data['escolaridad_conyugue']
            
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
            
            #encuestas = _query_set_filtrado(request)
            
            if form.cleaned_data['next_url']:
                return HttpResponseRedirect(form.cleaned_data['next_url'])
            else:
                muestra_indicador = 1
                return render_to_response('encuestas/consultar.html', locals(),
                            context_instance=RequestContext(request))
    else:
        #reset session parameters
        reset_parameters(request)
        form = ConsultarForm()
    return render_to_response('encuestas/consultar.html', locals(),
                              context_instance=RequestContext(request))

def consultarsimple(request):
    if request.method == 'POST':
        form = ConsultarForm(request.POST)
        if form.is_valid():
            request.session['fecha'] = form.cleaned_data['fecha']            
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
                muestra_indicador = 1
                return render_to_response('encuestas/consultarsimple.html', locals(),
                            context_instance=RequestContext(request))
    else:
        reset_parameters(request)
        form = ConsultarForm()
    return render_to_response('encuestas/consultarsimple.html', locals(),
                              context_instance=RequestContext(request))

def reset_parameters(request):
    request.session['departamento'] = request.session['municipio'] = request.session['contraparte'] = \
    request.session['comarca'] = request.session['indice_dep'] = request.session['credito_acceso'] = None
    
    #print 'filters cleaned! :D'   

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
    
#========================= Salidas sencillas ==================================
def datos_sexo(request):    
    encuestas = _query_set_filtrado(request).values_list('id', flat=True)    
    composicion_familia = Composicion.objects.filter(encuesta__id__in=encuestas)
    '''1: Hombre, 2: Mujer'''    
    tabla_sexo_jefe = {1: 0, 2: 0}
    tabla_sexo_beneficiario = {}
    tabla_sexo_jefe[1] = encuestas.filter(sexo_jefe=1).count()
    tabla_sexo_jefe[2] = encuestas.filter(sexo_jefe=2).count()
    tabla_sexo_beneficiario['masculino'] = composicion_familia.filter(sexo=1).count()
    tabla_sexo_beneficiario['femenino'] = composicion_familia.filter(sexo=2).count()                
    dondetoy = "sexojefe"
    return render_to_response('encuestas/datos_sexo.html', RequestContext(request, locals()))
    
def comelon(request,hembra,macho):
    encuestas = _query_set_filtrado(request).values_list('id', flat=True) 
    hombre_jefes = encuestas.filter(sexo_jefe=1).count()
    mujer_jefes = encuestas.filter(sexo_jefe=2).count() 
    
    clorada = []
    total = 0
    for cloro in CHOICE_CALIDAD:
        count_men = encuestas.filter(sexo_jefe=macho,agua__calidad=cloro[0]).count()
        per_men = round(saca_porcentajes(count_men,hombre_jefes),0)
        count_woman = encuestas.filter(sexo_jefe=hembra,agua__calidad=cloro[0]).count()
        per_woman = round(saca_porcentajes(count_woman,mujer_jefes),0)
        total = count_men + count_woman
        clorada.append([cloro[1],count_men,per_men,count_woman,per_woman,total])
        
    return clorada
    
def mano_quebrada(request,hembra,macho):
    encuestas = _query_set_filtrado(request).values_list('id', flat=True) 
    hombre_jefes = encuestas.filter(sexo_jefe=1).count()
    mujer_jefes = encuestas.filter(sexo_jefe=2).count() 
    
    tratamiento = []
    total1 = 0
    for trata in CHOICE_CLORADA:
        count_men = encuestas.filter(sexo_jefe=macho,agua__clorada=trata[0]).count()
        per_men = round(saca_porcentajes(count_men,hombre_jefes),0)
        count_woman = encuestas.filter(sexo_jefe=hembra,agua__clorada=trata[0]).count()
        per_woman = round(saca_porcentajes(count_woman,mujer_jefes),0)
        total1 = count_men + count_woman
        tratamiento.append([trata[1],count_men,per_men,count_woman,per_woman,total1])
        
    return tratamiento
def agua_clorada(request):
    encuestas = _query_set_filtrado(request).values_list('id', flat=True) 
    numero = encuestas.count()  
    
    hombre_jefes = encuestas.filter(sexo_jefe=1).count()
    mujer_jefes = encuestas.filter(sexo_jefe=2).count()
    
    helmy = comelon(request,2,1)
    giacoman = mano_quebrada(request,2,1)
    #print giacoman
    dondetoy = "cloran"
    return render_to_response('encuestas/agua_clorada.html', RequestContext(request,locals()))
    
def gastan_horas(request):
    encuestas = _query_set_filtrado(request).values_list('id', flat=True)
    numero = encuestas.count()
    hombre_jefes = encuestas.filter(sexo_jefe=1).count()
    mujer_jefes = encuestas.filter(sexo_jefe=2).count()
    #salidas cuantas horas gastan 
    tablas_gastan = {}
    
    tablas_gastan['masculino'] = encuestas.filter(sexo_jefe=1, agua__tiempo=3).count()
    tablas_gastan['porcentaje_masculino'] = round(saca_porcentajes(tablas_gastan['masculino'],hombre_jefes),1)
    
    tablas_gastan['femenino'] = encuestas.filter(sexo_jefe=2, agua__tiempo=3).count()
    tablas_gastan['porcentaje_femenino'] = round(saca_porcentajes(tablas_gastan['femenino'],mujer_jefes),1)
    
    tablas_gastan['total'] =  tablas_gastan['masculino'] + tablas_gastan['femenino']
    tablas_gastan['porcentaje_total'] = round(saca_porcentajes(tablas_gastan['total'],numero),1)
    dondetoy = "recolectar"
    return render_to_response('encuestas/gastan_horas.html', RequestContext(request,locals()))

def manzana(request,sexo):
    encuestas = _query_set_filtrado(request)
    
    lista = []
    for x in encuestas.filter(sexo_jefe=sexo):
        query = AreaProtegida.objects.filter(encuesta=x, respuesta__in=[2,3,4,5]).aggregate(query=Sum('cantidad'))['query']
        if query > 0:
            lista.append(x.id)
    
    return lista    

def familias_practicas(request):
    encuestas = _query_set_filtrado(request).values_list('id', flat=True)
    
    hombre_jefes = encuestas.filter(sexo_jefe=1).count()
    mujer_jefes =  encuestas.filter(sexo_jefe=2).count()
        
    conservacion_h = manzana(request,1)
    conservacion_m = manzana(request,2)
    total = len(encuestas)
     
    hombre = len(conservacion_h)
    por_hombre = round(saca_porcentajes(hombre,hombre_jefes),1)
    mujer = len(conservacion_m)
    por_mujer = round(saca_porcentajes(mujer,mujer_jefes),1)
    
    total_h_m = hombre + mujer
    por_total_h_m = round(saca_porcentajes(total_h_m,total),1)
    
    no_total = total - total_h_m
    por_no_total = round(saca_porcentajes(no_total,total),1)
    no_hombre = hombre_jefes - hombre
    por_no_hombre = round(saca_porcentajes(no_hombre,hombre_jefes),1)
    no_mujer = mujer_jefes - mujer
    por_no_mujer = round(saca_porcentajes(no_mujer,mujer_jefes),1)     
    dondetoy = "conservacion"
    return render_to_response('encuestas/familias_practicas.html', RequestContext(request,locals()))

def rango_mz(request,sexo):
    encuestas = _query_set_filtrado(request)
    lista = []
    for x in encuestas.filter(sexo_jefe=sexo):
        query = Tierra.objects.filter(encuesta=x, area=1).aggregate(mujer=Sum('mujer'),
                                                            hombre=Sum('hombre'),
                                                            ambos=Sum('ambos'))
        lista.append([x.id,query])
    return lista
        
def acceso_tierra(request):
    encuestas = _query_set_filtrado(request)
    numero = encuestas.count()
    hombre_jefes = encuestas.filter(sexo_jefe=1).count()
    mujer_jefes = encuestas.filter(sexo_jefe=2).count()
    
    #salidas cuantas horas gastan
    dicc1 = {}
    dicc1_h_m = {}
    for a in CHOICE_AREA[1:5]:
        total = Tierra.objects.filter(area=a[0], encuesta__in=encuestas)
        dicc1[a[1]] = total.count()
        dicc1_h_m[a[1]] = _hombre_mujer_dicc(total.values_list('encuesta__id', flat=True))
    tabla_dicc1 = _order_dicc(copy.deepcopy(dicc1))
    
    #-------------- start clean code XD ---------------------
    '''rangos: 1 => 0, 2 => 0.1 a 1 mz, 3 => 1.1 a 5 mz, 4 => 5.1 a 10 mz, 5 => mas de 10 mz'''
     
    labels = {1: '0 mz', 2: '0.1 - 0.3 mz', 3: '0.31 - 1 mz', 4: '1.1 - 5 mz', 5: '5.1 - 10 mz', 6: 'más de 10 mz'}
    query = Tierra.objects.filter(encuesta__in=encuestas, area=1)
    total_all = query.count()
    total_hombre = query.filter(encuesta__sexo_jefe=1).count()
    total_mujer = query.filter(encuesta__sexo_jefe=2).count()
                   
    dicc = area_total_rangos(query)    
    dicc_hombre = area_total_rangos(query.filter(encuesta__sexo_jefe=1))    
    dicc_mujer = area_total_rangos(query.filter(encuesta__sexo_jefe=2))
    
    promedio_mz = round(query.aggregate(promedio=Avg('area_total'))['promedio'], 2)       
    
    dondetoy = "accesotierra"
    return render_to_response('encuestas/acceso_tierra.html', RequestContext(request,locals()))

def area_total_rangos(query):
    return {1: query.filter(area_total=0.0).count(),
            2: query.filter(area_total__range=(0.1, 0.3)).count(),
            3: query.filter(area_total__range=(0.31, 1.0)).count(),
            4: query.filter(area_total__range=(1.1, 5.0)).count(),
            5: query.filter(area_total__range=(5.1, 10.0)).count(),
            6: query.filter(area_total__gt=10.0).count()}

def riego(request,sexo,tipo):
    encuestas = _query_set_filtrado(request)
    
    lista = []
    suma = 0
    for x in encuestas.filter(sexo_jefe=sexo):
        query = Riego.objects.filter(encuesta=x, respuesta__in=[tipo]).aggregate(query=Sum('area'))['query']
        if query > 0:
            suma += query
            lista.append([x.id,suma])
    return lista
        
def acceso_agua(request):
    encuestas = _query_set_filtrado(request)
    numero = encuestas.count()
    hombre_jefes = encuestas.filter(sexo_jefe=1).count()
    mujer_jefes = encuestas.filter(sexo_jefe=2).count()
    #hombre acceso a agua para riego
    lista_a_h = riego(request,1,2)
    aspersion_h = len(lista_a_h)
    try:
        total_lista_a_h = lista_a_h[(len(lista_a_h))-1][1]
    except:
        total_lista_a_h = 0
    #-----------------------------
    lista_g_h = riego(request,1,3)
    goteo_h = len(lista_g_h)
    try:
        total_lista_g_h = lista_g_h[(len(lista_g_h))-1][1]
    except:
        total_lista_g_h = 0
    #-----------------------------
    lista_gra_h = riego(request,1,4)
    gravedad_h = len(lista_gra_h)
    try:
        total_lista_gra_h = lista_gra_h[(len(lista_gra_h))-1][1]
    except:
        total_lista_gra_h = 0
    #-------------------------------
    lista_o_h = riego(request,1,5)
    otro_h = len(lista_o_h)
    try:
        total_o_h = lista_o_h[(len(lista_o_h))-1][1]
    except:
        total_o_h = 0
    
    #mujer acceso a agua para riego
    lista_a_m = riego(request,2,2)
    aspersion_m = len(lista_a_m)
    try:
        total_lista_a_m = lista_a_m[(len(lista_a_m))-1][1]
    except:
        total_lista_a_m = 0
    #----------------------------
    lista_g_m = riego(request,2,3)
    goteo_m = len(lista_g_m)
    try:
        total_lista_g_m = lista_g_m[(len(lista_g_m))-1][1]
    except:
        total_lista_g_m = 0
    #-----------------------------
    lista_gra_m = riego(request,2,4)
    gravedad_m = len(lista_gra_m)
    try:
        total_lista_gra_m = lista_gra_m[(len(lista_gra_m))-1][1]
    except:
        total_lista_gra_m = 0
    #-------------------------------
    lista_o_m = riego(request,1,5)
    otro_m = len(lista_o_m)
    try:
        total_o_m = lista_o_m[(len(lista_o_m))-1][1]
    except:
        total_o_m = 0
    #total de conteo    
    total_aspersion = aspersion_h + aspersion_m
    total_goteo = goteo_h + goteo_m
    total_gravedad = gravedad_h + gravedad_m
    total_otros = otro_h + otro_m
    
    #calculo de los que no tienen riego
    no_tiene_riego = numero - (total_aspersion + total_goteo + total_gravedad + total_otros)
    
    #total de manzanas
    total_manzadas_aspersion = total_lista_a_h + total_lista_a_m
    total_manzadas_goteo = total_lista_g_h + total_lista_g_m
    total_manzanas_gravedad = total_lista_gra_h + total_lista_gra_m
    total_manzanas_otros = total_o_h + total_o_m
    dondetoy = "accesoagua"
    return render_to_response('encuestas/acceso_agua.html', RequestContext(request,locals()))

def reponsable(request,sexo):
    encuestas = _query_set_filtrado(request)
    
    lista = {}
    for hombre in CHOICE_GENERO:
        conteo = Genero.objects.filter(encuesta__in=encuestas, encuesta__sexo_jefe=sexo,
                                       responsabilidades=hombre[0]).count()
        lista[hombre[1]] = conteo   
    lista2 = _order_dicc(copy.deepcopy(lista))
    return lista2

def dependencia(request):
    encuestas = _query_set_filtrado(request)
    query = Composicion.objects.filter(encuesta__in=encuestas)
    query_hombre_jefe = query.filter(encuesta__sexo_jefe=1)
    query_mujer_jefe = query.filter(encuesta__sexo_jefe=2)
    
    tabla = vale_gaver(query)
    tabla_hombre = vale_gaver(query_hombre_jefe)
    tabla_mujer = vale_gaver(query_mujer_jefe)
    
    keys = {1: u'Igual a 0'
            , 2: u'De 0.1 a 1.0'
            , 3: u'De 1.1 a 2.0'
            , 4: u'De 2.1 a 3.0'
            , 5: u'Más de 3.0'}
    
    dondetoy = "dependencia"    
    return render_to_response('encuestas/dependencia.html', RequestContext(request, locals()))

def vale_gaver(query):
    return {u'Igual a 0': query.filter(dependientes__lte=0).count(), 
             u'De 0.1 a 1.0': query.filter(dependientes__range=(0.1, 1.0)).count(),
             u'De 1.1 a 2.0': query.filter(dependientes__range=(1.1, 2.0)).count(),
             u'De 2.1 a 3.0': query.filter(dependientes__range=(2.1, 3.0)).count(),             
             u'Más de 3.0': query.filter(dependientes__gt=3.0).count()}

def sueno_tengo(request, numero):
    encuestas = _query_set_filtrado(request)
    dicc2 = {}
    for filas in CHOICE_GENERO:
        key = slugify(filas[1]).replace('-', '_')
        dicc2[key] = {}
        for resp in CHOICE_GENERO_RESPUESTA:
            key2 = slugify(resp[1]).replace('-', '_')
            dicc2[key][key2] = conteo = encuestas.filter(sexo_jefe=numero,genero__responsabilidades=filas[0],genero__respuesta=resp[0]).count()
    
    return dicc2
    
    
def hombre_responsable(request):
    encuestas = _query_set_filtrado(request)
    numero = encuestas.count()
    hombre_jefes = encuestas.filter(sexo_jefe=1).count()
    mujer_jefes = encuestas.filter(sexo_jefe=2).count()
    
    carlos = sueno_tengo(request,1)
    lava = total_dict(carlos[u'152_lava_y_plancha'])
    cocina = total_dict(carlos[u'151_cocina'])
    lleva  = total_dict(carlos[u'150_lleva_sus_hijos_e_hijas_al_centro_de_salud'])
    asiste = total_dict(carlos[u'149_asiste_a_las_reuniones_de_la_escuela'])
    atiende = total_dict(carlos[u'154_atiende_a_sus_hijas_e_hijos'])
    barre = total_dict(carlos[u'153_barre_limpia_la_casa'])
    
    rocha = sueno_tengo(request,2)
    lava1 = total_dict(rocha[u'152_lava_y_plancha'])
    cocina1 = total_dict(rocha[u'151_cocina'])
    lleva1  = total_dict(rocha[u'150_lleva_sus_hijos_e_hijas_al_centro_de_salud'])
    asiste1 = total_dict(rocha[u'149_asiste_a_las_reuniones_de_la_escuela'])
    atiende1 = total_dict(rocha[u'154_atiende_a_sus_hijas_e_hijos'])
    barre1 = total_dict(rocha[u'153_barre_limpia_la_casa'])
    
  
    dondetoy = "hombreresp"
    return render_to_response('encuestas/hombre_responsable.html', RequestContext(request,locals()))    

def mujeres_decisiones(request):
    encuestas = _query_set_filtrado(request)
    numero = encuestas.count()
    tabla_mujeres = {}
    key = '% de familias según quien toma las decisiones'
    for a in CHOICE_ASPECTO:
        con_hombre = TomaDecicion.objects.filter(encuesta__in=encuestas, respuesta=1, aspectos=a[0]).count()
        con_mujer = TomaDecicion.objects.filter(encuesta__in=encuestas, respuesta=2, aspectos=a[0]).count()
        con_ambos = TomaDecicion.objects.filter(encuesta__in=encuestas, respuesta=3, aspectos=a[0]).count()
        no_aplica = TomaDecicion.objects.filter(encuesta__in=encuestas, respuesta=4, aspectos=a[0]).count()
        tabla_mujeres[a[1]] = {'hombre':con_hombre,'mujer':con_mujer,
                               'ambos':con_ambos,'no aplica':no_aplica}

    tabla_mu = _order_dicc(copy.deepcopy(tabla_mujeres))    
    dondetoy = "mujeresdecision"
    return render_to_response('encuestas/mujeres_decisiones.html', RequestContext(request,locals()))
    
def sexo_beneficiario(request):
    encuestas = _query_set_filtrado(request).values_list('id', flat=True)    
    '''1: hombre, 2: mujer'''
       
    query_hombre = Composicion.objects.filter(encuesta__id__in=encuestas.filter(sexo_jefe=1))
    query_mujer = Composicion.objects.filter(encuesta__id__in=encuestas.filter(sexo_jefe=2))
    
    mujer_jefe = {1:query_mujer.filter(sexo=1).count(), 2:query_mujer.filter(sexo=2).count()}
    hombre_jefe = {1:query_hombre.filter(sexo=1).count(), 2:query_hombre.filter(sexo=2).count()}
                            
    dondetoy = "sexobene"
    return render_to_response('encuestas/sexo_beneficiario.html', RequestContext(request, locals()))

def escolaridad(request):    
    encuestas = _query_set_filtrado(request)
    esc_benef = {}
    #escolaridad por hombre y mujer
    esc_h_m = {}
    for nivel_edu in CHOICE_ESCOLARIDAD:
        escolaridad_query = Escolaridad.objects.filter(beneficia=nivel_edu[0], encuesta__in=encuestas)
        esc_benef[nivel_edu[1]] = escolaridad_query.count()
        esc_h_m[nivel_edu[1]] = _hombre_mujer_dicc(escolaridad_query.values_list('encuesta__id', flat=True))        
    tabla_esc_benef = _order_dicc(copy.deepcopy(esc_benef))
    dondetoy = "escolaridad"
    return render_to_response('encuestas/escolaridad.html', RequestContext(request, locals()))

def credito(request):
    encuestas = _query_set_filtrado(request)
    opciones = Credito.objects.all().exclude(id__in=[1, 7])
    no_tiene = Credito.objects.get(id=1)
    credito = {}
    credito_h_m = {}    
    for op in opciones:
        query = AccesoCredito.objects.filter(Q(hombre=op) | Q(mujer=op), encuesta__in=encuestas)        
        credito[op.nombre] = query.count()        
        credito_h_m[op.nombre] = {1: query.filter(encuesta__sexo_jefe=1).count(), 
                                  2: query.filter(encuesta__sexo_jefe=2).count()}
        
    query_no_tiene = AccesoCredito.objects.filter(hombre=no_tiene, mujer=no_tiene, encuesta__in=encuestas)
    credito[no_tiene.nombre] = query_no_tiene.count()
    credito_h_m[no_tiene.nombre] = {1: query_no_tiene.filter(encuesta__sexo_jefe=1).count(), 
                                  2: query_no_tiene.filter(encuesta__sexo_jefe=2).count()}
    
    tabla_credito = _order_dicc(copy.deepcopy(credito))
    
    hombre_jefe = encuestas.filter(sexo_jefe=1).count()
    mujer_jefe = encuestas.filter(sexo_jefe=2).count()
    dondetoy = "creditofamilia"
    return render_to_response('encuestas/credito.html', RequestContext(request, locals()))

def participacion(request):
    encuestas = _query_set_filtrado(request)
    total_general = encuestas.count()    
    query_all = ParticipacionCPC.objects.filter(encuesta__in=encuestas)
    part_cpc = get_participacion(query_all, 1)
    part_asam = get_participacion(query_all, 2)
    
    #-- obtener cuando el jefe de familia es hombre
    query_hombre = ParticipacionCPC.objects.filter(encuesta__in=encuestas.filter(sexo_jefe=1))
    part_cpc_hombre = get_participacion(query_hombre, 1)
    part_asam_hombre = get_participacion(query_hombre, 2)
        
    #-- obtener cuando el jefe de familia es mujer
    query_mujer = ParticipacionCPC.objects.filter(encuesta__in=encuestas.filter(sexo_jefe=2))
    part_cpc_mujer = get_participacion(query_mujer, 1)
    part_asam_mujer = get_participacion(query_mujer, 2) 
    
    hombre_jefe = encuestas.filter(sexo_jefe=1).count()
    mujer_jefe = encuestas.filter(sexo_jefe=2).count()
    
    dondetoy = "participacion"
    return render_to_response('encuestas/participacion.html', RequestContext(request, locals()))

def get_participacion(query_param, organismo):    
    query = query_param.filter(organismo=organismo)
    dicc = {'hombre': query.filter(hombre__gt=0).count(), 
            'mujer': query.filter(mujer__gt=0).count(),
            'ambos': query.filter(ambos__gt=0).count(),
            'total': query.count()}     
    return dicc

def ingreso_agropecuario(request):
    encuestas = _query_set_filtrado(request)
    query = PrincipalesFuentes.objects.filter(encuesta__in=encuestas)    
    
    #obtener queries segun jefe de familia
    query_hombre = PrincipalesFuentes.objects.filter(encuesta__in=encuestas.filter(sexo_jefe=1))
    query_mujer = PrincipalesFuentes.objects.filter(encuesta__in=encuestas.filter(sexo_jefe=2))
            
    ingreso_agropecuario = {'total': query.filter(fuentes_ap__gte=1).count(),
            'hombre': query_hombre.filter(fuentes_ap__gte=1).count(), 
            'mujer': query_mujer.filter(fuentes_ap__gte=1).count()}
    dondetoy = "actividadesagro"
    return render_to_response('encuestas/ingreso_agropecuario.html', RequestContext(request, locals()))

def ingreso_familiar(request, agro='total', titulo=None, dondetoy='ingresosfam'):
    encuestas = _query_set_filtrado(request)
    ingresos = TotalIngreso.objects.filter(encuesta__in=encuestas).values_list(agro, flat=True)
    
    #obtener queries segun jefe de familia
    query_hombre_jefe = TotalIngreso.objects.filter(encuesta__in=encuestas.filter(sexo_jefe=1)).values_list(agro, flat=True)
    query_mujer_jefe = TotalIngreso.objects.filter(encuesta__in=encuestas.filter(sexo_jefe=2)).values_list(agro, flat=True)     
    
    promedio = {'total': calcular_promedio(ingresos),
                'hombre_jefe': calcular_promedio(query_hombre_jefe),
                'mujer_jefe': calcular_promedio(query_mujer_jefe)    
                }
    
    mediana = {'total': calcular_mediana(ingresos),
                'hombre_jefe': calcular_mediana(query_hombre_jefe),
                'mujer_jefe': calcular_mediana(query_mujer_jefe)                
                }
    return render_to_response('encuestas/ingreso_familiar.html', RequestContext(request, locals()))

def abastecimiento(request):
    encuestas = _query_set_filtrado(request)
    jefes_ids = _queryid_hombre_mujer(encuestas.values_list('id', flat=True), flag=True)     
    frijol = {1: 0, 2: 0}
    maiz = {1: 0, 2: 0}
    
    encuestas_sin_consumo = []
    encuestas_sin_maiz = []
    encuestas_sin_frijol = []
    
    for key, lista in {1: encuestas.filter(sexo_jefe=1), 2: encuestas.filter(sexo_jefe=2)}.items():
        for encuesta in lista:
            #total_personas = sum([desc.femenino+desc.masculino for desc in Descripcion.objects.filter(encuesta=encuesta)])
            try:
                consumo_query = ConsumoDiario.objects.get(encuesta=encuesta)
                maiz_query = CultivosPeriodos.objects.get(encuesta=encuesta, cultivos__id=1)                
            except ConsumoDiario.DoesNotExist:
                encuestas_sin_consumo.append(encuesta.id)                        
                continue
            except CultivosPeriodos.DoesNotExist:
                encuestas_sin_maiz.append(encuesta.id)                     
                continue
            except:                
                continue
                
            try:
                frijol_query = CultivosPeriodos.objects.get(encuesta=encuesta, cultivos__id=3)                
            except CultivosPeriodos.DoesNotExist:
                encuestas_sin_frijol.append(encuesta.id)                
                continue
            
            produccion_diaria_maiz = round((maiz_query.produccion*float(100))/float(365), 2)
            produccion_diaria_frijol = round((frijol_query.produccion*float(100))/float(365), 2)
            if consumo_query.maiz <= produccion_diaria_maiz:
                maiz[key] += 1
        
            if consumo_query.frijol <= produccion_diaria_frijol:
                frijol[key] += 1
                
    frijol['total'] = sum(frijol.values())
    maiz['total'] = sum(maiz.values())
    
    totales = {1: len(jefes_ids[1]), 2: len(jefes_ids[2]), 3: len(jefes_ids[3])}
    totales['total'] = sum(totales.values())
    dondetoy = "autoabastecimiento"
    return render_to_response('encuestas/abastecimiento.html', RequestContext(request, locals()))

def diversidad_alimentaria(request):
    titulo = u'Diversidad de la dieta familiar'
    encuestas = _query_set_filtrado(request)
    query_hombre = encuestas.filter(sexo_jefe=1)
    query_mujer = encuestas.filter(sexo_jefe=2)
    
    dicc = get_diversidad_dicc(encuestas)
    dicc_hombre = get_diversidad_dicc(query_hombre)
    dicc_mujer = get_diversidad_dicc(query_mujer)    
    
    total = total_dict(dicc)
    total_hombre = total_dict(dicc_hombre)
    total_mujer = total_dict(dicc_mujer)
    
    labels = {1: 'Al menos 1', 2: 'Al menos 2',
              3: 'Al menos 3', 4: 'Al menos 4',
              5: 'Al menos 5', 6: 'Al menos 6',
              7: 'Al menos 7'}
    dondetoy = "diversidad_ali"
    return render_to_response('encuestas/diversidad_alimentaria.html', RequestContext(request, locals()))

def get_diversidad_dicc(query):
    dicc = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
    
    #grupos de alimentos
    granos = [1, 2, 3, 4, 5] #maiz, frijol, sorgo y arroz
    feculas = [6, 7, 8, 9] #papas, camote, yuca, malanga
    frutas_verduras = [10, 11, 12, 13] #verduras, hostalizas, frutas 
    lacteos = [14, 15] #lacteo y huevos
    carne = [16] #carne
    grasas = [17] #grasas y aceite
    otros = [18, 19, 20]
    
    for obj in query:
        grupo = 0
        for group in granos, feculas, frutas_verduras, lacteos, carne, grasas, otros:
            if obj.diversidad_set.filter(alimento__id__in=group, respuesta=1).count() != 0:
                grupo += 1
        
        if grupo != 0:
            dicc[grupo] += 1
                    
    return dicc

def diversificacion_productiva(request):
#    import inspect
#    print "My name is: %s" % inspect.stack()[0][3]
    titulo = u'Diversificación productiva'
    encuestas = _query_set_filtrado(request)
    query_hombre = encuestas.filter(sexo_jefe=1)
    query_mujer = encuestas.filter(sexo_jefe=2)
    
    dicc = get_div_produc(encuestas)
    dicc_hombre = get_div_produc(query_hombre)
    dicc_mujer = get_div_produc(query_mujer)    
    
    total = total_dict(dicc)
    total_hombre = total_dict(dicc_hombre)
    total_mujer = total_dict(dicc_mujer)
    
    labels = {0: 'Ninguno', 1: '1 cultivo', 2: '2 cultivos',
              3: '3 cultivos', 4: '4 cultivos',
              5: '5 cultivos', 6: '6 cultivos',
              7: '7 cultivos', 8: '8 cultivos o más'}
    dondetoy = "div_produc"
    
    return render_to_response('encuestas/diversificacion_productiva.html', RequestContext(request, locals()))

def get_div_produc(query):
    dicc = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for obj in query:
        c_periodos = obj.cultivosperiodos_set.filter().count()
        c_permanentes = obj.cultivospermanentes_set.filter().count()
        c_anuales = obj.cultivosanuales_set.filter().count()
        c_hortalizas = obj.hortalizas_set.filter().count()
        cultivos = c_periodos + c_permanentes + c_anuales + c_hortalizas
        if cultivos > 0 and cultivos < 8:
            dicc[cultivos] += 1
        elif cultivos >= 8:
            dicc[8] += 1
        else:
            dicc[cultivos] += 1
    
    return dicc

def venta_organizada(request):
    encuestas = _query_set_filtrado(request)
    labels = {1: '% de familias que venden', 2: '% de familias que no venden'}
    titulo = u'Acceso de las familias para vender sus productos de forma organizada'
    
    filtro = [2, 3, 4]
    venta = get_vende_num(encuestas, filtro)
    venta_hombre = get_vende_num(encuestas.filter(sexo_jefe=1), filtro)
    venta_mujer = get_vende_num(encuestas.filter(sexo_jefe=2), filtro)
    
    total = sum(venta)
    total_hombre = sum(venta_hombre)
    total_mujer = sum(venta_mujer)
            
    dicc = {1: venta[0], 2: venta[1]}
    dicc_hombre = {1: venta_hombre[0], 2: venta_hombre[1]}
    dicc_mujer = {1: venta_mujer[0], 2: venta_mujer[1]}  
    dondetoy = "venta_org"
    return render_to_response('encuestas/venta_organizada.html', RequestContext(request, locals()))

def familias_venden(request):
    encuestas = _query_set_filtrado(request)    
    labels = {1: '% de familias que venden', 2: '% de familias que no venden'}
    titulo = 'Familias que venden sus productos'
    
    filtro = [1, 2, 3, 4]
    venta = get_vende_num(encuestas, filtro)
    venta_hombre = get_vende_num(encuestas.filter(sexo_jefe=1), filtro)
    venta_mujer = get_vende_num(encuestas.filter(sexo_jefe=2), filtro)
    
    total = sum(venta)
    total_hombre = sum(venta_hombre)
    total_mujer = sum(venta_mujer)
            
    dicc = {1: venta[0], 2: venta[1]}
    dicc_hombre = {1: venta_hombre[0], 2: venta_hombre[1]}
    dicc_mujer = {1: venta_mujer[0], 2: venta_mujer[1]}  
    dondetoy = "familias_venden"
    return render_to_response('encuestas/venta_organizada.html', RequestContext(request, locals()))

def get_vende_num(query, filtro):
    venden = novenden = 0    
    for obj in query:
        n = obj.vendeproducto_set.filter(forma__in=filtro).count()
        if n != 0:
            venden += 1
        n1 = obj.vendeproducto_set.filter(forma=5).count()
        if n1 != 0:
            novenden += 1
    return venden, novenden

def procesando_productos(request):
    encuestas = _query_set_filtrado(request)
    labels = {1: '% de familias procesando', 2: '% de familias que no procesan'}
    
    venta = get_proces_num(encuestas)
    venta_hombre = get_proces_num(encuestas.filter(sexo_jefe=1))
    venta_mujer = get_proces_num(encuestas.filter(sexo_jefe=2))
    
    total = sum(venta)
    total_hombre = sum(venta_hombre)
    total_mujer = sum(venta_mujer)
            
    dicc = {1: venta[0], 2: venta[1]}
    dicc_hombre = {1: venta_hombre[0], 2: venta_hombre[1]}
    dicc_mujer = {1: venta_mujer[0], 2: venta_mujer[1]}  
    dondetoy = "procesando_prod"
    return render_to_response('encuestas/procesando_productos.html', RequestContext(request, locals()))

def get_proces_num(query):
    procesan = noprocesan = 0    
    for obj in query:
        n = obj.productosprocesado_set.all().count()
        if n != 0:
            procesan += 1
    noprocesan = query.count() - procesan        
    return procesan, noprocesan

def tecnologia_agricola(request):
    encuestas = _query_set_filtrado(request)        
    labels = {1: u'% de familias que usan tecnología agricola para fertilizar'}
    
    venta = get_fam_organica(encuestas)
    venta_hombre = get_fam_organica(encuestas.filter(sexo_jefe=1))
    venta_mujer = get_fam_organica(encuestas.filter(sexo_jefe=2))
    
    total = sum(venta)
    total_hombre = sum(venta_hombre)
    total_mujer = sum(venta_mujer)
            
    dicc = {1: venta[0]}
    dicc_hombre = {1: venta_hombre[0]}
    dicc_mujer = {1: venta_mujer[0]}
    dondetoy = "tecnologia"
    return render_to_response('encuestas/tecnologia_agricola.html', RequestContext(request, locals()))

def get_fam_organica(query):
    counter = falso = 0
    for obj in query:
        subquery = obj.usotecnologia_set.all()
        n = subquery.filter(Q(granos=1) | Q(anuales=1) | Q(permanentes=1) | Q(pastos=1), tecnologia=3).count()
        n1 = subquery.filter(Q(granos=1) | Q(anuales=1) | Q(permanentes=1) | Q(pastos=1), tecnologia=4).count()
        if (n != 0 and n1 != 0) or n != 0 or n1 != 0:
            counter += 1
        else:
            falso += 1
            
    return counter, falso

def _hombre_mujer_dicc(ids, jefe=False):
    '''Funcion que por defecto retorna la cantidad de beneficiarios
    hombres y mujeres de una lista de ids. Si jefe=True, retorna los
    jefes de familia hombres y mujeres segun la lista de ids :D'''
    composicion_familia = Composicion.objects.filter(encuesta__id__in=ids)
    if jefe:
        '''1: Hombre, 2: Mujer, 3: Compartido'''    
        dicc = {1: 0, 2: 0}    
        for composicion in composicion_familia:
            #validar si el beneficiario es el jefe de familia
            if composicion.beneficio in [1, 3]:
                dicc[composicion.sexo] += 1
            elif composicion.beneficio == 2:
                if composicion.sexo_jefe in [1, 2]:
                    dicc[composicion.sexo_jefe] += 1
                else:
                    dicc[composicion.sexo] += 1
            
        return dicc
                       
    return {
            'hombre': composicion_familia.filter(sexo=1).count(),
            'mujer': composicion_familia.filter(sexo=2).count()
            }

def _queryid_hombre_mujer(ids, flag=False):
    '''funcion que retorna las encuestas separadas por tipo de jefe,
    Hombre, Mujer y Compartido'''
    composicion_familia = Composicion.objects.filter(encuesta__id__in=ids)
    
    '''1: Hombre, 2: Mujer, 3: Compartido'''    
    dicc = {1: [], 2: [], 3: []}
    for composicion in composicion_familia:
        #validar si el beneficiario es el jefe de familia
        if composicion.beneficio in [1, 3]:
            if not flag:
                dicc[composicion.sexo].append(composicion.encuesta.id)
            else:
                dicc[composicion.sexo].append(composicion.encuesta)
        else:
            if not flag:
                dicc[composicion.sexo_jefe].append(composicion.encuesta.id)
            else:
                dicc[composicion.sexo_jefe].append(composicion.encuesta)                         
        
            
    return dicc                    
     
def _order_dicc(dicc):
    return sorted(dicc.items(), key=lambda x: x[1], reverse=True)
      
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

def calcular_promedio(lista):
    n = len(lista)
    total_suma = sum(lista)
    
    return round(total_suma/n, 2) 

def calcular_mediana(lista):
    n = len(lista)
    lista = sorted(lista)
    
    #calcular si lista es odd or even
    if (n%2) == 1:
        index = (n+1)/2
        return lista[index-1]
    else:
        index_1 = (n/2)
        index_2 = index_1+1
        return calcular_promedio([lista[index_1-1], lista[index_2-1]])
