# -*- coding: UTF-8 -*-
from django import forms

from trocaire.medios.models import *
from trocaire.familia.models import CHOICE_ESCOLARIDAD
from trocaire.genero.models import CHOICE_ASPECTO_RESPUESTA
from trocaire.lugar.models import *
from trocaire.ingresos.models import Fuentes

ANOS_CHOICES = ((2011,'2011'),(2012,'2012'),(2013,'2013'),(2014,'2014'),(2015,'2015'))

class ConsultarForm(forms.Form):
    #fecha = forms.ChoiceField(choices=ANOS_CHOICES)
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all().order_by('nombre'), 
                                          required=False, empty_label="Todos los Departamentos")
    municipio = forms.CharField(widget = forms.Select, required=False)
    comarca = forms.CharField(widget = forms.Select, required=False)
    contraparte = forms.ModelChoiceField(queryset=Contraparte.objects.all(), required=False)
    #escolaridad
    escolaridad_beneficiario = forms.ChoiceField(choices=CHOICE_ESCOLARIDAD, required=False)
    escolaridad_conyugue = forms.ChoiceField(choices=CHOICE_ESCOLARIDAD, required=False)
    #familia
    familia_beneficiario = forms.ChoiceField(CHOICE_SEXO, required=False)
    familia_dependientes = forms.IntegerField(min_value=0, required=False)
    #ingresos(ambos son rangos)
    ingresos_fuente = forms.ModelChoiceField(queryset=Fuentes.objects.all(), required=False)
    ingresos_total = forms.FloatField(required=False)
    #credito
    credito_acceso = forms.ChoiceField(choices=CHOICE_SINO, required=False)
    #toma de desicion
    desicion_gasto_mayor = forms.ChoiceField(choices=CHOICE_ASPECTO_RESPUESTA, required=False)
    desicion_inversion = forms.ChoiceField(choices=CHOICE_ASPECTO_RESPUESTA, required=False)
    #finca
    finca_area_total = forms.FloatField(required=False) #rango
    finca_num_vacas= forms.FloatField(required=False) #rango
    finca_riego = forms.ChoiceField(choices=CHOICE_SINO, required=False)
    finca_conssa= forms.ChoiceField(choices=CHOICE_SINO, required=False)
    finca_num_productos= forms.FloatField(required=False) #rango
    #magia
    next_url = forms.CharField(widget=forms.HiddenInput, required=False)
