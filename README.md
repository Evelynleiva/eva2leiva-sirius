# 🏢 Sistema de Gestión Empresarial - Sirius LyCh Spa

Sistema web completo de gestión empresarial desarrollado con Django 5.2, diseñado para administrar proyectos, clientes, servicios, presupuestos e incidencias en una empresa multirubro.

![Estado](https://img.shields.io/badge/Estado-En%20Producción-success)
![Django](https://img.shields.io/badge/Django-5.2-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)

## 📋 Descripción

Sistema integral desarrollado para gestionar operaciones de una empresa que ofrece servicios de instalaciones eléctricas, construcción, detección de incendios y programación. El sistema permite administrar el ciclo completo de proyectos desde la cotización hasta la entrega final, con seguimiento de incidencias y gestión de clientes.

## ✨ Características Principales

### 🔐 Autenticación y Autorización
- Sistema de login con perfiles diferenciados
- Tres tipos de usuario: Administradores, Trabajadores y Clientes
- Control de acceso basado en roles y permisos por grupos
- Panel administrativo personalizado según tipo de usuario

### 📊 Gestión de Proyectos
- Creación y seguimiento de proyectos
- Estados personalizables (En progreso, Completado, En espera, Cancelado)
- Prioridades (Alta, Media, Baja)
- Asignación de responsables
- Fechas de inicio y fin estimadas
- Panel de control con vista general de proyectos activos

### 👥 Módulo de Clientes
- Registro completo de clientes (personas y empresas)
- Validación automática de RUT chileno
- Historial de proyectos por cliente
- Información de contacto y datos de facturación

### 🛠️ Catálogo de Servicios
- Visualización pública de servicios ofrecidos
- Filtros por categoría:
  - Instalaciones Eléctricas
  - Construcción
  - Detección de Incendios
  - Programación y TI
- Galería de imágenes por servicio
- Descripciones detalladas

### 💰 Sistema de Presupuestos
- Generación de presupuestos con numeración automática
- Cálculo de subtotales, IVA y totales
- Exportación a PDF con formato profesional
- Estados de presupuesto (Pendiente, Aprobado, Rechazado)
- Conversión de presupuestos aprobados en proyectos

### 🚨 Gestión de Incidencias
- Registro de problemas y solicitudes
- Seguimiento de estado (Abierta, En proceso, Resuelta, Cerrada)
- Priorización de incidencias
- Asignación a responsables
- Historial de resolución

### 📄 Generación de Documentos
- Exportación de presupuestos a PDF con ReportLab
- Exportación de datos a Excel con openpyxl
- Plantillas personalizadas con logo y branding
- Informes de proyectos y clientes

### 🎨 Interfaz de Usuario
- Diseño responsive con Bootstrap 5
- Interfaz moderna con gradientes y animaciones CSS
- Experiencia de usuario optimizada
- Dashboards intuitivos
- Navegación fluida entre módulos

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.x**
- **Django 5.2** - Framework web
- **MySQL 8.0** - Base de datos
- **ReportLab** - Generación de PDFs
- **openpyxl** - Exportación a Excel

### Frontend
- **HTML5**
- **CSS3** (Custom + Gradientes + Animaciones)
- **Bootstrap 5** - Framework CSS
- **JavaScript / jQuery** - Interactividad

### Otras Librerías
- **Pillow** - Manejo de imágenes
- **python-decouple** - Gestión de variables de entorno
- **mysqlclient** - Conector MySQL

## 📦 Instalación

### Requisitos Previos
- Python 3.8 o superior
- MySQL 8.0 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/Evelynleiva/eva2leiva-sirius.git
cd eva2leiva-sirius

Crear entorno virtual

bashpython -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

Instalar dependencias

bashpip install -r requirements.txt

Configurar base de datos

bash# Crear base de datos en MySQL
mysql -u root -p
CREATE DATABASE sirius_lych;
EXIT;

Configurar variables de entorno
Copia el archivo .env.example y renómbralo a .env:

bashcp .env.example .env
Edita el archivo .env con tus datos reales:
envSECRET_KEY=tu_clave_secreta_aqui
DEBUG=True
DB_NAME=sirius_db
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=3306

Ejecutar migraciones

bashpython manage.py makemigrations
python manage.py migrate

Crear superusuario

bashpython manage.py createsuperuser

Ejecutar servidor de desarrollo

bashpython manage.py runserver

Acceder al sistema
Abrir navegador en: http://localhost:8000

🗂️ Estructura del Proyecto
eva2leiva-sirius/
│
├── eva2leiva/              # Configuración principal del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── siriusApp/              # Aplicación principal
│   ├── models.py           # Modelos de datos
│   ├── views.py            # Vistas y lógica de negocio
│   ├── forms.py            # Formularios
│   ├── urls.py             # Rutas de la aplicación
│   └── templates/          # Plantillas HTML
│
├── static/                 # Archivos estáticos
│   ├── css/
│   ├── js/
│   └── img/
│
├── media/                  # Archivos subidos por usuarios
│
├── requirements.txt        # Dependencias del proyecto
├── manage.py
└── README.md
💾 Modelo de Datos
El sistema cuenta con los siguientes modelos principales:

Usuario - Extensión del modelo User de Django
Cliente - Información de clientes
Proyecto - Proyectos en gestión
Servicio - Catálogo de servicios
Presupuesto - Cotizaciones y presupuestos
Incidencia - Registro de problemas y solicitudes
Categoría - Clasificación de servicios

🔒 Seguridad

Autenticación basada en sesiones de Django
Protección CSRF en todos los formularios
Validación de datos en backend y frontend
Control de acceso por roles
Sanitización de inputs del usuario
Protección contra SQL Injection (ORM de Django)
Variables de entorno para datos sensibles

📱 Funcionalidades por Rol
Administrador

Acceso completo a todos los módulos
Gestión de usuarios y permisos
Configuración del sistema
Reportes y estadísticas globales

Trabajador

Gestión de proyectos asignados
Registro de avances
Atención de incidencias
Generación de presupuestos

Cliente

Vista de proyectos propios
Consulta de presupuestos
Reporte de incidencias
Visualización de servicios

🚀 Características Futuras

Integración con pasarelas de pago
Notificaciones por email
App móvil (React Native)
Sistema de chat en tiempo real
Firma digital de documentos
Integración con API de facturación electrónica
Dashboard de analíticas avanzadas

👩‍💻 Autora
Evelyn Leiva Pino

GitHub: @Evelynleiva
LinkedIn: linkedin.com/in/evelyn-leiva-pino
Email: evelynleiva.03@gmail.com
Ubicación: Los Ángeles, Chile

📄 Licencia
Este proyecto es de código privado y fue desarrollado para uso comercial de Sirius LyCh Spa.

Desarrollado con Django | Sistema en producción desde 2024
