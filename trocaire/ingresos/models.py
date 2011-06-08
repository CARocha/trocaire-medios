# -*- coding: utf-8 -*-

from django.db import models
from trocaire.medios.models import *

# Create your models here.

choice_comercializacion = (
                                (1,'Granos básicos'),
                                (2,'Cultivos permanentes'),
                                (3,'Cualtivos anuales')
                          )
                          
choice_clasificacion = (
                                (1,'Agropecuarios'),
                                (2,'Comercio'),
                                (3,'Forestal'),
                                (4,'Trabajo asalariado'),
                                (5,'Remesas'),
                                (6,'Alquieres'),
                                (7,'Otros')
                          )

class Fuentes(models.Model):
    nombre = models.CharField(max_length=200)
    clasificacion = models.IntegerField(choices=choice_clasificacion)
    def __unicode__(self):
        return self.nombre
        
class PrincipalesFuentes(models.Model):
    fuente = models.ManyToManyField(Fuentes, verbose_name="Fuentes de ingreso")
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Cuales son las principales fuentes de ingreso de la familia"
        
class CIPeriodos(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class CIPermanentes(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class CIEstacionales(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class CIHortalizas(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class CultivosIPeriodos(models.Model):
    cultivo = models.ForeignKey(CIPeriodos)
    cuanto_primera = models.FloatField('Cuanto vendio en ciclo de primera', help_text="En qq")
    cuanto_postrera = models.FloatField('Cuanto vendio en ciclo de postrera', help_text="En qq")
    cuanto_apante = models.FloatField('Cuanto vendio en ciclo de apante', help_text="En qq")
    precio_primera = models.FloatField('Precio de venta de ciclo primera', help_text="En C$")
    precio_postrera = models.FloatField('Precio de venta de ciclo de postrera', help_text="En C$")
    precio_apante = models.FloatField('Precio de venta de ciclo de apante', help_text="En C$")
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Ventas agricolas"
        
    def suma_primera(self):
        primera = self.cuanto_primera * self.precio_primera
        return primera
    def suma_postrera(self):
        postrera = self.cuanto_postrera * self.precio_postrera
        return postrera
    def suma_apante(self):
        apante = self.cuanto_apante * self.precio_apante
        return apante
        
class CultivosIPermanentes(models.Model):
    cultivo = models.ForeignKey(CIPermanentes)
    cuanto = models.FloatField('Cuánto vendio', help_text="En qq")
    precio = models.FloatField('Precio de venta', help_text="En C$")
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Cultivos Permanentes"
        
    def perma(self):
        total = self.cuanto * self.precio
        
        return total
        
class CultivosIEstacionales(models.Model):
    cultivo = models.ForeignKey(CIEstacionales)
    cuanto = models.FloatField('Cuánto vendio', help_text="En qq")
    precio = models.FloatField('Precio de venta', help_text="En C$")
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Cultivos Estacionales"
        
#    def save(self, *args, **kwargs)
#        self.total = self.cuanto * self.precio
#        super(CultivosIEstacionales, self).save(*args, **kwargs)
        
    def estacional(self):
        total = self.cuanto * self.precio
        
        return total

class IHortalizas(models.Model):
    hortaliza = models.ForeignKey(CIHortalizas)
    cuanto = models.FloatField('Cuánto vendio', help_text="En qq")
    precio = models.FloatField('Precio de venta', help_text="En C$")
    equivalencias = models.FloatField()
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Hortalizas"
        
    def hortalizas(self):
        total = self.cuanto * self.precio
        
        return total
        
class IngresoPatio(models.Model):
    invierno = models.FloatField('Monto de los ingreso obtenido en invierno')
    verano = models.FloatField('Monto de los ingreso obtenido en verano')
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Ingreso por la producción agrícola del patio"
        
    def sumar(*args):
        pass
        
    def patio(self):
        total = self.invierno + self.verano
        
        return total
        
class Ganados(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

class IngresoGanado(models.Model):
    ganado = models.ForeignKey(Ganados)
    vendidos = models.IntegerField('Número de animales vendidos')
    valor = models.FloatField('Valor de venta')
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Ingresos por la comercialización del ganado mayor y menor"
        
    def ganados(self):
        total = self.vendidos * self.valor
        
        return total
        
class Productos(models.Model):
    nombre = models.CharField(max_length=200)
    unidad = models.CharField(max_length=20)
    def __unicode__(self):
        return self.nombre
               
class Lactios(models.Model):
    producto = models.ForeignKey(Productos)
    invierno_precio = models.FloatField()
    cantidad_invi = models.FloatField('Cantidad en Invierno')
    verano_precio = models.FloatField()
    cantidad_vera = models.FloatField('Cantidad en Verano')
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Producto en el ultimo año"
        
    def lacti(self):
        lista = []
        invierno = self.cantidad_invi * self.invierno_precio
        verano = self.cantidad_vera * self.verano_precio
        total = invierno + verano
        
        lista = [invierno, verano, total]
        return lista
        
class PProcesado(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class ProductosProcesado(models.Model):
    producto = models.ForeignKey(PProcesado)
    cantidad = models.FloatField('Cantidad vendida anualmente')
    monto = models.FloatField('Monto de los ingresos obtenidos')
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Ingresos por la producción, comercializacion e ingresos por productos procesados"
        
    def procesado(self):
        total = self.monto
        
        return total        
        
class OtrasActividades(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class OtrosIngresos(models.Model):
    actividad = models.ForeignKey(OtrasActividades)
    mayo = models.FloatField()
    junio = models.FloatField()
    julio = models.FloatField()
    agosto = models.FloatField()
    septiembre = models.FloatField()
    octubre = models.FloatField()
    noviembre = models.FloatField()
    diciembre = models.FloatField()
    enero = models.FloatField()
    febrero = models.FloatField()
    marzo = models.FloatField()
    abril = models.FloatField()
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Otros ingresos en el nucleo familiar (Estimación de ingresos anuales)"
        
    def otros(self):
        total = self.mayo + self.junio + self.julio + self.agosto + self.septiembre + self.octubre + self.noviembre + self.diciembre + self.enero + self.febrero + self.marzo + self.abril
        return total
        
choice_vendes = (
                                (1,'1. Vende Individual. No incluye vender en ferias'),
                                (2,'2. Vende colectivo. NO incluye venta en la cooperativa'),
                                (3,'3. Vende a la cooperativa de la que es socio'),
                                (4,'4. Vende en ferias campesinas'),
                                (5,'5. No aplica. No vende')
                                
                          )
                          
class PrincipalForma(models.Model):
    principal = models.IntegerField('121. Cuál es la principal forma de comercializar su producción',
                                    choices=choice_vendes)
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Principal Forma de comercializar su produccion"
        
class ProductosPrincipales(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class VendeProducto(models.Model):
    principal = models.ForeignKey(ProductosPrincipales, verbose_name="Rubros")
    forma = models.IntegerField('Forma principal de venta', choices=choice_vendes)
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "122. Como vende cada uno de los siguientes productos"  
