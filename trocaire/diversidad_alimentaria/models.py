# -*- coding: utf-8 -*-
from django.db import models
from trocaire.medios.models import CHOICE_SINO, Encuesta 

CHOICE_ALIMENTO = (
                    (1,'Granos'),
                    (2,'Féculas'),
                    (3,'Hortalizas y verduras'),
                    (4,'Frutas'),
                    (5,'Láctios y huevos'),
                    (6,'Carnes'),
                    (7,'Grasas y aceites'),
                    (8,'Otros')
               )
               
class Alimentos(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
               
class Diversidad(models.Model):
    alimento = models.ForeignKey(Alimentos)
    respuesta = models.IntegerField(choices=CHOICE_SINO)
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Diversidad Alimentaria"
