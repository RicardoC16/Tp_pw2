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

## Dificultades encontradas

| #   | Dificultad                                                                                                                                                        | Solución                                                                                                                                  |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Migración de datos en memoria a MySQL: los endpoints estaban escritos para trabajar con diccionarios y listas, y tuvieron que reescribirse para usar queries SQL  | Investigación sobre SQL, consulta de documentación y uso de IA para queries específicas                                                   |
| 2   | Al tener la conexión y la creación de tablas en un mismo archivo, las tablas se recreaban cada vez que la app corría                                              | Se separó la lógica en dos archivos: db.py para la conexión y db_setup.py para la creación de tablas, ejecutando este último solo una vez |
| 3   | Dificultad con JavaScript viniendo de Python: sintaxis diferente, métodos que no existen en Javascript, y entender cómo conectar el frontend con la API via fetch | Investigación sobre Javascript y práctica con ejercicios solicitados a la IA                                                              |

