# Sistema de Gestión Empresarial - Sirius LyCh

Sistema web integral desarrollado en **Django (Python)** para la gestión administrativa de proyectos, clientes y presupuestos empresariales.

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.x, Django Framework.
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap.
* **Base de Datos:** Relacional (SQL / PostgreSQL / MySQL).
* **Control de Versiones:** Git & GitHub.

## 📋 Funcionalidades Principales

* Autenticación y gestión de usuarios/roles.
* Módulo CRUD de administración de clientes.
* Control y seguimiento de proyectos empresariales.
* Generación y gestión de presupuestos.

## 🚀 Instalación y Configuración Local

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/Evelynleiva/eva2leiva-sirius.git](https://github.com/Evelynleiva/eva2leiva-sirius.git)
   python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
