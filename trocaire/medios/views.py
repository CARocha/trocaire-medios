# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import get_model, Sum, Q, Max, Min, Avg, Count
from django.utils import simplejson

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
    #if 'fecha' in request.session:
    #    params['fecha__year'] = anio
        
    if 'contraparte' in request.session:
        params['contraparte'] =  request.session['contraparte'] 

        if 'departamento' in request.session:                     
            if request.session['municipio']:                
                if request.session['comarca']:
                    params['comarca'] = request.session['comarca']
                else:                    
                    params['municipio'] = request.session['municipio']
            else:                
                params['municipio__departamento'] = request.session['departamento']
            
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
                ids = model.objects.filter(**request.session['parametros'][key]).values_list('encuesta__id', flat=True)                              
                encuestas_id += ids
        if not encuestas_id:
            return Encuesta.objects.filter(**params)
        else:
            ids_definitivos = reducir_lista(encuestas_id) if reducir else encuestas_id            
            return Encuesta.objects.filter(id__in = ids_definitivos, **params)

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
            #dependientes
            parametros['familia.composicion']['dependientes__gte'] = form.cleaned_data['dependientes_min']
            parametros['familia.composicion']['dependientes__lte'] = form.cleaned_data['dependientes_max']
            #parametros['formas_propiedad.finca']['area'] = forms.cleaned_data['finca_area_total']
            #parametros['produccion.ganadomayor']['num_vacas'] = forms.cleaned_data['finca_num_vacas']
            #parametros['finca']['conssa'] = forms.cleaned_data['finca_conssa']
            #parametros['finca']['num_productos'] = forms.cleaned_data['finca_num']
            request.session['parametros'] = parametros
            
            encuestas = _query_set_filtrado(request)
            
            
            if form.cleaned_data['next_url']:
                return HttpResponseRedirect(form.cleaned_data['next_url'])
            else:
                muestra_indicador = 1
                return render_to_response('encuestas/consultar.html', locals(),
                            context_instance=RequestContext(request))
    else:
        form = ConsultarForm()
    return render_to_response('encuestas/consultar.html', locals(),
                              context_instance=RequestContext(request))

