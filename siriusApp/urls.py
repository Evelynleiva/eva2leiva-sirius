from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # Clientes
    path('clientes/', views.cliente_lista, name='cliente_lista'),
    path('clientes/crear/', views.cliente_crear, name='cliente_crear'),
    path('clientes/<int:pk>/editar/', views.cliente_editar, name='cliente_editar'),
    path('clientes/<int:pk>/eliminar/', views.cliente_eliminar, name='cliente_eliminar'),
    
    # Servicios
    path('servicios/', views.servicio_lista, name='servicio_lista'),
    path('servicios/crear/', views.servicio_crear, name='servicio_crear'),
    path('servicios/<int:pk>/editar/', views.servicio_editar, name='servicio_editar'),
    path('servicios/<int:pk>/eliminar/', views.servicio_eliminar, name='servicio_eliminar'),
    
    # Proyectos
    path('proyectos/', views.proyecto_lista, name='proyecto_lista'),
    path('proyectos/crear/', views.proyecto_crear, name='proyecto_crear'),
    path('proyectos/<int:pk>/', views.proyecto_detalle, name='proyecto_detalle'),
    path('proyectos/<int:pk>/editar/', views.proyecto_editar, name='proyecto_editar'),
    
    # Presupuestos
    path('presupuestos/', views.presupuesto_lista, name='presupuesto_lista'),
    path('presupuestos/crear/', views.presupuesto_crear, name='presupuesto_crear'),
    path('presupuestos/<int:pk>/', views.presupuesto_detalle, name='presupuesto_detalle'),
    
    # Incidencias
    path('incidencias/', views.incidencia_lista, name='incidencia_lista'),
    path('incidencias/crear/', views.incidencia_crear, name='incidencia_crear'),
    path('incidencias/<int:pk>/resolver/', views.incidencia_resolver, name='incidencia_resolver'),
    
    # Autenticación
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    
    # Exportación
    path('proyectos/exportar-excel/', views.exportar_proyectos_excel, name='exportar_proyectos_excel'),
    path('proyectos/exportar-pdf/', views.exportar_proyectos_pdf, name='exportar_proyectos_pdf'),
    
    # AJAX
    path('ajax/calcular-total/', views.calcular_total_presupuesto, name='calcular_total_presupuesto'),
]