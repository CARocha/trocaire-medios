# -*- coding: utf-8 -*-

from django.db import models
from trocaire.medios.models import *

class Inmigracion(models.Model):
    inmigra = models.IntegerField('Inmigración', choices=CHOICE_INMIGRACION)
    mujer = models.IntegerField('Mujer Cantidad', default=0)
    hombre = models.IntegerField('Hombre Cantidad', default=0)
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "Inmigración"
        
class Codigo(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Codigo de porque no estudian"
        
class AccesoEscuela(models.Model):
    acceso = models.IntegerField('Acceso a la escuela', choices=CHOICE_ACCESO)
    fem_estudia = models.IntegerField(verbose_name='Femenino estudia')
    fem_no_estudia = models.IntegerField(verbose_name="Femenino no estudia")
    mas_estudia = models.IntegerField(verbose_name="Masculino estudia")
    mas_no_estudia = models.IntegerField(verbose_name="Masculino no estudia")
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "ACCESO A LA ESCUELA. Niñas/Ninos en la escuela"

CHOICE_NO_ESTUDIA = (
                        (1, '22. Razón principal porque no estudia.'),
                        (2, '24. Razón principal porque no estudian')
                    )

class RazonesNoEstudia(models.Model):
     acceso = models.IntegerField('Acceso a la escuela', choices=CHOICE_NO_ESTUDIA)
     fem_no_estudia = models.ForeignKey(Codigo, verbose_name="Femenino no estudia", related_name="Niñas No estudian")
     mas_no_estudia = models.ForeignKey(Codigo, verbose_name="Masculino no estudia", related_name="Niños No estudian")
     encuesta = models.ForeignKey(Encuesta)
     
     class Meta:
           verbose_name_plural = "Razones porque NO estudia los Niños/as"

# Parte del agua
class Abastece(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre
        
class Agua(models.Model):
    sistema = models.ForeignKey(Abastece, verbose_name='25. Sistema de agua de consumo humano que lo abastece')
    calidad = models.IntegerField('26. Calidad del agua que consume. ¿viene clorada?', choices=CHOICE_CALIDAD)
    clorada = models.IntegerField('27. Si no viene clorada ¿le da usted tratamiento?', choices=CHOICE_CLORADA)
    tiene = models.IntegerField('28. Tiene agua todo los dias en verano', choices=CHOICE_SINO)
    tiempo = models.IntegerField('29. Cuánto tiempo diario le toma traer el agua en verano', choices=CHOICE_TIEMPO)
    techo = models.IntegerField('30. Materiales del techo', choices=CHOICE_TECHO)
    piso = models.IntegerField('31. Materiales del piso', choices=CHOICE_PISO)
    paredes = models.IntegerField('32. Materiales en las paredes', choices=CHOICE_PAREDES)
    servicio = models.IntegerField('33. Servicio higiénico', choices=CHOICE_SERVICIO)
    cuartos = models.IntegerField('34. Número de cuartos en la vivienda (ambientes)')
    estado = models.IntegerField('35. La vivienda se encuentra en buen o mal estado', choices=CHOICE_ESTADO)
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "MATERIALES DE LA VIVIENDA"
