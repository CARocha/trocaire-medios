# -*- coding: UTF-8 -*-
from django import forms

from trocaire.medios.models import *
from trocaire.familia.models import CHOICE_ESCOLARIDAD
from trocaire.genero.models import CHOICE_ASPECTO_RESPUESTA
from trocaire.lugar.models import *
from trocaire.ingresos.models import Fuentes

ANOS_CHOICES = ((2010,'2010'), (2011,'2011'),(2012,'2012'),(2013,'2013'),(2014,'2014'),(2015,'2015'))
DEPENDIENTES_CHOICE = ((1, u'Igual a 0'), (2, u'De 0.1 a 1.0'), (3, u'De 1.1 a 2.0'), (4, u'De 2.1 a 3.0'), (5, u'Más de 3.0'))
CREDITO_CHOICE = ((1, 'Si'), (2, 'No'))

class CustomChoiceField(forms.ChoiceField):

    def __init__(self, *args, **kwargs):
        super(CustomChoiceField, self).__init__(*args, **kwargs)
        self.choices.insert(0, (None , '--------'))

class ConsultarForm(forms.Form):
    fecha = CustomChoiceField(choices=ANOS_CHOICES)
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all().order_by('nombre'), 
                                          required=False, empty_label="Todos los Departamentos")
    municipio = forms.CharField(widget = forms.Select, required=False)
    comarca = forms.CharField(widget = forms.Select, required=False)
    contraparte = forms.ModelChoiceField(queryset=Contraparte.objects.all(), required=False)
    #escolaridad
    escolaridad_beneficiario = CustomChoiceField(choices=CHOICE_ESCOLARIDAD, required=False)
    escolaridad_conyugue = CustomChoiceField(choices=CHOICE_ESCOLARIDAD, required=False)
    #familia
    familia_beneficiario = CustomChoiceField(CHOICE_SEXO, required=False)     
    indice_dep = CustomChoiceField(choices=DEPENDIENTES_CHOICE, required=False)    
    #ingresos(ambos son rangos)
    ingresos_fuente = forms.ModelChoiceField(queryset=Fuentes.objects.all(), required=False)
    ingresos_total_max = forms.FloatField(required=False)
    ingresos_total_min = forms.FloatField(required=False)
    #credito
    credito_acceso = CustomChoiceField(choices=CREDITO_CHOICE, required=False, label=u'Acceso a crédito')
    #toma de desicion
    desicion_gasto_mayor = CustomChoiceField(choices=CHOICE_ASPECTO_RESPUESTA, required=False)
    desicion_inversion = CustomChoiceField(choices=CHOICE_ASPECTO_RESPUESTA, required=False)
    #finca
    #finca_area_total_max = forms.FloatField(required=False) #rango
    #finca_area_total_min = forms.FloatField(required=False) #rango
    #finca_num_vacas_max = forms.FloatField(required=False) #rango
    #finca_num_vacas_min = forms.FloatField(required=False) #rango
    #finca_riego = CustomChoiceField(choices=CHOICE_SINO, required=False)
    #finca_conssa= CustomChoiceField(choices=CHOICE_SINO, required=False)
    #finca_num_productos_max = forms.FloatField(required=False) #rango
    #finca_num_productos_min = forms.FloatField(required=False) #rango
    #magia
    next_url = forms.CharField(widget=forms.HiddenInput, required=False)
