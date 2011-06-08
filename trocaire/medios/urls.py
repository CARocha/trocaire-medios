import os
from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('trocaire.medios.views',
    (r'^$', 'index'),
    (r'^ingreso/(?P<vista>[-\w]+)/$', '_get_view'),
)
