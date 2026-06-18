# TecnoHogar

## Descripción del Proyecto

TecnoHogar es una tienda virtual desarrollada con Django que permite a los usuarios registrarse, iniciar sesión, recuperar su contraseña, visualizar productos tecnológicos, agregarlos al carrito de compras y gestionar sus pedidos. El sistema cuenta con diferentes categorías de productos como computadores, tablets y productos en oferta, ofreciendo una experiencia de compra sencilla e intuitiva.

---

## Integrantes

- Rolando Barela Pérez
- (Agregar demás integrantes si aplica)

---

## Tecnologías Utilizadas

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Backend
- Python
- Django

### Base de Datos
- SQLite3 (desarrollo)
- PostgreSQL (producción)

### Despliegue
- Render

---

## Instalación

### 1. Diseño y Maquetación

Inicialmente se realizó el diseño de la interfaz gráfica utilizando HTML, CSS y Bootstrap para definir la estructura visual de la tienda virtual.

### 2. Instalación de Django

```bash
pip install django
```

### 3. Creación del Proyecto

```bash
django-admin startproject tecnohogar
```

### 4. Creación de la Aplicación

```bash
python manage.py startapp tienda
```

### 5. Organización de Carpetas

Se organizaron las carpetas de plantillas y archivos estáticos para mantener una estructura ordenada del proyecto.

```text
templates/
static/
├── css/
├── js/
└── img/
```

### 6. Configuración de Archivos Estáticos

Se configuró Django para cargar archivos CSS, JavaScript e imágenes mediante:

```html
{% load static %}
```

### 7. Desarrollo de la Lógica de Negocio

Se implementaron las funcionalidades de:

- Registro de usuarios.
- Inicio de sesión.
- Recuperación de contraseña.
- Visualización de productos.
- Carrito de compras.
- Historial de pedidos.

### 8. Creación de la Base de Datos

Se definieron los modelos necesarios y posteriormente se generaron las migraciones.

```bash
python manage.py makemigrations
python manage.py migrate
```

### 9. Creación del Administrador

```bash
python manage.py createsuperuser
```

### 10. Ejecución Local

```bash
python manage.py runserver
```

Acceder desde:

```text
http://127.0.0.1:8000
```

### 11. Despliegue

Finalmente se configuró el proyecto para producción mediante Render, utilizando PostgreSQL como base de datos y los archivos necesarios para el despliegue.

---

## Ejecución

Para ejecutar el proyecto localmente:

```bash
python manage.py runserver
```

Luego abrir en el navegador:

```text
http://127.0.0.1:8000
```

---

## Pruebas

Se realizaron pruebas de:

- Registro de usuarios.
- Inicio de sesión.
- Recuperación de contraseña.
- Visualización de productos.
- Funcionamiento del carrito de compras.
- Historial de pedidos.
- Carga de archivos estáticos.
- Despliegue en producción.

---

## Video

Enlace del video de sustentación:

(https://youtu.be/OlnS3BpkMx4)
