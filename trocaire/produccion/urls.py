from django.conf.urls.defaults import *

urlpatterns = patterns('trocaire.produccion.views',
    url(r'rangos/maiz/$', 'produccion_por_rango', {'modelo': 'cultivosperiodos', 'cultivos': [1,2] }, name="produccion_maiz"),
    url(r'rangos/maiz/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'produccion_por_rango',{'modelo': 'cultivosperiodos', 'cultivos': [1,2] },  name="produccion_maiz"),
    #frijol
    url(r'rangos/frijol/$', 'produccion_por_rango', {'modelo': 'cultivosperiodos', 'cultivos': [3] }, name="produccion_maiz"),
    url(r'rangos/frijol/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'produccion_por_rango',{'modelo': 'cultivosperiodos', 'cultivos': [3] },  name="produccion_maiz"),
    #cafe
    url(r'rangos/cafe/$', 'produccion_por_rango', {'modelo': 'cultivospermanentes', 'cultivos': [1] }, name="produccion_maiz"),
    url(r'rangos/cafe/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'produccion_por_rango',{'modelo': 'cultivospermanentes', 'cultivos': [1] },  name="produccion_maiz"),
    #cacao
    url(r'rangos/cacao/$', 'produccion_por_rango', {'modelo': 'cultivospermanentes', 'cultivos': [2] }, name="produccion_maiz"),
    url(r'rangos/cacao/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'produccion_por_rango',{'modelo': 'cultivospermanentes', 'cultivos': [2] },  name="produccion_maiz"),
    #numero bovino
    url(r'rangos/animales-bovino/$', 'generic_range', 
        {'model': 'ganadomayor', 'field': 'cantidad', 'extra_params': {'ganado__in': [1,2,3,4,5,6]}}, name="produccion_bovino"),
    url(r'rangos/animales-bovino/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', 
        {'model': 'ganadomayor', 'field': 'cantidad', 'extra_params': {'ganado__in': [1,2,3,4,5,6]}},  name="produccion_bovino"),
    #numero aves 
    url(r'rangos/animales-aves/$', 'generic_range', 
        {'model': 'ganadomayor', 'field': 'cantidad', 'extra_params': {'ganado': 7}}, name="produccion_aves"),
    url(r'rangos/animales-aves/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', 
        {'model': 'ganadomayor', 'field': 'cantidad', 'extra_params': {'ganado': 7}},  name="produccion_aves"),
    #numero cerdos 
    url(r'rangos/animales-cerdos/$', 'generic_range', 
        {'model': 'ganadomayor', 'field': 'cantidad', 'extra_params': {'ganado': 8}}, name="produccion_cerdos"),
    url(r'rangos/animales-cerdos/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', 
        {'model': 'ganadomayor', 'field': 'cantidad', 'extra_params': {'ganado': 8}},  name="produccion_cerdos"),
)
