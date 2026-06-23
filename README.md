# API de Carrito de Compras

API REST desarrollada en Flask que permite gestionar productos y un carrito de compras. Incluye operaciones para listar, agregar y eliminar productos,
junto con documentación interactiva mediante Swagger.

## Tecnologías

- Python
- Flask
- Flasgger (Swagger)

## Instalación

- Instalar dependencias detalladas en requirements.txt

## Ejecutar la API

1- Correr el servidor
python app.py

2- Luego ingresar a: http://127.0.0.1:5000/
para visualizar el sitio web

## Documentación

La documentación con Swagger está disponible en:

http://127.0.0.1:5000/apidocs/

## Endpoints

### GET /productos

Obtiene la lista de productos disponibles

### GET /carrito

Muestra el carrito con el total

### POST /carrito

Agrega un producto al carrito

### DELETE /carrito

Elimina un producto del carrito
