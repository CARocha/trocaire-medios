# -*- coding: utf-8 -*-

from django.db import models
from trocaire.medios.models import CHOICE_SEXO, CHOICE_JEFE, CHOICE_RELACION, \
        CHOICE_SEXO_JEFE, CHOICE_DESCRIPCION, CHOICE_CIVIL, Encuesta 

class Composicion(models.Model):
    ''' Modelo sobre la composicion de la 
        familas
    '''
    sexo = models.IntegerField('1. Sexo del beneficiario/a', choices=CHOICE_SEXO)
    edad = models.IntegerField('2. Edad del beneficiario/a')
    estado = models.IntegerField('3. Estado Civil', choices=CHOICE_CIVIL)
    beneficio = models.IntegerField('4. El o la beneficiario/a es el jefe de familas', choices=CHOICE_JEFE)
    relacion = models.IntegerField('5. Si no es jefe/a de famila... cuál es su relación con el jefe de Familia',
                                    choices=CHOICE_RELACION)
    sexo_jefe = models.IntegerField('6. Si no es jefe/a... Cuál es el sexo del jefe de familia',
                                    choices=CHOICE_SEXO_JEFE)
    num_familia = models.IntegerField('7. Número de personas que viven en la vivienda')
    encuesta = models.ForeignKey(Encuesta)
    #ocultos
    dependientes = models.FloatField(editable=False, default=0)

    def _get_sexo_jefe(self):
        #validar si el beneficiario es el jefe de familia o es compartido
        if self.beneficio in [1, 3]:
            return self.sexo        
        #si el beneficiario no es el jefe
        elif self.beneficio == 2:
            if self.sexo_jefe in [1, 2]:
                return self.sexo_jefe                    
            else:
                #si no aplica, tomar el sexo del beneficiario como sexo del jefe
                return self.sexo  

    def save(self, *args, **kwargs):
        #debe de haber una mejor manera de hacer esto pero me vale gaver! :-D
        viejos = sum(map(sum, Descripcion.objects.filter(descripcion = 4, encuesta = self.encuesta).values_list('femenino','masculino')))
        discapacitados = sum(map(sum,Descripcion.objects.filter(descripcion = 5, encuesta = self.encuesta).values_list('femenino','masculino')))
        adultos = sum(map(sum,Descripcion.objects.filter(descripcion = 3, encuesta = self.encuesta).values_list('femenino','masculino')))
        chateles = sum(map(sum,Descripcion.objects.filter(descripcion = 2, encuesta = self.encuesta).values_list('femenino','masculino')))
        try:
            self.dependientes = (viejos + chateles + discapacitados) / (float(adultos) - discapacitados)
        except:
            self.dependientes = 0
        
        '''antes de guardar los dependientes, guardar el sexo del jefe en la encuesta'''
        self.encuesta.sexo_jefe = self._get_sexo_jefe()
        self.encuesta.save()
        
        #ahora guardar los dependientes        
        super(Composicion, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Beneficiario" 

class Descripcion(models.Model):
    descripcion = models.IntegerField('Descripción', choices=CHOICE_DESCRIPCION)
    femenino = models.IntegerField()
    masculino = models.IntegerField()
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "DESCRIPCIÓN"

CHOICE_ESCOLARIDAD = (
                            (1, "1) Analfabeto"),
                            (2, "2) 4 y hasta 6 grado de Primaria"),
                            (3, "3) Algo de Secundaria"),
                            (4, "4) Bachiller o Técnico Medio"),
                            (5, "5) Universidad o Profesional Universitario"),
                            (6, "6) No aplica"),
                            (7, "7) Hasta 3er grado")
                     )
        
class Escolaridad(models.Model):
    beneficia = models.IntegerField(choices=CHOICE_ESCOLARIDAD, verbose_name="13. Beneficiaria/o")
    conyugue = models.IntegerField(choices=CHOICE_ESCOLARIDAD, verbose_name="14. Conyugue", null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "Nivel de educación del beneficiario/a"
