from django.contrib import admin

from trocaire.participacion_ciudadana.models import *
from trocaire.diversidad_alimentaria.models import *
from trocaire.crisis_alimentaria.models import *
from trocaire.formas_propiedad.models import *
from trocaire.calidad_vida.models import *
from trocaire.produccion.models import *
from trocaire.tecnologia.models import *
from trocaire.ingresos.models import *
from trocaire.familia.models import *
from trocaire.genero.models import *
from trocaire.lugar.models import *
from trocaire.medios.models import *

# familia

class AdminComposicionInline(admin.TabularInline):
    model = Composicion
    extra = 1
    max_num = 1
    can_delete = False
    
class AdminDescripcionInline(admin.TabularInline):
    model = Descripcion
    extra = 1
    max_num = 5
    can_delete = False
    
class AdminEscolaridadInline(admin.TabularInline):
    model = Escolaridad
    extra = 1
    max_num = 1
    can_delete = False

# calidad de vida
    
class AdminInmigracionInline(admin.TabularInline):
    model = Inmigracion
    extra = 1
    max_num = 5
    can_delete = False
    
class AdminAccesoEscuela(admin.TabularInline):
    model = AccesoEscuela
    extra = 1
    max_num = 5
    can_delete = False

class AdminAbasteceInline(admin.TabularInline):
    model = Agua
    extra = 1
    max_num = 1
    can_delete = False
    
admin.site.register(Abastece)

# formas y propiedad

class AdminTierraInline(admin.TabularInline):
    model = Tierra
    extra = 1
    max_num = 7
    can_delete = False
    
class AdminPropiedadInline(admin.TabularInline):
    model = Propiedad
    extra = 1
    max_num = 1
    can_delete = False
    
admin.site.register(Ciclo)
admin.site.register(Riegos)

# produccion agropecuaria

class AdminCultivosPeriodosInline(admin.TabularInline):
    model = CultivosPeriodos
    extra = 1
    max_num = 8
    can_delete = False
    
    
admin.site.register(CPeriodos)
admin.site.register(CPermanentes)
admin.site.register(CAnuales)
admin.site.register(CHortalizas)
admin.site.register(Codigo)

class AdminCultivosPermanentesInline(admin.TabularInline):
    model = CultivosPermanentes
    extra = 1
    max_num = 8
    can_delete = False
    
class AdminCultivosAnualesInline(admin.TabularInline):
    model = CultivosAnuales
    extra = 1
    max_num = 8
    can_delete = False
    
class AdminHortalizaInline(admin.TabularInline):
    model = Hortalizas
    extra = 1
    max_num = 8
    can_delete = False
    
class AdminConsumoDiarioInline(admin.TabularInline):
    model = ConsumoDiario
    extra = 1
    max_num = 1
    can_delete = False
    
class AdminPricipalLimitacionInline(admin.TabularInline):
    model = PrincipalLimitacion
    extra = 1
    max_num = 1
    can_delete = False

admin.site.register(Limitaciones)
    
class AdminPatioCultivadaInline(admin.TabularInline):
    model = PatioCultivada
    extra = 1
    max_num = 1
    can_delete = False
    
class AdminArbolesInline(admin.TabularInline):
    model = Arboles
    extra = 1
    max_num = 1
    can_delete = False
    
class AdminCalidadPatioInline(admin.TabularInline):
    model = CalidadPatio
    extra = 1
    max_num = 1
    can_delete = False
    
class AdminGanadoMayorInline(admin.TabularInline):
    model = GanadoMayor
    extra = 1
    max_num = 11
    can_delete = False
    
admin.site.register(Ganado)

# Ingresos

class AdminPrincipalesFuentesInline(admin.TabularInline):
    model = PrincipalesFuentes
    extra = 1
    max_num = 1
    can_delete = False
    
admin.site.register(Fuentes)

class AdminCultivosIPeriodosInline(admin.TabularInline):
    model = CultivosIPeriodos
    extra = 1
    max_num = 8
    can_delete = False
    
class AdminCultivosIPermanentesInline(admin.TabularInline):
    model = CultivosIPermanentes
    extra = 1
    max_num = 8
    can_delete = False
    
class AdminCultivosIEstacionalesInline(admin.TabularInline):
    model = CultivosIEstacionales
    extra = 1
    max_num = 9
    can_delete = False
    
    
class AdminIHortalizasInline(admin.TabularInline):
    model = IHortalizas
    extra = 1
    max_num = 12
    can_delete = False

admin.site.register(CIPeriodos)
admin.site.register(CIPermanentes)
admin.site.register(CIEstacionales)
admin.site.register(CIHortalizas)

class AdminIngresoPatioInline(admin.TabularInline):
    model = IngresoPatio
    extra = 1
    max_num = 1
    can_delete = False

