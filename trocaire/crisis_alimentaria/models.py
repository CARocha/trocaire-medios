# -*- coding: utf-8 -*-

from django.db import models
from trocaire.medios.models import *

# Create your models here.

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

choice_credito = (
                    (1,'1. No tiene. No recibe credito'),
                    (2,'2. Banca tradicional, micro-financiera'),
                    (3,'3. Cooperativa, proyectos, ONG'),
                    (4,'4. Banquito comunal'),
                    (5,'5. Comerciante, pretamista'),
                    (6,'6. Otro')
               )  
               
class AccesoCredito(models.Model):
    hombre = models.IntegerField(choices=choice_credito)
    mujer =  models.IntegerField(choices=choice_credito)
    otro_hombre = models.IntegerField('Otro hombre que vive en el hogar', choices=choice_credito)
    otra_mujer = models.IntegerField('Otra mujer que vive en el hogar', choices=choice_credito)
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "142. Podria decirnos cuál es su principal fuente de crédito (matrimonio)"         
