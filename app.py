from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

productos = [
    {"id": 1,
     "nombre": "Curso de aleman inicial",
     "precio": 1500,
     "moneda": "Euro"},
     {"id": 2,
     "nombre": "Curso de ruso intermedio",
     "precio": 2500,
     "moneda": "Rublo"},
     {"id": 3,
     "nombre": "Curso de portugues avanzado",
     "precio": 3500,
     "moneda": "Real"},
     {"id": 4,
     "nombre": "Curso de ingles avanzado",
     "precio": 2950,
     "moneda": "Dolar"},
     {"id": 5,
     "nombre": "Curso de chino mandarin inicial",
     "precio": 6500,
     "moneda": "Yuan"}
]

carrito = []

@app.route('/productos', methods = ["GET"])
def mostrar_productos():
    """
    Retorna la lista de productos disponibles
    ---
    responses:
      200:
        description: Lista de productos obtenida correctamente
        examples:
          application/json:
            [
              {
                "id": 1,
                "nombre": "Curso de aleman inicial",
                "precio": 1500,
                "moneda": "Euro"
              },
              {
                "id": 2,
                "nombre": "Curso de ruso intermedio",
                "precio": 2500,
                "moneda": "Rublo"
              }
            ]
    """
    return jsonify(productos)

@app.route('/carrito', methods=["GET"])
def mostrar_carrito():
    """
    Muestra el carrito con el total calculado
    ---
    responses:
        200:
            description: "muestra productos del carrito con el total"
            examples:
                application/json:
                    carrito:
                        - id: 2
                          cantidad: 3
                    total: 4500
              
    """
    total = 0
    for prod_carrito in carrito:
        for prod_lista in productos:
            if prod_carrito["id"] == prod_lista["id"]:
                subtotal = prod_lista["precio"] * prod_carrito["cantidad"]
                total += subtotal
    return jsonify({"carrito": carrito, "total": total})

@app.route('/carrito', methods = ["POST"])
def agregar_producto():
    """
    Agrega un producto al carrito
    ---
    parameters:
        - name: datos_prod
          in: body
          required: true
          schema:
            type: object
            properties:
                id: 
                    type: integer
                cantidad:
                    type: integer
    responses:
        200:
            description: Muestra un mensaje de exito al agregar un producto al carrito
            examples:
                application/json:
                    Mensaje: "Producto añadido existosamente"
        404:
            description: Muestra un mensaje de error cuando se intenta agregar un id que no existe
            examples:
                application/json:
                    Error: "Id inexistente"

    """
    datos_prod = request.get_json()
    id = datos_prod["id"]
    cantidad = datos_prod["cantidad"]
    id_existe = False
    for prod in productos:
        if id == prod["id"]:
            id_existe = True
    if id_existe == False:
        return jsonify({"Error": "Id inexistente"}), 404
    else:
        id_de_carrito = False 
        for prod in carrito:
            if id == prod["id"]:
                id_de_carrito = True
                prod["cantidad"] += cantidad
        if id_de_carrito == False:
            carrito.append({"id": id, "cantidad": cantidad})
    return jsonify({"Mensaje": "Producto añadido existosamente"}), 200

@app.route('/carrito', methods = ["DELETE"])
def eliminar_producto():

    """
    Elimina un producto del carrito
    ---
    parameters:
        - name: datos_prod
          in: body
          required: true
          schema:
            type: object
            properties:
                id: 
                    type: integer
    responses:
        200:
            description: Muestra un mensaje de exito al eliminar un producto del carrito
            examples:
                application/json:
                    Mensaje: "Producto eliminado exitosamente"
        404:
            description: Muestra un mensaje de error cuando se intenta eliminar un id que no existe
            examples:
                application/json:
                    Error: "Id inexistente"

    """

    datos_prod = request.get_json()
    id = datos_prod["id"]
    id_a_eliminar = False
    for prod in carrito:
        if id == prod["id"]:
            id_a_eliminar = True
            carrito.remove(prod)
    if id_a_eliminar == False:
        return jsonify({"Error": "Id inexistente"}), 404
    
    return jsonify({"Mensaje": "Producto eliminado exitosamente"}), 200
            

if __name__ == "__main__":
    app.run(debug=True)