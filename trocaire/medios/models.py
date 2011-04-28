# -*- coding: utf-8 -*-

from django.db import models
from trocaire.lugar import *
# Create your models here.

class Recolector(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

class Encuesta(models.Model):
    ''' Modelo de encuesta principal
    '''
    municipio = models.ForeignKey('Nombre del Municipio', Municipio)
    comarca = moels.ForeignKey('Nombre de la comarca', Comarca)
    beneficiario = models.CharField('Nombre del Beneficiario/a', max_length=200)
    encuestador = models.ForeignKey('Nombre del encuestador', Recolector)
    def __unicode__(self):
        return self.beneficiario
    class Meta:
        verbose_name_plural = "Identificación"

#Utilitarios para toda la encuesta
        
CHOICE_SEXO = (
                    (1, 'Masculino'),
                    (2, 'Femenino')
              )
              
CHOICE_ESTADO = (
                    (1, 'Casado/a'),
                    (2, 'Soltero/a'),
                    (3, 'Viudo/a')
                )
              
CHOICE_JEFE = (
                    (1, 'Si'),
                    (2, 'No'),
                    (3, 'Compartida')
              )
CHOICE_RELACION = (
                    (1, 'Conyugue'),
                    (2, 'Madre/Padre'),
                    (3, 'Hijo/Hija'),
                    (4, 'Otro/a'),
                    (5, 'No aplica')
                  )
                  
CHOICE_SEXO_JEFE = (
                    (1, 'Masculino'),
                    (2, 'Femenino'),
                    (3, 'No aplica')
                   )
                   
CHOICE_DESCRIPCION = (
    (1, '8. Número de personas que viven en el hogar...(que no se han ido a vivir permanente a otro lugar)'),
    (2, '9. Número de niñas/niños entre 0 y 17 que viven en el hogar...'),
    (3, '10. Número personas entre 18 y 60 años en el hogar...'),
    (4, '11. Número personas 61 años y más en el hogar familiar...'),
    (5, '12. Número de personas entre 18 y 60 años en el hogar familiar con discapacidad o deficiencia imposibilitados de trabajar...')
)

# II calidad de vida apps calidad_vida

CHOICE_INMIGRACION = (
    (1, '15. En los últimos 12 meses... Alguien de la familia salió a trabajar por un periodo menor de 6 meses fuera del pais y regreso'),
    (2, '16. En los últimos 12 meses... Alguien de la familia salió a trabajar por un periodo entre 6 y 12 meses fuera del pais y regreso'),
    (3, '17. En los últimos 12 meses... Alguien de la familia salió a trabajar por un periodo menor de 6 meses en Nicaragua y regreso'),
    (4, '18. En los últimos 12 meses... Alguien de la familia salió a trabajar por un periodo entre 6 y 12 meses en Nicaragua y regreso'),
    (5, '19. Su conyugue... tiene más de un año de haber salido a trabajar y no ha regresado')
)

CHOICE_ACCESO = (
    (1, '20. Número de niñas/os entre 6 y 17 años con discapacidad o deficiencia imposibilitados de ir a la escuela'),
    (2, '21. Número de niñas/os entre 6 y 14 años No incluye con discapacidad o deficiencia. Cuántos estudian o no estudian.'),
    (3, '22. Razón principal porque no estudia.'),
    (4, '23. Número de niñas/os entre 15 y 17 años. No incluye con discapacidad o deficiencia. '),
    (5, '24. Razón principal porque no estudian')
)

CHOICE_CALIDAD = (
                    (1, 'Si'),
                    (2, 'No'),
                    (3, 'No sabe')
                 )
                 
CHOICE_CLORADA = (
                    (1, 'Le da tratamiento'),
                    (2, 'No le da tratamiento'),
                    (3, 'No aplica. Viene clorada')
                 )
CHOICE_SINO = (
                    (1, 'Si'),
                    (2, 'No')
                 )                                  

CHOICE_TECHO = (
                    (1, 'Zinc o playcen'),
                    (2, 'Teco y otros'),
                    (3, 'Paja o ripios')
                 )
                 
CHOICE_PISO = (
                    (1, 'Ladrillo, Cemento'),
                    (2, 'Tierra y otros'),
                    (3, 'Tierra')
                 )
                 
CHOICE_PAREDES = (
                    (1, 'Ladrillo, bloque, adobe, talquezal'),
                    (2, 'Madera, minifalda'),
                    (3, 'Materiales en mal estado')
                 )         
             
CHOICE_SERVICIO = (
                    (1, 'Inodoro'),
                    (2, 'Letrina'),
                    (3, 'No tiene')
                 )   
                 
CHOICE_ESTADO = (
                    (1, 'Buen estado'),
                    (2, 'Ni muy bueno ni muy malo'),
                    (3, 'En muy mal estado')
                 )
                 
# III FORMAS DE PROPIEDAD

CHOICE_AREA = (
    (1, '36. Área total en manzanas de la propiedad agropecuaria familiar'),
    (2, '37. De esta propiedad... Posee titulo real inscrito en el registro de la propiedad'),
    (3, '38. Posee un titulo entregado por el gobierno... y no lo ha inscrito.'),
    (4, '39. Posee un documento no inscrito(compra venta, herencia,otro)'),
    (5, '40. No posee ningún titulo de respaldo'),
    (6, '41. Si no vive en la propiedad agropecuaria donde trabaja. cuanto es el area del lote donde vive.')
    (7, '42. Posee titulo real inscrito en el registro de este lote. Poner el area que tiene con titulo real...')
)                    
