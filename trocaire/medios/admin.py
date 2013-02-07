from django.contrib import admin
from django.contrib.auth.models import User

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
    can_delete = True
    
class AdminDescripcionInline(admin.TabularInline):
    model = Descripcion
    extra = 1
    max_num = 5
    can_delete = True
    
class AdminEscolaridadInline(admin.TabularInline):
    model = Escolaridad
    fields = ('beneficia',)
    extra = 1
    max_num = 1
    can_delete = True

# calidad de vida
    
class AdminInmigracionInline(admin.TabularInline):
    model = Inmigracion
    extra = 1
    max_num = 5
    can_delete = True
    
class AdminAccesoEscuela(admin.TabularInline):
    model = AccesoEscuela
    extra = 1
    max_num = 3
    can_delete = True
    
class AdminRazonesNoEstudia(admin.TabularInline):
    model = RazonesNoEstudia
    extra = 1
    max_num = 2
    can_delete = True

class AdminAbasteceInline(admin.TabularInline):
    model = Agua
    extra = 1
    max_num = 1
    can_delete = True
    
admin.site.register(Abastece)

# formas y propiedad

class AdminTierraInline(admin.TabularInline):
    model = Tierra
    extra = 1
    max_num = 7
    can_delete = True
    
class AdminPropiedadInline(admin.TabularInline):
    model = Propiedad
    fields = ('ciclo',)
    extra = 1
    max_num = 1
    can_delete = True
    
admin.site.register(Ciclo)
admin.site.register(Riegos)

# produccion agropecuaria

class AdminCultivosPeriodosInline(admin.TabularInline):
    model = CultivosPeriodos
    extra = 1
    max_num = 8
    can_delete = True
    
    
admin.site.register(CPeriodos)
admin.site.register(CPermanentes)
admin.site.register(CAnuales)
admin.site.register(CHortalizas)
admin.site.register(Codigo)

class AdminCultivosPermanentesInline(admin.TabularInline):
    model = CultivosPermanentes
    extra = 1
    max_num = 8
    can_delete = True
    
class AdminCultivosAnualesInline(admin.TabularInline):
    model = CultivosAnuales
    extra = 1
    max_num = 8
    can_delete = True
    
class AdminHortalizaInline(admin.TabularInline):
    model = Hortalizas
    extra = 1
    max_num = 8
    can_delete = True
    
class AdminConsumoDiarioInline(admin.TabularInline):
    model = ConsumoDiario
    extra = 1
    max_num = 1
    can_delete = True
    
class AdminPricipalLimitacionInline(admin.TabularInline):
    model = PrincipalLimitacion
    extra = 1
    max_num = 1
    can_delete = True

admin.site.register(Limitaciones)
    
class AdminPatioCultivadaInline(admin.TabularInline):
    model = PatioCultivada
    extra = 1
    max_num = 1
    can_delete = True
    
class AdminArbolesInline(admin.TabularInline):
    model = Arboles
    extra = 1
    max_num = 1
    can_delete = True
    
class AdminCalidadPatioInline(admin.TabularInline):
    model = CalidadPatio
    extra = 1
    max_num = 1
    can_delete = True
    
class AdminGanadoMayorInline(admin.TabularInline):
    model = GanadoMayor
    extra = 1
    max_num = 11
    can_delete = True
    
admin.site.register(Ganado)

# Ingresos

class AdminPrincipalesFuentesInline(admin.TabularInline):
    model = PrincipalesFuentes
    extra = 1
    max_num = 1
    can_delete = True
    
admin.site.register(Fuentes)

class AdminCultivosIPeriodosInline(admin.TabularInline):
    model = CultivosIPeriodos
    extra = 1
    max_num = 8
    can_delete = True
    
class AdminCultivosIPermanentesInline(admin.TabularInline):
    model = CultivosIPermanentes
    extra = 1
    max_num = 8
    can_delete = True
    
class AdminCultivosIEstacionalesInline(admin.TabularInline):
    model = CultivosIEstacionales
    extra = 1
    max_num = 9
    can_delete = True
    
    
class AdminIHortalizasInline(admin.TabularInline):
    model = IHortalizas
    fields = ('hortaliza','cuanto','precio',)
    extra = 1
    max_num = 12
    can_delete = True

admin.site.register(CIPeriodos)
admin.site.register(CIPermanentes)
admin.site.register(CIEstacionales)
admin.site.register(CIHortalizas)

class AdminIngresoPatioInline(admin.TabularInline):
    model = IngresoPatio
    extra = 1
    max_num = 1
    can_delete = True

class AdminIngresoGanadoInline(admin.TabularInline):
    model = IngresoGanado
    extra = 1
    max_num = 12
    can_delete = True
        
admin.site.register(Ganados)

class AdminLactiosInline(admin.TabularInline):
    model = Lactios
    extra = 1
    max_num = 5
    can_delete = True
    
admin.site.register(Productos)

class AdminProductosProcesadoInline(admin.TabularInline):
    model = ProductosProcesado
    extra = 1
    max_num = 12
    can_delete = True   

