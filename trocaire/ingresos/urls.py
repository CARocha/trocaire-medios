from django.conf.urls.defaults import *

urlpatterns = patterns('trocaire.ingresos.views',
    url(r'(?P<vista>[-\w]+)/$', '_get_view'),
)
