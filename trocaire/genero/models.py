# -*- coding: utf-8 -*-

from django.db import models
from trocaire.medios.models import *

# Create your models here.

choice_genero = (
                    (1,'149. Asiste a las reuniones de la escuela'),
                    (2,'150. Lleva sus hijos e hijas al centro de salud'),
                    (3,'151. Cocina'),
                    (4,'152. Lava y plancha'),
                    (5,'153. Barre, limpia la casa'),
                    (6,'154. Atiende a sus hijas e hijos')
                    
                )
                
choice_genero_respuesta = (
                    (1,'Lo hace con frecuencia'),
                    (2,'Algunas veces'),
                    (3,'Muy poco o nunca lo hacen'),
                    (4,'No tiene niños/as')
                    
                )

class Genero(models.Model):
    responsabilidades = models.IntegerField(choices=choice_genero)
    respuesta = models.IntegerField(choices=choice_genero_respuesta)
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Con que frecuenca los hombre de la casa asumen responsabilidades"
        
choice_aspecto = (
                    (1,'155. Gastos mayores para la casa'),
                    (2,'156. Inversión agricola'),
                    (3,'157. Inversión en ganado mayor '),
                    (4,'158. Inversión en pequeños negocios'),
                    (5,'159. Venta de la producción agricola (sin patio)'),
                    (6,'160. venta de la producción pecuario (sin aves)')
                    
                )
                
choice_aspecto_respuesta = (
                    (1,'Hombre'),
                    (2,'Mujer'),
                    (3,'Ambos'),
                    (4,'No aplica')
                    
                )
                
                
class TomaDecicion(models.Model):
    aspectos = models.IntegerField(choices=choice_aspecto)
    respuesta = models.IntegerField(choices=choice_aspecto_respuesta)
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Quién toma la decisión final"