admin.site.register(PProcesado)

class AdminOtrosIngresosInline(admin.StackedInline):
    model = OtrosIngresos
    #fields = (('mayo','junio','julio','agosto'),('septiembre','octubre','noviembre','diciembre'),('enero','febrero','marzo','abril'))
    fieldsets = (
        (None, {
            'fields': ('actividad',('mayo', 'junio', 'julio', 'agosto'),
                      ('septiembre','octubre','noviembre','diciembre'),
                      ('enero','febrero','marzo','abril'))
        }),
    )
    extra = 1
    max_num = 12
    can_delete = True
    
admin.site.register(OtrasActividades)

class AdminPrincipalFormaInline(admin.TabularInline):
    model = PrincipalForma
    extra = 1
    max_num = 1
    can_delete = True
    
class AdminVendeProductoInline(admin.TabularInline):
    model = VendeProducto
    extra = 1
    max_num = 16
    can_delete = True
    
admin.site.register(ProductosPrincipales)

# tecnologia

class AdminRiegoInline(admin.TabularInline):
    model = Riego
    extra = 1
    max_num = 5
    can_delete = True
    
class AdminAreaProtegidaInline(admin.TabularInline):
    model = AreaProtegida
    extra = 1
    max_num = 6
    can_delete = True
    
class AdminUsoTecnologiaInline(admin.TabularInline):
    model = UsoTecnologia
    extra = 1
    max_num = 4
    can_delete = True
    
class AdminSemillaInline(admin.TabularInline):
    model = Semilla
    extra = 1
    max_num = 1
    can_delete = True
    
# diversidad alimentaria
    
class AdminDiversidadInline(admin.TabularInline):
    model = Diversidad
    extra = 1
    max_num = 21
    can_delete = True
    
admin.site.register(Alimentos)

# crisis sobre seguridad alimentaria

class AdminCrisisInline(admin.TabularInline):
    model = Crisis
    extra = 1
    max_num = 1
    can_delete = True
    
admin.site.register(EstrategiaCrisis)

class AdminAccesoCreditoInline(admin.TabularInline):
    model = AccesoCredito
    extra = 1
    max_num = 1
    can_delete = True
    
admin.site.register(Credito)
    
# participacion ciudadana

class AdminParticipacionInline(admin.TabularInline):
    model = Participacion
    extra = 1
    max_num = 2
    can_delete = True
    
class AdminParticipacionCPCInline(admin.TabularInline):
    model = ParticipacionCPC
    extra = 1
    max_num = 2
    can_delete = True
    
class AdminFrecuenciaInline(admin.TabularInline):
    model = Frecuencia
    extra = 1
    max_num = 2
    can_delete = True
    
# genero

class AdminGeneroInline(admin.TabularInline):
    model = Genero
    extra = 1
    max_num = 6
    can_delete = True
    
class AdminTomaDecicionInline(admin.TabularInline):
    model = TomaDecicion
    extra = 1
    max_num = 6
    can_delete = True
    
class EncuestaAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()
        
    def queryset(self, request):
        qs = super(EncuestaAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)
        
    save_on_top = True
    actions_on_top = True
    exclude = ('usuario',)
    inlines = [AdminComposicionInline,AdminDescripcionInline,AdminEscolaridadInline,
               AdminInmigracionInline,AdminAccesoEscuela,AdminRazonesNoEstudia,AdminAbasteceInline,
               AdminTierraInline,AdminPropiedadInline,AdminCultivosPeriodosInline,
               AdminCultivosPermanentesInline,AdminCultivosAnualesInline,AdminHortalizaInline,
               AdminConsumoDiarioInline,AdminPricipalLimitacionInline,AdminPatioCultivadaInline,
               AdminArbolesInline,AdminCalidadPatioInline,AdminGanadoMayorInline,
               AdminPrincipalesFuentesInline,AdminCultivosIPeriodosInline,AdminCultivosIPermanentesInline,
               AdminCultivosIEstacionalesInline,AdminIHortalizasInline,AdminIngresoPatioInline,
               AdminIngresoGanadoInline,AdminProductosProcesadoInline,AdminLactiosInline,AdminOtrosIngresosInline,
               AdminPrincipalFormaInline,AdminVendeProductoInline,AdminRiegoInline,AdminAreaProtegidaInline,
               AdminUsoTecnologiaInline,AdminSemillaInline,AdminDiversidadInline,AdminCrisisInline,
               AdminAccesoCreditoInline,AdminParticipacionInline,AdminParticipacionCPCInline,AdminFrecuenciaInline,
               AdminGeneroInline,AdminTomaDecicionInline,              
               ]
    list_display = ['beneficiario', 'municipio', 'comarca', 'contraparte' ]
    list_filter = ['contraparte','fecha']
    search_fields = ['beneficiario']
    #date_hierarchy = 'fecha'
    class Media:
        css = {
            'all': ('/archivos/css/admin.css',),
        }
               
admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Contraparte)
admin.site.register(Recolector)
    
