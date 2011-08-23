from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('trocaire.medios.views',
    url(r'^$', 'index'),
    url(r'^consultar/$', 'consultar', name="consultar"),
    url(r'^consultarsimple/$', 'consultarsimple', name="consultar"),
    #para extrar los lugares
    url(r'^consultar/ajax/municipio/(?P<departamento>\d+)/$', 'get_municipios'),
    url(r'^consultar/ajax/comarca/(?P<municipio>\d+)/$', 'get_comarca'),
    url(r'^encuestas/generales/$', 'indicadores', name="indicadores"),
    url(r'^encuestas/salidas-sencillas/$', direct_to_template, {'template': 'foo_index.html'}, name='salidas-sencillas'),
    url(r'^encuestas/datos-x-sexo/$', 'datos_sexo', name="datos_sexo"),
    url(r'^encuestas/agua-clorada/$', 'agua_clorada', name="agua_clorada"),
    url(r'^encuestas/gastan-horas/$', 'gastan_horas', name="gastan_horas"),
    url(r'^encuestas/familias-practicas/$', 'familias_practicas', name="familias_practicas"),
    #url(r'^encuestas/promedio-suelo/$', 'promedio_suelo', name="promedio_suelo"),
    url(r'^encuestas/dependencia/$', 'dependencia', name="dependencia"),
    url(r'^encuestas/acceso-tierra/$', 'acceso_tierra', name="acceso_tierra"),
    url(r'^encuestas/acceso-agua/$', 'acceso_agua', name="acceso_agua"),
    url(r'^encuestas/hombre-responsable/$', 'hombre_responsable', name="hombre_responsable"),
    url(r'^encuestas/mujer-decicion/$', 'mujeres_decisiones', name="mujeres_decisiones"),
    url(r'^encuestas/sexo-beneficiario/$', 'sexo_beneficiario', name="sexo-beneficiario"),
    url(r'^encuestas/escolaridad/$', 'escolaridad', name="escolaridad"),
    url(r'^encuestas/credito/$', 'credito', name="credito"),
    url(r'^encuestas/participacion/$', 'participacion', name="participacion"),
    url(r'^encuestas/ingreso-agropecuario/$', 'ingreso_agropecuario', name="ingreso_agropecuario"),
    url(r'^encuestas/ingreso-familiar/$', 'ingreso_familiar', name="ingreso_familiar"),
    url(r'^encuestas/abastecimiento/$', 'abastecimiento', name="abastecimiento"),
)
