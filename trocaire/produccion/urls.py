from django.conf.urls.defaults import *

urlpatterns = patterns('trocaire.produccion.views',
    url(r'rangos/(?P<modelo>\w+)/$', 'produccion_por_rango', name="produccion_por_rango"),
    url(r'rangos/(?P<modelo>\w+)/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'produccion_por_rango', name="produccion_por_rango"),
    #url(r'(?P<vista>[-\w]+)/$', '_get_view'),
)
