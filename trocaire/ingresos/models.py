# -*- coding: utf-8 -*-
from django.db import models
from trocaire.medios.models import Encuesta 
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

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
    #campos ocultos
    fuentes_ap = models.IntegerField(default=0, editable=False)
    fuentes_no_ap = models.IntegerField(default=0, editable=False)

    def _save_fuentes(self, *args, **kwargs):
        self.fuentes_ap = self.fuente.filter(id__in = [1,2,3,4,5]).count()
        self.fuentes_no_ap = self.fuente.exclude(id__in = [1,2,3,4,5]).count()
        super(PrincipalesFuentes, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Cuales son las principales fuentes de ingreso de la familia"

#signal de post_add en PrincipalesFuentes para campos autocalculados: fuentes_ap, fuentes_no_ap    
@receiver(m2m_changed, sender=PrincipalesFuentes.fuente.through)
def create_fuentes_callback(sender, **kwargs):    
    instance = kwargs['instance']
    if kwargs['action'] == 'post_add':
        instance._save_fuentes()
        

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
    #campos hipsters
    total_primera = models.FloatField(editable=False)
    total_postrera = models.FloatField(editable=False)
    total_apante = models.FloatField(editable=False)
    total_primera = models.FloatField(editable=False)
    total = models.FloatField(editable=False)

    class Meta:
        verbose_name_plural = "Ventas agricolas"

    def save(self, *args, **kwargs):
        '''Save sobrecargado para calcular totales'''
        self.total_primera = self.cuanto_primera * self.precio_primera
        self.total_postrera = self.cuanto_postrera * self.precio_postrera
        self.total_apante = self.cuanto_apante * self.precio_apante
        self.total = self.total_primera + self.total_postrera + self.total_apante
        super(CultivosIPeriodos, self).save(*args, **kwargs)
        
class CultivosIPermanentes(models.Model):
    cultivo = models.ForeignKey(CIPermanentes)
    cuanto = models.FloatField('Cuánto vendio', help_text="En qq")
    precio = models.FloatField('Precio de venta', help_text="En C$")
    encuesta = models.ForeignKey(Encuesta)
    #campos hipsters
    total = models.FloatField(editable=False)

    class Meta:
        verbose_name_plural = "Cultivos Permanentes"
        
    def save(self, *args, **kwargs):
        self.total = self.cuanto * self.precio
        super(CultivosIPermanentes, self).save(*args, **kwargs)
        
class CultivosIEstacionales(models.Model):
    cultivo = models.ForeignKey(CIEstacionales)
    cuanto = models.FloatField('Cuánto vendio', help_text="En qq")
    precio = models.FloatField('Precio de venta', help_text="En C$")
    encuesta = models.ForeignKey(Encuesta)
    #campos hipsters
    total = models.FloatField(editable=False)

    class Meta:
        verbose_name_plural = "Cultivos Estacionales"
        
    def save(self, *args, **kwargs):
        self.total = self.cuanto * self.precio
        super(CultivosIEstacionales, self).save(*args, **kwargs)

class IHortalizas(models.Model):
    hortaliza = models.ForeignKey(CIHortalizas)
    cuanto = models.FloatField('Cuánto vendio', help_text="En qq")
    precio = models.FloatField('Precio de venta', help_text="En C$")
    equivalencias = models.FloatField(null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    #campos hipsters
    total = models.FloatField(editable=False)
    
    class Meta:
        verbose_name_plural = "Hortalizas"
        
    def save(self, *args, **kwargs):
        self.total = self.cuanto * self.precio
        super(IHortalizas, self).save(*args, **kwargs)
        
class IngresoPatio(models.Model):
    invierno = models.FloatField('Monto de los ingreso obtenido en invierno')
    verano = models.FloatField('Monto de los ingreso obtenido en verano')
    encuesta = models.ForeignKey(Encuesta)
    #campos hipsters
    total = models.FloatField(editable=False)

    class Meta:
        verbose_name_plural = "Ingreso por la producción agrícola del patio"

    def save(self, *args, **kwargs):
        self.total = self.invierno + self.verano
        super(IngresoPatio, self).save(*args, **kwargs)
        
class Ganados(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

class IngresoGanado(models.Model):
    ganado = models.ForeignKey(Ganados)
    vendidos = models.IntegerField('Número de animales vendidos')
    valor = models.FloatField('Valor de venta')
    #rango = models.FloatField('Rangos de precios')
    encuesta = models.ForeignKey(Encuesta)
    #campos hipsters
    total = models.FloatField(editable=False)

    class Meta:
        verbose_name_plural = "Ingresos por la comercialización del ganado mayor y menor"
        
    def save(self, *args, **kwargs):
        self.total = self.vendidos * self.valor
        super(IngresoGanado, self).save(*args, **kwargs)
        
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
    #campos hipsters
    total = models.FloatField(editable=False)
    total_verano = models.FloatField(editable=False)
    total_invierno  = models.FloatField(editable=False)

    class Meta:
        verbose_name_plural = "Producto en el ultimo año"
        
    def save(self, *args, **kwargs):
        self.total_invierno = self.cantidad_invi * self.invierno_precio
        self.total_verano = self.cantidad_vera * self.verano_precio
        self.total = self.total_invierno + self.total_verano
        super(Lactios, self).save(*args, **kwargs)

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
    #campos hipsters
    total = models.FloatField(editable=False)

    class Meta:
        verbose_name_plural = "Otros ingresos en el nucleo familiar (Estimación de ingresos anuales)"
        
    def save(self, *args, **kwargs):
        self.total = self.mayo + self.junio + self.julio + self.agosto +\
                self.septiembre + self.octubre + self.noviembre +\
                self.diciembre + self.enero + self.febrero + self.marzo +\
                self.abril
        super(OtrosIngresos, self).save(*args, **kwargs)
        
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

class TotalIngreso(models.Model):
    encuesta = models.ForeignKey(Encuesta, unique=True)
    total = models.FloatField(editable=False)
    total_ap = models.FloatField(editable=False)

    class Meta:
        verbose_name_plural = 'Totales'

    #def __unicode__(self):
    #    return 'Total para la encuesta %s' % self.encuesta

    def save(self, *args, **kwargs):
        self.total = self._get_total()
        self.total_ap = self._get_total() - (OtrosIngresos.objects.filter(encuesta=self.encuesta).aggregate(t=models.Sum('total'))['t'] or 0)
        print self.total, self.total_ap
        super(TotalIngreso, self).save(*args, **kwargs)
    
    def _get_total(self):
        params = dict(encuesta = self.encuesta)
        totales = [CultivosIPeriodos.objects.filter(**params).aggregate(t=models.Sum('total'))['t'], \
                CultivosIEstacionales.objects.filter(**params).aggregate(t=models.Sum('total'))['t'], \
                CultivosIPermanentes.objects.filter(**params).aggregate(t=models.Sum('total'))['t'], \
                IHortalizas.objects.filter(**params).aggregate(t=models.Sum('total'))['t'], \
                IngresoPatio.objects.filter(**params).aggregate(t=models.Sum('total'))['t'], \
                IngresoGanado.objects.filter(**params).aggregate(t=models.Sum('total'))['t'], \
                Lactios.objects.filter(**params).aggregate(t=models.Sum('total'))['t'], \
                ProductosProcesado.objects.filter(**params).aggregate(t=models.Sum('monto'))['t'], \
                OtrosIngresos.objects.filter(**params).aggregate(t=models.Sum('total'))['t']] 
        total = sum(filter(None, totales))
        return total

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Encuesta)
def create_encuesta_callback(sender, **kwargs):    
    encuesta = kwargs['instance']
    try:
        total_ingreso = TotalIngreso.objects.get(encuesta=encuesta)
        total_ingreso.save()
    except:
        total_ingreso = TotalIngreso(encuesta=encuesta)
        total_ingreso.save()
