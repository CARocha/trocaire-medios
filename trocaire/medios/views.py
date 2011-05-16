
#importaciones de Django
from datetime import date
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.utils import simplejson
from django.db.models import Sum, Count, Avg
from django.core.exceptions import ViewDoesNotExist

#importaciones de los models
from trocaire.calidad_vida.models import *
from trocaire.crisis_alimentaria.models import *
from trocaire.diversidad_alimentaria.models import *
from trocaire.familia.models import *
from trocaire.formas_propiedad.models import *
from trocaire.genero.models import * 
from trocaire.ingresos.models import *
from trocaire.lugar.models import *
from trocaire.medios.models import *
from trocaire.participacion_ciudadana.models import *
from trocaire.produccion.models import *
from trocaire.tecnologia.models import *


# Create your views here.

def index(request, template_name="index.html"):
               
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
    
    
