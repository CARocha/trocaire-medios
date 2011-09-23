# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('trocaire.ingresos.views',
    #url(r'rangos/$', 'ingreso_por_rango', name="ingreso_por_rango"),
    #url(r'rangos/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'ingreso_por_rango', name="ingreso_por_rango"),
    #url(r'rangos/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'ingreso_por_rango', name="ingreso_por_rango"),
    url(r'rangos/$', 'generic_range', {'title': 'Ingresos familiares anuales totales', 'subtitle': 'Según rangos en Córdobas (C$) (o US Dólares, según lo que se decida)', 'eje': 'Cordoba', 'serie': 'Ingreso','model': 'totalingreso', 'field': 'total','dondetoy2':'totalingreso'}, name="ingresos_generic_range"),
    url(r'rangos/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', {'title': 'Ingresos Totales', 'subtitle': 'algo', 'eje': 'Cordoba', 'serie': 'Ingreso','model':'totalingreso', 'field': 'total','dondetoy2':'totalingreso'}, name="ingresos_generic_range"),
    #url(r'rangos/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', {'title': 'Ingresos Totales', 'subtitle': 'algo', 'eje': 'Cordoba', 'serie': 'Ingreso','model':'totalingreso', 'field': 'total','dondetoy':'totalingreso'}, name="ingresos_generic_range"),
    #ingreso ganado
    url(r'rangos/ganado/$', 'generic_range', {'model': 'ingresoganado', 'field': 'total', 'title': 'Ingreso por ganado', 'subtitle': 'grafico ingreso', 'serie': 'Num Fuentes', 'eje': 'miles de cordobas','dondetoy2':'ganadoingreso'}, name="ingresos_ganado"),
    url(r'rangos/ganado/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', {'model': 'ingresoganado', 'field': 'total', 'title': 'Ingreso por ganado', 'serie': 'Num Fuentes', 'subtitle': 'grafico ingreso', 'eje': 'miles de cordobas','dondetoy2':'ganadoingreso'}, name="ingresos_ganado"),
    #url(r'rangos/ganado/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', {'model': 'ingresoganado', 'field': 'total', 'title': 'Ingreso por ganado', 'serie': 'Num Fuentes', 'subtitle': 'grafico ingreso', 'eje': 'miles de cordobas'}, name="ingresos_ganado"),
    #fuentes ap
    url(r'rangos/fuentes-ap/$', 'generic_range', {'model': 'principalesfuentes', 'field': 'fuentes_ap', 'title': 'Numero de fuentes de ingreso agropecuario', 'serie': 'Num Fuentes', 'subtitle': 'fuentes', 'eje': 'Numero de fuentes','dondetoy2':'fuentesapingreso'}, name="fuentes_ap_generic_range"),
    url(r'rangos/fuentes-ap/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', {'model': 'principalesfuentes', 'serie': 'Num Fuentes', 'field': 'fuentes_ap', 'title': 'Numero de fuentes de ingreso agropecuario', 'subtitle': 'fuentes', 'eje': 'Numero de fuentes','dondetoy2':'fuentesapingreso'}, name="fuentes_ap_generic_range"),
    #fuentes no ap
    url(r'rangos/fuentes-no-ap/$', 'generic_range', {'model': 'principalesfuentes', 'field': 'fuentes_no_ap', 'serie': 'Num Fuentes', 'title': 'Numero de fuentes de ingreso agropecuario', 'subtitle': 'fuentes', 'eje': 'Numero de fuentes','dondetoy2':'fuentesnoapingreso'}, name="fuentes_no_ap_generic_range"),
    url(r'rangos/fuentes-no-ap/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', {'model': 'principalesfuentes', 'field': 'fuentes_no_ap', 'title': 'Numero de fuentes de ingreso agropecuario', 'subtitle': 'fuentes', 'eje': 'Numero de fuentes','dondetoy2':'fuentesnoapingreso'}, name="fuentes_no_ap_generic_range"),
)
