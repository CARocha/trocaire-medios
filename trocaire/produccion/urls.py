# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('trocaire.produccion.views',
    url(r'rangos/maiz/$', 'produccion_por_rango', {'modelo': 'cultivosperiodos', 'cultivos': [1,2], 'dondetoy2':'maizprod' }, name="produccion_maiz"),
    url(r'rangos/maiz/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'produccion_por_rango',{'modelo': 'cultivosperiodos', 'cultivos': [1,2],'dondetoy2':'maizprod' },  name="produccion_maiz"),
    #frijol
    url(r'rangos/frijol/$', 'produccion_por_rango', {'modelo': 'cultivosperiodos', 'cultivos': [3], 'dondetoy2':'frijolprod' }, name="produccion_frijol"),
    url(r'rangos/frijol/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'produccion_por_rango',{'modelo': 'cultivosperiodos', 'cultivos': [3],'dondetoy2':'frijolprod' },  name="produccion_frijol"),
    #cafe
    url(r'rangos/cafe/$', 'produccion_por_rango', {'modelo': 'cultivospermanentes', 'cultivos': [1],'dondetoy2':'cafeprod' }, name="produccion_cafe"),
    url(r'rangos/cafe/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'produccion_por_rango',{'modelo': 'cultivospermanentes', 'cultivos': [1],'dondetoy2':'cafeprod'  },  name="produccion_cafe"),
    #cacao
    url(r'rangos/cacao/$', 'produccion_por_rango', {'modelo': 'cultivospermanentes', 'cultivos': [2],'dondetoy2':'cacaoprod'  }, name="produccion_cacao"),
    url(r'rangos/cacao/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'produccion_por_rango',{'modelo': 'cultivospermanentes', 'cultivos': [2],'dondetoy2':'cacaoprod'  },  name="produccion_cacao"),
    #numero bovino
    url(r'rangos/animales-bovino/$', 'generic_range', 
        {'dondetoy2':'animalesprod','title': 'Numero de bovinos', 'subtitle': 'algo', 'eje': 'bovinos', 'serie': 'bovinos','model': 'ganadomayor', 'field': 'cantidad', 'extra_params': {'ganado__in': [1,2,3,4,5,6]}}, name="produccion_bovino"),
    url(r'rangos/animales-bovino/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', 
        {'dondetoy2':'animalesprod','title': 'Numero de  bovinos', 'subtitle': 'algo', 'eje': 'bovinos', 'serie': 'bovinos','model': 'ganadomayor', 'field': 'cantidad', 'extra_params': {'ganado__in': [1,2,3,4,5,6]}},  name="produccion_bovino"),
    #numero aves 
    url(r'rangos/animales-aves/$', 'generic_range', 
        {'dondetoy2':'avesprod','title': 'Numero de Aves', 'subtitle': 'algo', 'eje': 'aves', 'serie': 'aves','model': 'ganadomayor', 'field': 'cantidad', 'extra_params': {'ganado': 7}}, name="produccion_aves"),
    url(r'rangos/animales-aves/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', 
        {'dondetoy2':'avesprod','title': 'Numero de Aves', 'subtitle': 'algo', 'eje': 'aves', 'serie': 'aves','model': 'ganadomayor', 'field': 'cantidad', 'extra_params': {'ganado': 7}},  name="produccion_aves"),
    #productividd maiz 
    url(r'rangos/productividad-maiz/$', 'generic_range', 
        {'dondetoy2':'maizproductividad','title': 'Productividad Maiz', 'subtitle': '', 'eje': 'número de familias', 'serie': 'productividad','model': 'cultivosperiodos', 'field': 'productividad', 'extra_params': {'cultivos__in': [1,2]}}, name="productividad_maiz"),
    url(r'rangos/productividad-maiz/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', 
        {'dondetoy2':'maizproductividad','title': 'Productividad Maiz', 'subtitle': '', 'eje': 'número de familias', 'serie': 'productividad','model': 'cultivosperiodos', 'field': 'productividad', 'extra_params': {'cultivos__in': [1,2]}},  name="productividad_maiz"),
    #productividd frijol 
    url(r'rangos/productividad-frijol/$', 'generic_range', 
        {'dondetoy2':'frijolproductividad','title': 'Productividad Frijol', 'subtitle': '', 'eje': 'número de familias', 'serie': 'productividad','model': 'cultivosperiodos', 'field': 'productividad', 'extra_params': {'cultivos': 3}}, name="productividad_frijol"),
    url(r'rangos/productividad-frijol/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', 
        {'dondetoy2':'frijolproductividad','title': 'Productividad Frijol', 'subtitle': '', 'eje': 'número de familias', 'serie': 'productividad','model': 'cultivosperiodos', 'field': 'productividad', 'extra_params': {'cultivos': 3}},  name="productividad_frijol"),
    #productividad cafe 
    url(r'rangos/productividad-cafe/$', 'generic_range', 
        {'dondetoy2':'cafeproductividad','title': 'Productividad Cafe', 'subtitle': '', 'eje': 'número de familias', 'serie': 'productividad','model': 'cultivospermanentes', 'field': 'productividad', 'extra_params': {'cultivos': 1}}, name="productividad_cafe"),
    url(r'rangos/productividad-cafe/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', 
        {'dondetoy2':'cafeproductividad','title': 'Productividad Cafe', 'subtitle': '', 'eje': 'número de familias', 'serie': 'productividad','model': 'cultivospermanentes', 'field': 'productividad', 'extra_params': {'cultivos': 1}},  name="productividad_cafe"),
    #productividad cacao 
    url(r'rangos/productividad-cacao/$', 'generic_range', 
        {'dondetoy2':'cacaoproductividad','title': 'Productividad Cacao', 'subtitle': '', 'eje': 'número de familias', 'serie': 'productividad','model': 'cultivospermanentes', 'field': 'productividad', 'extra_params': {'cultivos': 2}}, name="productividad_cacao"),
    url(r'rangos/productividad-cacao/(?P<maximo>\d+)/(?P<minimo>\d+)/(?P<separaciones>\d+)/$', 'generic_range', 
        {'dondetoy2':'cacaoproductividad','title': 'Productividad Cacao', 'subtitle': '', 'eje': 'número de familias', 'serie': 'productividad', 'model': 'cultivospermanentes', 'field': 'productividad', 'extra_params': {'cultivos': 2}},  name="productividad_cacao"),
)
