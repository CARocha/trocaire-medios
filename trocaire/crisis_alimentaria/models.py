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
                   verbose_name="140. Podria decirnos cual fue la causa principal de la crisis de comida que vivieron",
                   null=True, blank=True)
    enfrentar = models.ManyToManyField(EstrategiaCrisis, 
                verbose_name="141. Si tuvieron crisis podria decirnos, como hicieron para enfrentarla",
                null=True, blank=True)
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

def _set_encuesta_credito(id):    
    #lazy function to check if any elements of list is in list2
    _list_in_list = lambda foo, meh: any(x in meh for x in foo)
    foo = [1, 7]
    obj = AccesoCredito.objects.get(id=id)
    hombre_l = obj.hombre.all().values_list('id', flat=True)
    print '--------Hombre credito'
    print hombre_l               
    mujer_l = obj.mujer.all().values_list('id', flat=True)  
    print '--------Mujer credito'
    print mujer_l
         
    #chequear si algun valor de foo (no tiene y no aplica) esta en en hombre o mujer             
    if _list_in_list(foo, hombre_l) and _list_in_list(foo, mujer_l):
        obj.encuesta.credito = 2            
    else:
        obj.encuesta.credito = 1
    
    #guardar encuesta con dato de credito
    obj.encuesta.save()
          
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
        
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

@receiver(m2m_changed, sender=AccesoCredito.mujer.through)
def create_credito_callback(sender, **kwargs):    
    instance = kwargs['instance']
    if kwargs['action'] == 'post_add':
        _set_encuesta_credito(instance.id)
