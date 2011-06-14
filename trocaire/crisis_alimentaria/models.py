# -*- coding: utf-8 -*-
from django.db import models
from trocaire.medios.models import CHOICE_SINO, Encuesta 

class EstrategiaCrisis(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre
        
class Crisis(models.Model):
    escases = models.IntegerField('139. Podria decirnos si su familia ha enfrentado escases de alimentos', 
                                    choices=CHOICE_SINO)
    causa = models.CharField(max_length=200, 
                   verbose_name="140. Podria decirnos cual fue la causa principal de la crisis de comida que vivieron")
    enfrentar = models.ManyToManyField(EstrategiaCrisis, 
                verbose_name="141. Si tuvieron crisis podria decirnos, como hicieron para enfrentarla")
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "Crisis sobre seguridad alimentaria"
        
# ACCESO A CREDITO
class Credito(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de creditos"
              
class AccesoCredito(models.Model):
    hombre = models.ManyToManyField(Credito, related_name="Hombre")
    mujer =  models.ManyToManyField(Credito, related_name="Mujer")
    otro_hombre = models.ManyToManyField(Credito, 
            verbose_name='Otro hombre que vive en el hogar', related_name="Hombre vive")
    otra_mujer = models.ManyToManyField(Credito, 
            verbose_name='Otra mujer que vive en el hogar', related_name="Mujer vive")
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "142. Podria decirnos cuál es su principal fuente de crédito (matrimonio)"         
