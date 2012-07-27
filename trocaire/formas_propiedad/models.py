# -*- coding: utf-8 -*-
from django.db import models
from trocaire.medios.models import CHOICE_AREA, CHOICE_SINO, Encuesta 

class Tierra(models.Model):
    area = models.IntegerField('Área y propiedad en Manzanas', choices=CHOICE_AREA)
    mujer = models.FloatField('De la mujer')
    hombre = models.FloatField('Del hombre')
    ambos = models.FloatField('De ambos')
    encuesta = models.ForeignKey(Encuesta)
    #campos hipsters
    area_total = models.FloatField(editable=False, default=0)

    def save(self, *args, **kwargs):        
        self.area_total = self.mujer + self.hombre + self.ambos        
        super(Tierra, self).save(*args, **kwargs)

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
    conflicto = models.IntegerField('43. Su propiedad tiene conflicto con otras  personas que la reclaman como propia o han invadido',
            choices=CHOICE_SINO, null=True, blank=True)
    ciclo = models.ManyToManyField(Ciclo, 
            verbose_name='44. ciclo agricola de un año. Para sus actividades agropecuarias alquilo, hizo mediería o le prestaron.')
    zonas = models.ManyToManyField(Riegos,verbose_name="45. En su propiedad y en la casa. ¿Hay zonas de riesgo?",
            help_text="Enumerar los 3 mas importantes", null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "Producción"
