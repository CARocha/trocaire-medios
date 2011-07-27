from django.conf.urls.defaults import *

urlpatterns = patterns('trocaire.ingresos.views',
    #url(r'rangos/$', 'ingreso_por_rango', name="ingreso_por_rango"),
    #url(r'rangos/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'ingreso_por_rango', name="ingreso_por_rango"),
    #url(r'rangos/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'ingreso_por_rango', name="ingreso_por_rango"),
    url(r'rangos/$', 'generic_range', {'model': 'totalingreso', 'field': 'total'}, name="ingresos_generic_range"),
    url(r'rangos/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', {'model':'totalingreso', 'field': 'total'}, name="ingresos_generic_range"),
    url(r'rangos/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', {'model':'totalingreso', 'field': 'total'}, name="ingresos_generic_range"),
    #ingreso ganado
    url(r'rangos/ganado/$', 'generic_range', {'model': 'ingresoganado', 'field': 'total'}, name="ingresos_generic_range"),
    url(r'rangos/ganado/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', {'model': 'ingresoganado', 'field': 'total'}, name="ingresos_generic_range"),
    url(r'rangos/ganado/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', {'model': 'ingresoganado', 'field': 'total'}, name="ingresos_generic_range"),
    #fuentes ap
    url(r'rangos/fuentes-ap/$', 'generic_range', {'model': 'principalesfuentes', 'field': 'fuentes_ap'}, name="fuentes_ap_generic_range"),
    url(r'rangos/fuentes-ap/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', {'model': 'principalesfuentes', 'field': 'fuentes_ap'}, name="fuentes_ap_generic_range"),
    #fuentes no ap
    url(r'rangos/fuentes-no-ap/$', 'generic_range', {'model': 'principalesfuentes', 'field': 'fuentes_no_ap'}, name="fuentes_no_ap_generic_range"),
    url(r'rangos/fuentes-no-ap/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', {'model': 'principalesfuentes', 'field': 'fuentes_no_ap'}, name="fuentes_no_ap_generic_range"),
)
