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
)
