# -*- coding: utf-8 -*-
from django.db import models
from trocaire.medios.models import Encuesta 

CHOICE_GENERO = (
                    (1,'149. Asiste a las reuniones de la escuela'),
                    (2,'150. Lleva sus hijos e hijas al centro de salud'),
                    (3,'151. Cocina'),
                    (4,'152. Lava y plancha'),
                    (5,'153. Barre, limpia la casa'),
                    (6,'154. Atiende a sus hijas e hijos')
                    
                )
                
CHOICE_GENERO_RESPUESTA = (
                    (1,'Lo hace con frecuencia'),
                    (2,'Algunas veces'),
                    (3,'Muy poco o nunca lo hacen'),
                    (4,'No tiene niños/as')
                    
                )

class Genero(models.Model):
    responsabilidades = models.IntegerField(choices=CHOICE_GENERO)
    respuesta = models.IntegerField(choices=CHOICE_GENERO_RESPUESTA)
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "Con que frecuenca los hombre de la casa asumen responsabilidades"
        
CHOICE_ASPECTO = (
                    (1,'155. Gastos mayores para la casa'),
                    (2,'156. Inversión agricola'),
                    (3,'157. Inversión en ganado mayor '),
                    (4,'158. Inversión en pequeños negocios'),
                    (5,'159. Venta de la producción agricola (sin patio)'),
                    (6,'160. venta de la producción pecuario (sin aves)')
                    
                 )
                
CHOICE_ASPECTO_RESPUESTA = (
                             (1,'Hombre'),
                             (2,'Mujer'),
                             (3,'Ambos'),
                             (4,'No aplica')
                           )
                
                
class TomaDecicion(models.Model):
    aspectos = models.IntegerField(choices=CHOICE_ASPECTO)
    respuesta = models.IntegerField(choices=CHOICE_ASPECTO_RESPUESTA)
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "Quién toma la decisión final"
