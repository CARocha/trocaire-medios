# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request, template_name="index.html"):
               
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
