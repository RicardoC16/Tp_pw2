## Arquitectura

<img width="1280" height="720" alt="Spa_Arquitectura" src="https://github.com/user-attachments/assets/e2e50f41-dc00-43c2-95ae-d800a37ff1bf" />


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

## Dificultades encontradas

| #   | Dificultad                                                                                                                                                       | Solución                                                                                                                                  |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Migracion de datos en memoria a MySQL: los endpoints estaban escritos para trabajar con diccionarios y listas, y tuvieron que reescribirse para usar queries SQL | Investigacion sobre SQL, consulta de documentación y consultas con la IA para queries especificos                                         |
| 2   | Al tener la conexion y la creacion de tablas en un mismo archivo, las tablas se recreaban cada vez que la app corria                                             | Se separo la logica en dos archivos: db.py para la conexion y db_setup.py para la creacion de tablas, ejecutando este ultimo solo una vez |
| 3   | Entender Javascript viniendo de Python: sintaxis diferente, metodos que no existen en Javascript, y entender como conectar el frontend con la API via fetch      | Investigacion sobre Javascript y practica con ejercicios del repo de la materia                                                           |


