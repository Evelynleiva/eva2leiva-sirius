from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Cliente(models.Model):
    TIPO_CLIENTE_CHOICES = [
        ('empresa', 'Empresa'),
        ('particular', 'Particular'),
        ('gobierno', 'Gobierno'),
    ]
    
    nombre = models.CharField(max_length=200)
    rut = models.CharField(
        max_length=12, 
        unique=True,
        validators=[RegexValidator(r'^\d{7,8}-[0-9kK]$', 'Formato: 12345678-9')]
    )
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    tipo_cliente = models.CharField(max_length=20, choices=TIPO_CLIENTE_CHOICES)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.rut}"
    
    class Meta:
        ordering = ['nombre']

class Servicio(models.Model):
    TIPO_SERVICIO_CHOICES = [
        ('electrico', 'Instalaciones Eléctricas'),
        ('incendio', 'Sistemas de Detección de Incendios'),
        ('construccion', 'Construcción'),
        ('programacion', 'Programación'),
    ]
    
    nombre = models.CharField(max_length=200)
    tipo_servicio = models.CharField(max_length=20, choices=TIPO_SERVICIO_CHOICES)
    descripcion = models.TextField()
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_servicio_display()})"
    
    class Meta:
        ordering = ['tipo_servicio', 'nombre']

class Proyecto(models.Model):
    ESTADO_CHOICES = [
        ('cotizado', 'Cotizado'),
        ('aprobado', 'Aprobado'),
        ('en_proceso', 'En Proceso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
        ('pausado', 'Pausado'),
    ]
    
    PRIORIDAD_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ]
    
    nombre = models.CharField(max_length=200)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='proyectos')
    servicios = models.ManyToManyField(Servicio, related_name='proyectos')
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin_estimada = models.DateField()
    fecha_fin_real = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='cotizado')
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='media')
    presupuesto_total = models.DecimalField(max_digits=12, decimal_places=2)
    costo_real = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='proyectos_asignados')
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='proyectos_creados')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.cliente.nombre}"
    
    class Meta:
        ordering = ['-fecha_creacion']

class Presupuesto(models.Model):
    ESTADO_PRESUPUESTO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('revision', 'En Revisión'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='presupuestos')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='presupuestos', null=True, blank=True)
    numero_presupuesto = models.CharField(max_length=50, unique=True, blank=True)
    descripcion = models.TextField()
    monto_total = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_emision = models.DateField()
    validez_dias = models.IntegerField(default=30)
    estado = models.CharField(max_length=20, choices=ESTADO_PRESUPUESTO_CHOICES, default='pendiente')
    observaciones = models.TextField(blank=True)
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Presupuesto {self.numero_presupuesto} - {self.cliente.nombre}"
    
    def save(self, *args, **kwargs):
        if not self.numero_presupuesto:
            from datetime import datetime
            year = datetime.now().year
            count = Presupuesto.objects.filter(fecha_creacion__year=year).count() + 1
            self.numero_presupuesto = f"PRES-{year}-{count:04d}"
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-fecha_creacion']

class Incidencia(models.Model):
    TIPO_INCIDENCIA_CHOICES = [
        ('tecnica', 'Técnica'),
        ('administrativa', 'Administrativa'),
        ('cliente', 'Del Cliente'),
        ('proveedor', 'Del Proveedor'),
        ('calidad', 'Control de Calidad'),
    ]
    
    PRIORIDAD_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('critica', 'Crítica'),
    ]
    
    ESTADO_CHOICES = [
        ('abierta', 'Abierta'),
        ('en_proceso', 'En Proceso'),
        ('resuelta', 'Resuelta'),
        ('cerrada', 'Cerrada'),
    ]
    
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='incidencias')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo_incidencia = models.CharField(max_length=20, choices=TIPO_INCIDENCIA_CHOICES)
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='media')
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='abierta')
    reportado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='incidencias_reportadas')
    asignado_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='incidencias_asignadas')
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    fecha_resolucion = models.DateTimeField(null=True, blank=True)
    solucion = models.TextField(blank=True)
    
    archivo_adjunto = models.FileField(
        upload_to='incidencias/%Y/%m/',
        null=True,
        blank=True,
        help_text='Subir archivos relacionados (fotos, documentos, etc.)'
    )
    
    def __str__(self):
        return f"{self.titulo} - {self.proyecto.nombre}"
    
    class Meta:
        ordering = ['-fecha_reporte']

class PerfilUsuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('administrador', 'Administrador'),
        ('cliente', 'Cliente'),
        ('empleado', 'Empleado'),
        ('contratista', 'Contratista'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES, default='cliente')
    telefono = models.CharField(max_length=15, blank=True)
    empresa = models.CharField(max_length=200, blank=True)
    rut = models.CharField(max_length=12, blank=True)
    direccion = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username} ({self.get_tipo_usuario_display()})"