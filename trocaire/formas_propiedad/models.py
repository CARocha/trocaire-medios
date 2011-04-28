# -*- coding: utf-8 -*-

from django.db import models
from trocaire.medios import *

# Create your models here.

class Tierra(models.Model):
    area = models.IntegerField('Área y propiedad en Manzanas', choices=CHOICE_AREA)
    mujer = models.IntegerField('De la mujer')
    hombre = models.IntegerField('Del hombre')
    ambos = models.IntegerField('De ambos')
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "PROPIEDAD DE LA TIERRA"

class Ciclo(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

class Riegos(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
                
class Propiedad(models.Model):
    conflicto = models.IntegerField('43. Su propiedad tiene conflicto con otras  personas que la reclaman como propia o han invadido', choices=CHOICE_SINO)
    ciclo = models.ManyToManyField(Ciclo,verbose_name='44. ciclo agricola de un año. Para sus actividades agropecuarias alquilo, hizo mediería o le prestaron.')
    zonas = models.ManyToManyField(Riegos,verbose_name="45. En su propiedad y en la casa. ¿Hay zonas de riesgo?", help_text="Enumerar los 3 mas importantes")
