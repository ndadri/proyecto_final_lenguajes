# GamingStore API Backend

¡Bienvenido al backend de **GamingStore**! Una robusta API RESTful desarrollada en Python utilizando el framework **Flask**, diseñada bajo una arquitectura limpia en capas y protegida con un avanzado sistema de autenticación basado en **JSON Web Tokens (JWT)** y control de acceso por roles (RBAC).

Este sistema provee el soporte completo para la gestión de inventario de videojuegos, catálogo de servicios técnicos, flujos transaccionales de compras automatizadas con reducción de stock, y calificaciones de usuarios. Está optimizado para integrarse perfectamente con un frontend desarrollado en **Angular**.

---

## Características Principales

* **Arquitectura Limpia en Capas**: Desacoplamiento total mediante modelos de base de datos (`Models`), repositorios de persistencia (`Repositories`), lógica de negocio (`Services`) y controladores de endpoints (`Routes`).
* **Autenticación Segura**: Implementación de JSON Web Tokens (JWT) con firmas de seguridad HS256 y expiración controlada.
* **Control de Acceso Basado en Roles (RBAC)**: Gestión granular de permisos mediante decoradores personalizados para tres niveles de usuarios:
    * `admin`: Control total del sistema (CRUD completo de usuarios, videojuegos, servicios, categorías, plataformas y eliminación de reseñas).
    * `vendedor`: Gestión operativa (creación y edición de videojuegos/servicios, actualización de stock).
    * `cliente`: Consumo e interacción (visualización del catálogo, procesamiento de compras transaccionales y publicación de reseñas).
* **Seguridad de Contraseñas**: Encriptación irreversible de credenciales en la base de datos utilizando algoritmos de hash criptográfico seguros mediante `werkzeug.security`.
* **Integración Transaccional**: Procesamiento de órdenes de compra con validación estricta de existencias en tiempo real y descuento automático de stock mediante transacciones seguras de base de datos.

---

## Stack Tecnológico

* **Lenguaje:** Python 3.x
* **Framework Web:** Flask
* **ORM (Mapeo Objeto-Relacional):** Flask-SQLAlchemy
* **Manejador de Base de Datos (RDBMS):** Microsoft SQL Server
* **Herramienta de Conectividad:** PyODBC / SQL Server Authentication
* **Seguridad y Tokens:** PyJWT & Werkzeug Security
* **Automatización:** GNU Make (Makefile) / Scripts por lotes para Windows (.bat)

---

## Estructura del Proyecto

El backend se organiza bajo el patrón arquitectónico de diseño guiado por dominios y separación de responsabilidades:

```text
PROYECTO_FINAL_LENGUAJES/
│
├── database/                # Configuración de persistencia
│   ├── db.py                # Instancia global de SQLAlchemy
│   └── models.py            # Definición de tablas y relaciones relacionales
│
├── repositories/            # Capa de datos (Consultas directas SQL/ORM)
│   ├── categoria_repository.py
│   ├── plataforma_repository.py
│   ├── resena_repository.py
│   ├── servicio_repository.py
│   ├── usuario_repository.py
│   ├── venta_repository.py
│   └── videojuego_repository.py
│
├── services/                # Capa de negocio (Validaciones y lógica)
│   ├── categoria_service.py
│   ├── plataforma_service.py
│   ├── resena_service.py
│   ├── servicio_service.py
│   ├── usuario_service.py
│   ├── venta_service.py
│   └── videojuego_service.py
│
├── routes/                  # Capa de presentación (Endpoints HTTP / Blueprints)
│   ├── categoria_routes.py
│   ├── plataforma_routes.py
│   ├── resena_routes.py
│   ├── servicio_routes.py
│   ├── usuario_routes.py
│   ├── venta_routes.py
│   └── videojuego_routes.py
│
├── utils/                   # Herramientas transversales y seguridad
│   └── decorators.py        # Guardia interceptor de seguridad para verificar JWT y Roles
│
├── venv/                    # Entorno virtual de Python
├── .env                     # Variables de entorno confidenciales (Base de datos y llaves)
├── app.py                   # Archivo central de inicialización del servidor
├── Makefile                 # Automatización de tareas para entornos compatibles
├── run.bat                  # Lanzador automatizado nativo para entornos Windows
└── requirements.txt         # Listado oficial de dependencias del ecosistema
```
## Configuración e Instalación
1. Clonar el repositorio y acceder al directorio
cd PROYECTO_FINAL_LENGUAJES
2. Configurar el Entorno Virtual (Venv)
Si deseas recrear el entorno desde cero de forma manual:
python -m venv venv
Para activarlo en Windows (PowerShell):
.\venv\Scripts\Activate.ps1
Para activarlo en Windows (Git Bash / Linux / Mac):
source venv/Scripts/activate
3. Instalar Dependencias
Instala todas las librerías necesarias con el siguiente comando:
pip install -r requirements.txt
4. Configurar Variables de Entorno (.env)
Crea un archivo .env en la raíz del proyecto y define los siguientes parámetros de conexión (conecta de forma segura a SQL Server utilizando autenticación de Windows o de SQL Server):
DATABASE_URL=mssql+pyodbc://@localhost/GamingStoreDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes
SECRET_KEY=tu_clave_secreta_altamente_confidencial_2026
Automatización con Atajos de Comando
Para facilitar la ejecución, el proyecto cuenta con dos herramientas de automatización que simplifican el flujo de trabajo sin requerir la activación manual de rutas internas.

Opción A: Utilizando el Makefile (Sistemas Linux, Mac o Windows configurados)
make install: Instala automáticamente todas las dependencias base del proyecto.

make run: Inicia el servidor de desarrollo de Flask apuntando al Python del entorno virtual.

make freeze: Guarda el estado actual de las dependencias instaladas en el archivo requirements.txt.

make clean: Elimina recursivamente todas las carpetas temporales de caché __pycache__.

Opción B: Utilizando el script nativo de Windows (run.bat)
Si experimentas restricciones con las políticas de PowerShell o comandos no reconocidos de Make, simplemente haz doble clic sobre el archivo run.bat o ejecútalo desde tu consola:
.\run.bat
Este archivo ejecutará el backend directamente cargando de forma transparente el binario correcto de tu entorno virtual.
Catálogo Completo de Endpoints de la API
Todas las peticiones base deben dirigirse al prefijo /api. Las rutas protegidas requieren que se envíe el token JWT en las cabeceras HTTP de la siguiente manera:

Authorization: Bearer <TU_TOKEN_JWT>
Notas de Seguridad Importantes
Protección de Datos Sensibles: Las contraseñas nunca deben almacenarse ni manipularse en texto plano dentro de la capa lógica. La capa de presentación las recibe y el servicio las hashea inmediatamente antes de interactuar con el repositorio.

Fuga de Datos Criptográficos: La clave SECRET_KEY definida en el archivo .env es el pilar de seguridad de los tokens JWT. Cambie el valor por defecto en producción; si la firma se ve comprometida, todo el sistema de roles quedará expuesto a falsificaciones de identidad.