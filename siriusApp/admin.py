from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Cliente, Servicio, Proyecto, Presupuesto, Incidencia, PerfilUsuario

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rut', 'email', 'tipo_cliente', 'activo', 'fecha_registro']
    list_filter = ['tipo_cliente', 'activo', 'fecha_registro']
    search_fields = ['nombre', 'rut', 'email']
    list_editable = ['activo']
    ordering = ['nombre']

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo_servicio', 'precio_base', 'activo', 'fecha_creacion']
    list_filter = ['tipo_servicio', 'activo', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['precio_base', 'activo']
    ordering = ['tipo_servicio', 'nombre']

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cliente', 'estado', 'prioridad', 'responsable', 'fecha_inicio', 'presupuesto_total']
    list_filter = ['estado', 'prioridad', 'fecha_inicio', 'responsable']
    search_fields = ['nombre', 'cliente__nombre', 'descripcion']
    list_editable = ['estado', 'prioridad']
    filter_horizontal = ['servicios']
    date_hierarchy = 'fecha_inicio'
    ordering = ['-fecha_creacion']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'cliente', 'descripcion', 'servicios')
        }),
        ('Fechas', {
            'fields': ('fecha_inicio', 'fecha_fin_estimada', 'fecha_fin_real')
        }),
        ('Estado y Prioridad', {
            'fields': ('estado', 'prioridad')
        }),
        ('Presupuesto', {
            'fields': ('presupuesto_total', 'costo_real')
        }),
        ('Responsabilidad', {
            'fields': ('responsable', 'creado_por')
        }),
    )

@admin.register(Presupuesto)
class PresupuestoAdmin(admin.ModelAdmin):
    list_display = ['numero_presupuesto', 'cliente', 'monto_total', 'fecha_emision', 'validez_dias', 'estado']
    list_filter = ['estado', 'fecha_emision', 'cliente']
    search_fields = ['numero_presupuesto', 'cliente__nombre', 'descripcion']
    readonly_fields = ['numero_presupuesto', 'fecha_creacion']

@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'proyecto', 'tipo_incidencia', 'prioridad', 'estado', 'reportado_por', 'fecha_reporte']
    list_filter = ['tipo_incidencia', 'prioridad', 'estado', 'fecha_reporte']
    search_fields = ['titulo', 'descripcion', 'proyecto__nombre']
    list_editable = ['estado', 'prioridad']
    date_hierarchy = 'fecha_reporte'
    ordering = ['-fecha_reporte']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('proyecto', 'titulo', 'descripcion', 'tipo_incidencia')
        }),
        ('Estado y Prioridad', {
            'fields': ('prioridad', 'estado')
        }),
        ('Asignación', {
            'fields': ('reportado_por', 'asignado_a')
        }),
        ('Resolución', {
            'fields': ('fecha_resolucion', 'solucion')
        }),
        ('Archivos', {
            'fields': ('archivo_adjunto',)
        }),
    )

class PerfilUsuarioInline(admin.StackedInline):
    model = PerfilUsuario
    can_delete = False
    verbose_name_plural = 'Perfil de Usuario'

class UserAdmin(BaseUserAdmin):
    inlines = (PerfilUsuarioInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ['user', 'tipo_usuario', 'empresa', 'telefono', 'activo']
    list_filter = ['tipo_usuario', 'activo', 'fecha_creacion']
    search_fields = ['user__username', 'user__email', 'empresa', 'rut']
    list_editable = ['tipo_usuario', 'activo']