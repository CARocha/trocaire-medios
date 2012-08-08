from django.conf.urls.defaults import *
from trocaire.settings import *
from os import path as os_path

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^ingresos/', include('trocaire.ingresos.urls')),
    (r'^produccion/', include('trocaire.produccion.urls')),
    (r'^propiedad/', include('trocaire.formas_propiedad.urls')),    
    (r'^', include('trocaire.medios.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
)

if DEBUG:
    urlpatterns += patterns('',
                            (r'^archivos/(.*)$', 'django.views.static.serve',
                            {'document_root': os_path.join(MEDIA_ROOT)}),
                           )
