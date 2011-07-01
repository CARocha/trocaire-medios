# -*- coding: UTF-8 -*-

from django import forms
from trocaire.medios.models import *
from trocaire.lugar.models import *

ANOS_CHOICES = ((2011,'2011'),(2012,'2012'),(2013,'2013'),(2014,'2014'),(2015,'2015'))
    
class ConsultarForm(forms.Form):
    fecha = forms.ChoiceField(choices=ANOS_CHOICES)
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all().order_by('nombre'), 
                                          required=False, empty_label="Todos los Departamentos")
    municipio = forms.CharField(widget = forms.Select, required=False)
    comarca = forms.CharField(widget = forms.Select, required=False)
    contraparte = forms.ModelChoiceField(queryset=Contraparte.objects.all(), required=False)
    next_url = forms.CharField(widget = forms.HiddenInput, required=False)
