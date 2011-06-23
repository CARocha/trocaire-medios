from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('trocaire.medios.views',
    (r'^$', 'index'),
    (r'^consultar/$', 'consultar'),
    #para extrar los lugares
    (r'^consultar/ajax/municipio/(?P<departamento>\d+)/$', 'get_municipios'),
    (r'^consultar/ajax/comarca/(?P<municipio>\d+)/$', 'get_comarca'),
)
