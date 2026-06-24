# API de Carrito de Compras

API REST desarrollada en Flask que permite gestionar productos y un carrito de compras. Incluye operaciones para listar, agregar y eliminar productos,
junto con documentación interactiva mediante Swagger.

## Tecnologías

- Python
- Flask
- Flasgger (Swagger)
- MySQL
- HTML
- CSS
- Bootstrap
- JavaScript
- Cypress (Testing automatico)

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

## Dificultades encontradas

| #   | Dificultad                                                                                                                                                       | Solución                                                                                                                                  |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Migracion de datos en memoria a MySQL: los endpoints estaban escritos para trabajar con diccionarios y listas, y tuvieron que reescribirse para usar queries SQL | Investigacion sobre SQL, consulta de documentación y consultas con la IA para queries especificos                                         |
| 2   | Al tener la conexion y la creacion de tablas en un mismo archivo, las tablas se recreaban cada vez que la app corria                                             | Se separo la logica en dos archivos: db.py para la conexion y db_setup.py para la creacion de tablas, ejecutando este ultimo solo una vez |
| 3   | Entender Javascript viniendo de Python: sintaxis diferente, metodos que no existen en Javascript, y entender como conectar el frontend con la API via fetch      | Investigacion sobre Javascript y practica con ejercicios del repo de la materia                                                           |

## Arquitectura

<img width="1280" height="720" alt="Spa_Arquitectura" src="https://github.com/user-attachments/assets/10b38e10-32ea-43be-b582-2a7a2c0eed72" />