def consultarsimple(request):
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
            #dependientes
            parametros['familia.composicion']['dependientes__gte'] = form.cleaned_data['dependientes_min']
            parametros['familia.composicion']['dependientes__lte'] = form.cleaned_data['dependientes_max']
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
        form = ConsultarForm()
    return render_to_response('encuestas/consultarsimple.html', locals(),
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

def agua_clorada(request):
    encuestas = _query_set_filtrado(request).values_list('id', flat=True) 
    numero = encuestas.count()  
    tabla_aguas = {}
    
    tabla_aguas['m_clora'] = encuestas.filter(sexo_jefe=1,agua__calidad=1).count()
    tabla_aguas['m_trata'] = encuestas.filter(sexo_jefe=1,agua__clorada=1).count()
    tabla_aguas['m_no'] = encuestas.filter(sexo_jefe=1,agua__clorada=2, agua__calidad=2).count()
    tabla_aguas['m_no_sabe'] = encuestas.filter(sexo_jefe=1,agua__calidad=3).count()
    
    #tabla_aguas['masculino'] = tabla_aguas['m_clora'] + tabla_aguas['m_trata']
    tabla_aguas['porcentaje_m_clora'] = round(saca_porcentajes(tabla_aguas['m_clora'],numero),1)
    tabla_aguas['porcentaje_m_trata'] = round(saca_porcentajes(tabla_aguas['m_trata'],numero),1)
    tabla_aguas['porcentaje_m_no'] = round(saca_porcentajes(tabla_aguas['m_no'],numero),1)
    tabla_aguas['porcentaje_m_no_sabe'] = round(saca_porcentajes(tabla_aguas['m_no_sabe'],numero),1)
    
    tabla_aguas['f_clora'] = encuestas.filter(sexo_jefe=2,agua__calidad=1).count()
    tabla_aguas['f_trata'] = encuestas.filter(sexo_jefe=2,agua__clorada=1).count()
    tabla_aguas['f_no'] = encuestas.filter(sexo_jefe=2,agua__clorada=2, agua__calidad=2).count()
    tabla_aguas['f_no_sabe'] = encuestas.filter(sexo_jefe=2,agua__calidad=3).count()
    
    #tabla_aguas['femenino'] = tabla_aguas['f_clora'] + tabla_aguas['f_trata']
    tabla_aguas['porcentaje_f_clora'] = round(saca_porcentajes(tabla_aguas['f_clora'],numero),1)
    tabla_aguas['porcentaje_f_trata'] = round(saca_porcentajes(tabla_aguas['f_trata'],numero),1)
    tabla_aguas['porcentaje_f_no'] = round(saca_porcentajes(tabla_aguas['f_no'],numero),1)
    tabla_aguas['porcentaje_f_no_sabe'] = round(saca_porcentajes(tabla_aguas['f_no_sabe'],numero),1)
    
    tabla_aguas['combinado_cloran'] = tabla_aguas['m_clora'] + tabla_aguas['f_clora']
    tabla_aguas['combinado_tratan'] = tabla_aguas['m_trata'] + tabla_aguas['f_trata']
    tabla_aguas['combinado_no_sabe'] = tabla_aguas['m_no_sabe'] + tabla_aguas['f_no_sabe']
    tabla_aguas['combinado_no'] = tabla_aguas['m_no'] + tabla_aguas['f_no']
    
    #tabla_aguas['total'] =  tabla_aguas['masculino'] + tabla_aguas['femenino']
    tabla_aguas['porcentaje_cloran'] = round(saca_porcentajes(tabla_aguas['combinado_cloran'],numero),1)
    tabla_aguas['porcentaje_tratan'] = round(saca_porcentajes(tabla_aguas['combinado_tratan'],numero),1)
    tabla_aguas['porcentaje_no_saben'] = round(saca_porcentajes(tabla_aguas['combinado_no_sabe'],numero),1)
    tabla_aguas['porcentaje_no'] = round(saca_porcentajes(tabla_aguas['combinado_no'],numero),1)
    dondetoy = "cloran"
    return render_to_response('encuestas/agua_clorada.html', RequestContext(request,locals()))
    
def gastan_horas(request):
    encuestas = _query_set_filtrado(request).values_list('id', flat=True)
    numero = encuestas.count()
    #salidas cuantas horas gastan 
    tablas_gastan = {}
    
    tablas_gastan['masculino'] = encuestas.filter(sexo_jefe=1, agua__tiempo=3).count()
    tablas_gastan['porcentaje_masculino'] = round(saca_porcentajes(tablas_gastan['masculino'],numero),1)
    
    tablas_gastan['femenino'] = encuestas.filter(sexo_jefe=2, agua__tiempo=3).count()
    tablas_gastan['porcentaje_femenino'] = round(saca_porcentajes(tablas_gastan['femenino'],numero),1)
    
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
     
    conservacion_h = manzana(request,1)
    conservacion_m = manzana(request,2)
    total = len(encuestas)
     
    hombre = len(conservacion_h)
    por_hombre = round(saca_porcentajes(hombre,total),1)
    mujer = len(conservacion_m)
    por_mujer = round(saca_porcentajes(mujer,total),1)
    
    total_h_m = hombre + mujer
    por_total_h_m = round(saca_porcentajes(total_h_m,total),1)
    
    no_total = total - total_h_m
    por_no_total = round(saca_porcentajes(no_total,total),1)
    no_hombre = total - hombre
    por_no_hombre = round(saca_porcentajes(no_hombre,total),1)
    no_mujer = total - mujer
    por_no_mujer = round(saca_porcentajes(no_mujer,total),1)     
    dondetoy = "conservacion"
    return render_to_response('encuestas/familias_practicas.html', RequestContext(request,locals()))

def acceso_tierra(request):
    encuestas = _query_set_filtrado(request)
    numero = encuestas.count()
    #salidas cuantas horas gastan
    dicc1 = {}
    dicc1_h_m = {}
    for a in CHOICE_AREA[1:5]:
        total = Tierra.objects.filter(area=a[0], encuesta__in=encuestas)
        dicc1[a[1]] = total.count()
        dicc1_h_m[a[1]] = _hombre_mujer_dicc(total.values_list('encuesta__id', flat=True))
    tabla_dicc1 = _order_dicc(copy.deepcopy(dicc1))
    dondetoy = "accesotierra"
    return render_to_response('encuestas/acceso_tierra.html', RequestContext(request,locals()))

def riego(request,sexo,tipo):
    encuestas = _query_set_filtrado(request)
    
    lista = []
    suma = 0
    for x in encuestas.filter(sexo_jefe=sexo):
        query = Riego.objects.filter(encuesta=x, respuesta__in=[tipo]).aggregate(query=Sum('area'))['query']
        if query > 0:
            suma += query
            lista.append([x.id,suma])
    print lista
    return lista
        
def acceso_agua(request):
    encuestas = _query_set_filtrado(request)
    numero = encuestas.count()
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
    
def hombre_responsable(request):
    encuestas = _query_set_filtrado(request)
    numero = encuestas.count()
    tabla_responsable = {}
    for hombre in CHOICE_GENERO:
        conteo = Genero.objects.filter(encuesta__in=encuestas, responsabilidades=hombre[0]).count()
        tabla_responsable[hombre[1]] = conteo

    tabla_resp = _order_dicc(copy.deepcopy(tabla_responsable))
    dondetoy = "hombreresp"
    return render_to_response('encuestas/hombre_responsable.html', RequestContext(request,locals()))    

def mujeres_decisiones(request):
    encuestas = _query_set_filtrado(request)
    numero = encuestas.count()
    tabla_mujeres = {}
    for a in CHOICE_ASPECTO:
        con_hombre = TomaDecicion.objects.filter(encuesta__in=encuestas, respuesta=1, aspectos=a[0]).count()
        con_mujer = TomaDecicion.objects.filter(encuesta__in=encuestas, respuesta=2, aspectos=a[0]).count()
        con_ambos = TomaDecicion.objects.filter(encuesta__in=encuestas, respuesta=3, aspectos=a[0]).count()
        no_aplica = TomaDecicion.objects.filter(encuesta__in=encuestas, respuesta=4, aspectos=a[0]).count()
        tabla_mujeres[a[1]] = (con_hombre,con_mujer,con_ambos,no_aplica)

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
    opciones = Credito.objects.all()
    credito = {}
    credito_h_m = {}    
    for op in opciones:
        query = AccesoCredito.objects.filter(Q(hombre=op) | Q(mujer=op) | Q(otro_hombre=op) | Q(otra_mujer=op),
                                                                encuesta__in=encuestas)
        credito[op.nombre] = query.count()
        credito_h_m[op.nombre] = _hombre_mujer_dicc(query.values_list('encuesta__id', flat=True), jefe=True)
    tabla_credito = _order_dicc(copy.deepcopy(credito))
    dondetoy = "creditofamilia"
    return render_to_response('encuestas/credito.html', RequestContext(request, locals()))

def participacion(request):
    encuestas = _query_set_filtrado(request)    
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

def ingreso_familiar(request):
    encuestas = _query_set_filtrado(request)
    ingresos = TotalIngreso.objects.filter(encuesta__in=encuestas).values_list('total', flat=True)
    
    #obtener queries segun jefe de familia
    query_hombre_jefe = TotalIngreso.objects.filter(encuesta__in=encuestas.filter(sexo_jefe=1)).values_list('total', flat=True)
    query_mujer_jefe = TotalIngreso.objects.filter(encuesta__in=encuestas.filter(sexo_jefe=2)).values_list('total', flat=True)    
    
    
    promedio = {'total': calcular_promedio(ingresos),
                'hombre_jefe': calcular_promedio(query_hombre_jefe),
                'mujer_jefe': calcular_promedio(query_mujer_jefe)    
                }
    
    mediana = {'total': calcular_mediana(ingresos),
                'hombre_jefe': calcular_mediana(query_hombre_jefe),
                'mujer_jefe': calcular_mediana(query_mujer_jefe)                
                }
    dondetoy = "ingresosfam"
    return render_to_response('encuestas/ingreso_familiar.html', RequestContext(request, locals()))

def abastecimiento(request):
    encuestas = _query_set_filtrado(request)
    jefes_ids = _queryid_hombre_mujer(encuestas.values_list('id', flat=True), flag=True)     
    frijol = {1: 0, 2: 0, 3: 0}
    maiz = {1: 0, 2: 0, 3: 0}
    
    encuestas_sin_consumo = []
    encuestas_sin_maiz = []
    encuestas_sin_frijol = []
    
    for key, lista in jefes_ids.items():
        for encuesta in lista:
            #total_personas = sum([desc.femenino+desc.masculino for desc in Descripcion.objects.filter(encuesta=encuesta)])
            try:
                consumo_query = ConsumoDiario.objects.get(encuesta=encuesta)
                maiz_query = CultivosPeriodos.objects.get(encuesta=encuesta, cultivos__id=1)                
            except ConsumoDiario.DoesNotExist:
                encuestas_sin_consumo.append(encuesta.id)
                jefes_ids[key].remove(encuesta)              
                continue
            except CultivosPeriodos.DoesNotExist:
                encuestas_sin_maiz.append(encuesta.id)   
                jefes_ids[key].remove(encuesta)             
                continue
            except:                
                continue
                
            try:
                frijol_query = CultivosPeriodos.objects.get(encuesta=encuesta, cultivos__id=3)                
            except CultivosPeriodos.DoesNotExist:
                encuestas_sin_frijol.append(encuesta.id)
                jefes_ids[key].remove(encuesta)
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
