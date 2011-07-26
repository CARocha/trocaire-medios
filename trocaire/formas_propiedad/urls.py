from django.conf.urls.defaults import *

urlpatterns = patterns('trocaire.formas_propiedad.views',
    url(r'rangos/area-finca/$', 'generic_range', 
        {'model': 'tierra', 'field': 'area_total', 'extra_params': {'area': 1}}, name="formas_propiedad_area_total"),
    url(r'rangos/area-finca/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', 
        {'model': 'tierra', 'field': 'area_total', 'extra_params': {'area': 1}},  name="formas_propiedad_area_total"),
)
