# -*- coding: utf-8 -*-

from django.db import models
from trocaire.medios.models import CHOICE_SEXO, CHOICE_JEFE, CHOICE_RELACION, \
        CHOICE_SEXO_JEFE, CHOICE_DESCRIPCION, CHOICE_CIVIL, Encuesta 

class Composicion(models.Model):
    ''' Modelo sobre la composicion de la 
        familas
    '''
    sexo = models.IntegerField('1. Sexo del beneficiario/a', choices=CHOICE_SEXO)
    edad = models.IntegerField('2. Edad del beneficiario/a')
    estado = models.IntegerField('3. Estado Civil', choices=CHOICE_CIVIL)
    beneficio = models.IntegerField('4. El o la beneficiario/a es el jefe de familas', choices=CHOICE_JEFE)
    relacion = models.IntegerField('5. Si no es jefe/a de famila... cuál es su relación con el jefe de Familia',
                                    choices=CHOICE_RELACION)
    sexo_jefe = models.IntegerField('6. Si no es jefe/a... Cuál es el sexo del jefe de familia',
                                    choices=CHOICE_SEXO_JEFE)
    num_familia = models.IntegerField('7. Número de familas que viven en la vivienda')
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "COMPOSICIÓN DE LA FAMILIA" 

class Descripcion(models.Model):
    descripcion = models.IntegerField('Descripción', choices=CHOICE_DESCRIPCION)
    femenino = models.IntegerField()
    masculino = models.IntegerField()
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "DESCRIPCIÓN"

CHOICE_ESCOLARIDAD = (
                            (1, "1) Analfabeto o hasta 3er grado"),
                            (2, "2) 4 y hasta 6 grado de Primaria"),
                            (3, "3) Algo de Secundaria"),
                            (4, "4) Bachiller o Técnico Medio"),
                            (5, "5) Universidad o Profesional Universitario"),
                            (6, "6) No aplica")
                     )
        
class Escolaridad(models.Model):
    beneficia = models.IntegerField(choices=CHOICE_ESCOLARIDAD, verbose_name="13. Beneficiaria/o")
    conyugue = models.IntegerField(choices=CHOICE_ESCOLARIDAD, verbose_name="14. Conyugue")
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "ESCOLARIDAD"