class AdminIngresoGanadoInline(admin.TabularInline):
    model = IngresoGanado
    extra = 1
    max_num = 12
    can_delete = False
        
admin.site.register(Ganados)

class AdminLactiosInline(admin.TabularInline):
    model = Lactios
    extra = 1
    max_num = 1
    can_delete = False
    
admin.site.register(Productos)

class AdminProductosProcesadoInline(admin.TabularInline):
    model = ProductosProcesado
    extra = 1
    max_num = 12
    can_delete = False   

admin.site.register(PProcesado)

class AdminOtrosIngresosInline(admin.TabularInline):
    model = OtrosIngresos
    extra = 1
    max_num = 12
    can_delete = False
    
admin.site.register(OtrasActividades)

class AdminPrincipalFormaInline(admin.TabularInline):
    model = PrincipalForma
    extra = 1
    max_num = 1
    can_delete = False
    
class AdminVendeProductoInline(admin.TabularInline):
    model = VendeProducto
    extra = 1
    max_num = 16
    can_delete = False
    
admin.site.register(ProductosPrincipales)

# tecnologia

class AdminRiegoInline(admin.TabularInline):
    model = Riego
    extra = 1
    max_num = 5
    can_delete = False
    
class AdminAreaProtegidaInline(admin.TabularInline):
    model = AreaProtegida
    extra = 1
    max_num = 6
    can_delete = False
    
class AdminUsoTecnologiaInline(admin.TabularInline):
    model = UsoTecnologia
    extra = 1
    max_num = 4
    can_delete = False
    
class AdminSemillaInline(admin.TabularInline):
    model = Semilla
    extra = 1
    max_num = 1
    can_delete = False
    
# diversidad alimentaria
    
class AdminDiversidadInline(admin.TabularInline):
    model = Diversidad
    extra = 1
    max_num = 21
    can_delete = False
    
admin.site.register(Alimentos)

# crisis sobre seguridad alimentaria

class AdminCrisisInline(admin.TabularInline):
    model = Crisis
    extra = 1
    max_num = 1
    can_delete = False
    
admin.site.register(EstrategiaCrisis)

class AdminAccesoCreditoInline(admin.TabularInline):
    model = AccesoCredito
    extra = 1
    max_num = 1
    can_delete = False
    
# participacion ciudadana

class AdminParticipacionInline(admin.TabularInline):
    model = Participacion
    extra = 1
    max_num = 2
    can_delete = False
    
class AdminParticipacionCPCInline(admin.TabularInline):
    model = ParticipacionCPC
    extra = 1
    max_num = 2
    can_delete = False
    
class AdminFrecuenciaInline(admin.TabularInline):
    model = Frecuencia
    extra = 1
    max_num = 2
    can_delete = False
    
# genero

class AdminGeneroInline(admin.TabularInline):
    model = Genero
    extra = 1
    max_num = 6
    can_delete = False
    
class AdminTomaDecicionInline(admin.TabularInline):
    model = TomaDecicion
    extra = 1
    max_num = 6
    can_delete = False
    
class EncuestaAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    inlines = [AdminComposicionInline,AdminDescripcionInline,AdminEscolaridadInline,
               AdminInmigracionInline,AdminAccesoEscuela,AdminAbasteceInline,
               AdminTierraInline,AdminPropiedadInline,AdminCultivosPeriodosInline,
               AdminCultivosPermanentesInline,AdminCultivosAnualesInline,AdminHortalizaInline,
               AdminConsumoDiarioInline,AdminPricipalLimitacionInline,AdminPatioCultivadaInline,
               AdminArbolesInline,AdminCalidadPatioInline,AdminGanadoMayorInline,
               AdminPrincipalesFuentesInline,AdminCultivosIPeriodosInline,AdminCultivosIPermanentesInline,
               AdminCultivosIEstacionalesInline,AdminIHortalizasInline,AdminIngresoPatioInline,
               AdminIngresoGanadoInline,AdminLactiosInline,AdminProductosProcesadoInline,AdminOtrosIngresosInline,
               AdminPrincipalFormaInline,AdminVendeProductoInline,AdminRiegoInline,AdminAreaProtegidaInline,
               AdminUsoTecnologiaInline,AdminSemillaInline,AdminDiversidadInline,AdminCrisisInline,
               AdminAccesoCreditoInline,AdminParticipacionInline,AdminParticipacionCPCInline,AdminFrecuenciaInline,
               AdminGeneroInline,AdminTomaDecicionInline,              
               ]
    #list_display = ()
    #list_filter = ['comunidad']
#    search_fields = []
#    date_hierarchy = 'fecha'
               
admin.site.register(Encuesta, EncuestaAdmin)
    
