# -*- coding: utf-8 -*-
from django.db import models
from trocaire.medios.models import Encuesta 

CHOICE_COMERCIALIZACION = (
                             (1,'Granos básicos'),
                             (2,'Cultivos permanentes'),
                             (3,'Cualtivos anuales')
                          )
                          
CHOICE_CLASIFICACION = (
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
    clasificacion = models.IntegerField(choices=CHOICE_CLASIFICACION)

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
        
    def total_primera(self):
        return self.cuanto_primera * self.precio_primera

    def total_postrera(self):
        return self.cuanto_postrera * self.precio_postrera

    def total_apante(self):
        return self.cuanto_apante * self.precio_apante
    
    def total(self):
        return self.total_primera() + self.total_postrera() + self.total_apante()
        
class CultivosIPermanentes(models.Model):
    cultivo = models.ForeignKey(CIPermanentes)
    cuanto = models.FloatField('Cuánto vendio', help_text="En qq")
    precio = models.FloatField('Precio de venta', help_text="En C$")
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Cultivos Permanentes"
        
    def total(self):
        total = self.cuanto * self.precio
        
        return total
        
class CultivosIEstacionales(models.Model):
    cultivo = models.ForeignKey(CIEstacionales)
    cuanto = models.FloatField('Cuánto vendio', help_text="En qq")
    precio = models.FloatField('Precio de venta', help_text="En C$")
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Cultivos Estacionales"
        
    def total(self):
        return self.cuanto * self.precio

class IHortalizas(models.Model):
    hortaliza = models.ForeignKey(CIHortalizas)
    cuanto = models.FloatField('Cuánto vendio', help_text="En qq")
    precio = models.FloatField('Precio de venta', help_text="En C$")
    equivalencias = models.FloatField()
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Hortalizas"
        
    def total(self):
        return tself.cuanto * self.precio
        
class IngresoPatio(models.Model):
    invierno = models.FloatField('Monto de los ingreso obtenido en invierno')
    verano = models.FloatField('Monto de los ingreso obtenido en verano')
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Ingreso por la producción agrícola del patio"
        
    def total(self):
        return self.invierno + self.verano
        
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
        
    def total(self):
        return self.vendidos * self.valor
        
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
        
    def total(self):
        #TODO: REVISAR
        invierno = self.cantidad_invi * self.invierno_precio
        verano = self.cantidad_vera * self.verano_precio
        total = invierno + verano
        return [invierno, verano, total]
        
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
        
    def total(self):
        return self.monto 
        
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
        
    def total(self):
        return  self.mayo + self.junio + self.julio + self.agosto +\
                self.septiembre + self.octubre + self.noviembre +\
                self.diciembre + self.enero + self.febrero + self.marzo +\
                self.abril
        
CHOICE_VENDE = (
                 (1,'1. Vende Individual. No incluye vender en ferias'),
                 (2,'2. Vende colectivo. NO incluye venta en la cooperativa'),
                 (3,'3. Vende a la cooperativa de la que es socio'),
                 (4,'4. Vende en ferias campesinas'),
                 (5,'5. No aplica. No vende')
               )
                          
class PrincipalForma(models.Model):
    principal = models.IntegerField('121. Cuál es la principal forma de comercializar su producción',
                                    choices=CHOICE_VENDE)
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "Principal Forma de comercializar su produccion"
        
class ProductosPrincipales(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre
        
class VendeProducto(models.Model):
    principal = models.ForeignKey(ProductosPrincipales, verbose_name="Rubros")
    forma = models.IntegerField('Forma principal de venta', choices=CHOICE_VENDE)
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "122. Como vende cada uno de los siguientes productos"  
