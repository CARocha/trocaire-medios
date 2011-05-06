# -*- coding: utf-8 -*-

from django.db import models
from trocaire.medios.models import *

# Create your models here.

class CPeriodos(models.Model):
    nombre = models.CharField(max_length=200)
    unidad = models.CharField(max_length=6)
    def __unicode__(self):
        return self.nombre
        
class CPermanentes(models.Model):
    nombre = models.CharField(max_length=200)
    unidad = models.CharField(max_length=6)
    def __unicode__(self):
        return self.nombre
        
class CAnuales(models.Model):
    nombre = models.CharField(max_length=200)
    unidad = models.CharField(max_length=6)
    def __unicode__(self):
        return self.nombre
        
class CHortalizas(models.Model):
    nombre = models.CharField(max_length=200)
    unidad = models.CharField(max_length=6)
    def __unicode__(self):
        return self.nombre
        
class CultivosPeriodos(models.Model):
    cultivos = models.ForeignKey(CPeriodos, verbose_name="Cultivos de periodos")
    primera = models.IntegerField('Ciclo de Primera')
    postrera = models.IntegerField('Ciclo de Postrera')
    apante = models.IntegerField('Ciclo de Apante')
    p_primera = models.IntegerField('Producción del ciclo de Primera')
    p_postrera = models.IntegerField('Producción del ciclo de postrera')
    p_apante = models.IntegerField('Producción del ciclo de apante')
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Cultivos de Periodos"
        
class CultivosPermanentes(models.Model):
    cultivos = models.ForeignKey(CPermanentes, verbose_name="Cultivos Permanentes")
    manzana = models.FloatField(verbose_name="Área Manzanas")
    produccion = models.FloatField(verbose_name="Producción")
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Cultivos Permanentes"
        
class CultivosAnuales(models.Model):
    cultivos = models.ForeignKey(CAnuales, verbose_name="Cultivos anuales")
    manzana = models.FloatField(verbose_name="Área Manzanas")
    produccion = models.FloatField(verbose_name="Producción")
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Cultivos Anuales"
        
class Hortalizas(models.Model):
    cultivos = models.ForeignKey(CHortalizas, verbose_name="Hortalizas")
    manzana = models.FloatField(verbose_name="Área Manzanas")
    produccion = models.FloatField(verbose_name="Producción")
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Cultivos Anuales"
        
class ConsumoDiario(models.Model):
    maiz = models.IntegerField('76. Maiz')
    frijol = models.IntegerField('77. Frijol')
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Consumo diario de maíz y frijol.Libras consumidas por familia"
        
class Limitaciones(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Código de las principal limitación"
        
class PrincipalLimitacion(models.Model):
    opcion1 = models.ForeignKey(Limitaciones, verbose_name="Opción 1", related_name="uno")
    opcion2 = models.ForeignKey(Limitaciones, verbose_name="Opción 2", related_name="dos")
    opcion3 = models.ForeignKey(Limitaciones, verbose_name="Opción 3", related_name="tres")
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "78. Para usted... cuál es la pricipal limitación para aumentar su producción"
        
class PatioCultivada(models.Model):
    invierno = models.FloatField('79. Invierno')
    verano = models.FloatField('80. Verano')
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Área del patio cultivada en manzanas"
        
class Arboles(models.Model):
    patio = models.IntegerField('82. En el patio')
    otra = models.IntegerField('83. En otras áreas' )
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "81. Número de árboles frutales en el patio y en otras áreas de la finca no comerciales... o eventualmente comerciales"
        
class CalidadPatio(models.Model):
    calidad = models.IntegerField('Calidad del patio', choices=CHOICE_CALIDAD_PATIO)
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Calidad del patio"
        
class Ganado(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class GanadoMayor(models.Model):
    ganado = models.ForeignKey(Ganado, verbose_name="Ganado mayor y menor en propiedad")
    cantidad = models.IntegerField()
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Ganado Mayor y Menor"
