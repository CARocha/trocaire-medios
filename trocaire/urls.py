from django.conf.urls.defaults import *
from trocaire.settings import *
from os import path as os_path

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('trocaire.medios.urls')),
    (r'^ingresos/', include('trocaire.ingresos.urls')),
    (r'^admin/', include(admin.site.urls)),
)

if DEBUG:
    urlpatterns += patterns('',
                            (r'^archivos/(.*)$', 'django.views.static.serve',
                            {'document_root': os_path.join(MEDIA_ROOT)}),
                           )
