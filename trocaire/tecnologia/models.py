# -*- coding: utf-8 -*-

from django.db import models
from trocaire.medios.models import *

# Create your models here.

choice_riego = (
                    (1,'No tiene'),
                    (2,'Aspersión'),
                    (3,'Goteo'),
                    (4,'Gravedad'),
                    (5,'Otro')
               )
               
class Riego(models.Model):
    respuesta = models.IntegerField(choices=choice_riego)
    area = models.FloatField('Área regadas', help_text="en manzanas")
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "123. Tiene riego (Área regada en manzana)"
        
choice_CSA = (
                    (1,'No tiene'),
                    (2,'Granos y hortalizas'),
                    (3,'Anuales'),
                    (4,'Permanentes'),
                    (5,'Pastos'),
                    (6,'Área total')
               )
               
class AreaProtegida(models.Model):
    respuesta = models.IntegerField(choices=choice_CSA)
    cantidad = models.FloatField('Cantidad protegida', help_text="en manzanas")
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "124. Área protegida con obras de CSA (En manzana)"
        
choice_tecnologias = (
                    (1,'125. Fertilizo con urea y completo'),
                    (2,'126. Protegió contra plagas, enfermedades con agroquimico. O utilizo de herbicidas'),
                    (3,'127. Tiene áreas fertilizadas solamente con abonos orgánicos'),
                    (4,'128. Tiene áreas protegidas contra plagas y enfermedades solamente con insecticidas, fungicidas y plaguicidas orgánicos')
               
                    )
                    
class UsoTecnologia(models.Model):
    tecnologia = models.IntegerField(choices=choice_tecnologias)
    granos = models.IntegerField('Granos y hortalizas', choices=CHOICE_SINO)
    anuales = models.IntegerField('Granos y hortalizas', choices=CHOICE_SINO)
    permanentes = models.IntegerField('Granos y hortalizas', choices=CHOICE_SINO)
    pastos = models.IntegerField('Granos y hortalizas', choices=CHOICE_SINO)
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Tecnologia utilizada en la producción agropecuaria"
        
choice_maiz = (
                    (1,'Maíz criollo'),
                    (2,'Maíz mejorado'),
                    (3,'Otra'),
                    (4,'No sembró Maíz')
                    
               )
choice_frijol = (
                    (1,'Frijol criollo'),
                    (2,'Frijol mejorado'),
                    (3,'Otra'),
                    (4,'No sembró Frijol')
                   
               )
               
class Semilla(models.Model):
    maiz = models.IntegerField('Maíz', choices=choice_maiz)
    frijol = models.IntegerField(choices=choice_frijol)
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "129. Cuál es el principal tipo de semilla que utilizó para sembrar Maíz y Frijol"       
