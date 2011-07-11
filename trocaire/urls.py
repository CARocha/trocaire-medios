from django.conf.urls.defaults import *
from trocaire.settings import *
from os import path as os_path

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^ingresos/', include('trocaire.ingresos.urls')),
    (r'^produccion/', include('trocaire.produccion.urls')),
    (r'^', include('trocaire.medios.urls')),
)

if DEBUG:
    urlpatterns += patterns('',
                            (r'^archivos/(.*)$', 'django.views.static.serve',
                            {'document_root': os_path.join(MEDIA_ROOT)}),
                           )
