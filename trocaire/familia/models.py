# -*- coding: utf-8 -*-

from django.db import models
from trocaire.medios import *

# Create your models here.

class Composicion(models.Model):
    ''' Modelo sobre la composicion de la 
        familas
    '''
    sexo = models.IntegerField('1. Sexo del beneficiario/a', choices=CHOICE_SEXO)
    edad = models.IntegerField('2. Edad del beneficiario/a')
    estado = models.IntegerField('3. Estado Civil', choices=CHOICE_ESTADO)
    beneficio = models.IntegerField('4. El o la beneficiario/a es el jefe de familas', choices=CHOICE_JEFE)
    relacion = models.IntegerField('5. Si no es jefe/a de famila... cuál es su relacion con el jefe de Familia',
                                    choices=CHOICE_RELACION)
    sexo_jefe = models.IntegerField('6. Si no es jefe/a... Cuál es el sexo del jefe de familia',
                                    choices=CHOICE_SEXO_JEFE)
    num_familia = models.IntegerField('7. Número de familas que viven en la vivienda')
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "COMPOSICIÓN DE LA FAMILIA"
        
class Descripcion(models.Model):
    descripcion = models.IntegerField('Descripción', choices=)
    femenino = models.IntegerField()
    masculino = models.IntegerField()
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "DESCRIPCIÓN"
        
class Escolaridad(models.Model):
    beneficia = models.IntegerField('13. Beneficiaria/o')
    conyugue = models.IntegerField('14. Conyugue')
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "ESCOLARIDAD"
