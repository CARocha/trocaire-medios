from django.conf.urls.defaults import *

urlpatterns = patterns('trocaire.ingresos.views',
    url(r'rangos/$', 'ingreso_por_rango'),
    url(r'rangos/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'ingreso_por_rango'),
    #url(r'(?P<vista>[-\w]+)/$', '_get_view'),
)
