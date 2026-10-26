# Informe de Avance y Estructura del Proyecto: Tienda Kodda

**Fecha:** 22 de Octubre, 2026  
**Proyecto:** Sistema de Promoción de Productos y Servicios (Tienda Kodda)  
**Tecnología Principal:** Django (Python) + SQLite + Bootstrap  

---

## 1. Resumen Ejecutivo
Se ha implementado con éxito la arquitectura base del proyecto **Tienda Kodda**, correspondiente al backend relacional, la persistencia de datos mediante ORM, el sistema de autenticación de Django y una interfaz de administración personalizada para la gestión de productos y categorías (CRUD) con estilos responsive integrados vía **Bootstrap 5**.

---

## 2. Herramientas y Stack Tecnológico

* **Lenguaje de Programación:** Python 3.12+
* **Framework Web:** Django 6.1.2 (Patrón MVT: Model-View-Template)
* **Base de Datos:** SQLite3 (Integrada nativamente mediante el ORM de Django)
* **Diseño e Interfaz (UI/UX):** Bootstrap 5.3 (Vía CDN) + Bootstrap Icons
* **Entorno Virtual:** `venv` (Aislamiento de dependencias local)

---

## 3. Funcionalidades Implementadas

1. **Modelos de Datos Relacionales (`models.py`):**
   * **`Categoria`:** ID, Nombre, Descripción.
   * **`Producto`:** ID, Categoría (Relación `ForeignKey` 1:N), Nombre, Precio, Stock, Imagen (`ImageField`), Fecha de Creación.

2. **Operaciones CRUD Completas:**
   * **Crear:** Formularios dinamizados con `ModelForm` (`form_producto.html`, `form_categoria.html`).
   * **Leer/Listar:** Tablas interactivas para gestión de inventario y categorías (`lista_productos.html`, `lista_categorias.html`).
   * **Actualizar:** Vistas parametrizadas para modificación de registros existentes.
   * **Eliminar:** Confirmación de seguridad mediante modal/pantalla previa (`confirmar_eliminacion.html`).

3. **Búsqueda y Filtros Dinámicos:**
   * Implementación de motor de búsqueda mediante solicitudes `GET` con filtros `icontains` y consultas complejas `Q` sobre nombre y categoría.

4. **Seguridad y Control de Acceso:**
   * Protección de vistas administrativas mediante el decorador `@login_required` y redirección automática al sistema de autenticación nativo de Django.

---

## 4. Estructura Exacta del Proyecto

```text
tienda_kodda/
│
├── db.sqlite3                       # Base de datos SQLite generada tras migraciones
├── manage.py                        # Gestor de comandos de Django
│
├── tienda_kodda/                    # Configuración Global del Proyecto
│   ├── __init__.py
│   ├── settings.py                  # Apps registradas (INSTALLED_APPS), BD y Media URLs
│   ├── urls.py                      # Enrutador principal
│   ├── wsgi.py
│   └── asgi.py
│
└── productos/                       # Aplicación Principal
    ├── migrations/                  # Historial de migraciones de la BD
    ├── templates/                   # Directorio raíz de plantillas
    │   └── productos/               # Subcarpeta obligatoria para Namespace de Django
    │       ├── catalogo.html        # [Pendiente Frontend] Vista pública comercial
    │       ├── lista_productos.html # Panel Admin Personalizado (Tabla de Productos)
    │       ├── lista_categorias.html# Panel Admin Personalizado (Tabla de Categorías)
    │       ├── form_producto.html   # Formulario de Alta/Edición de Productos
    │       ├── form_categoria.html  # Formulario de Alta/Edición de Categorías
    │       └── confirmar_eliminacion.html # Pantalla de confirmación de borrado
    │
    ├── __init__.py
    ├── admin.py                     # Configuración del Admin NATIVO de Django
    ├── apps.py                      # Registro e Identificación de la app 'productos'
    ├── forms.py                     # Declaración de Django ModelForms
    ├── models.py                    # Modelos de BD (Categoria y Producto)
    ├── tests.py
    ├── urls.py                      # Enrutamiento local de la app productos
    └── views.py                     # Lógica de negocio (Controladores)
```

---

## 5. Estado Actual y Próximos Pasos

* **Estado Backend/BD:** 100% Funcional y Sincronizado.
* **Estado Admin Personalizado:** 100% Funcional y Diseñado con Bootstrap.
* **Pendiente (Próxima Sesión):**
  1. Conectar y pulir la vista pública comercial (`catalogo.html`) para los usuarios/clientes finales (tarjetas de productos, banner comercial, carrito simulado).
  2. Ajustar archivos estáticos (`MEDIA_URL` / `MEDIA_ROOT`) para la visualización de imágenes subidas desde local.