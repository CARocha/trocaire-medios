# -*- coding: utf-8 -*-

from django.db import models
from trocaire.medios.models import *

# Create your models here.

choice_ciudadana = (
                    (1,'143. CPC'),
                    (2,'144. Asamblea comunitaria')
                    
                   )
choice_ciudadana_respuesta = (
                                (1,'Son muy beneficioso'),
                                (2,'Hacen algunas cosas'),
                                (3,'No hacen nada'),
                                (4,'NS NR')
                    
                              ) 
               
choice_ciudadana_dos = (
                    (1,'145. CPC'),
                    (2,'146. Asamblea comunitaria')
                   
                       )
               
choice_ciudadana_tres = (
                    (1,'147. CPC'),
                    (2,'148. Asamblea comunitaria')
                    
               )

choice_ciudadana_tres_respuesta = (
                    (1,'Lo hacen con frecuencia'),
                    (2,'Algunas veces'),
                    (3,'Muy poco o nunca lo hacen'),
                    (4,'No aplica. No participan')
                    
               )    

class Participacion(models.Model):
    organismo = models.IntegerField(choices=choice_ciudadana)
    respuesta = models.IntegerField(choices=choice_ciudadana_respuesta)
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Podria decirnos si esto organismo que le vamos a mencionar son muy beneficioso"

class ParticipacionCPC(models.Model):
    organismo = models.IntegerField(choices=choice_ciudadana_dos)
    hombre = models.IntegerField()
    mujer = models.IntegerField()
    ambos = models.IntegerField()
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Quien de la familia participa en los CPC y AC"
        
class Frecuencia(models.Model):
    organismo = models.IntegerField(choices=choice_ciudadana_tres)
    respuesta = models.IntegerField(choices=choice_ciudadana_tres_respuesta)
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Podria decirnos con que frecuencia participan en estas estructuras"       
