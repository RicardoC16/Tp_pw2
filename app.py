from flask import Flask, jsonify, request, render_template
from flasgger import Swagger
from db import mydb

mycursor = mydb.cursor(dictionary=True)

app = Flask(__name__)
swagger = Swagger(app)

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
    mycursor.execute('SELECT * FROM productos')
    cursos = mycursor.fetchall()
    return jsonify(cursos)

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
    mycursor.execute('SELECT carrito.id, carrito.cantidad, productos.precio, productos.nombre FROM carrito JOIN productos ON carrito.id = productos.id')
    carrito = mycursor.fetchall()
    total = 0
    for prod in carrito: 
        total += prod["cantidad"] * prod["precio"]
    return jsonify({"carrito": carrito, "total":total})



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
    datos_prod = request.get_json() #get_json lee el body de una solicitud HTTP
    id = datos_prod["id"]

    #verifico que el id que se manda es de un producto que exista
    mycursor.execute('SELECT * FROM productos where id = %s', (id,))
    result = mycursor.fetchone()

    if result == None:
        return jsonify({"Error": "Id Erroneo"}), 404
    else:
        mycursor.execute('SELECT * FROM carrito where id = %s', (id,))
        producto = mycursor.fetchone()
        if producto != None:
            sql = 'UPDATE carrito set cantidad = cantidad + 1 WHERE id = %s'
            val = (id, )
            mycursor.execute(sql, val)
            mydb.commit()
        else:
            sql =  'INSERT INTO carrito (id, cantidad) VALUES (%s, %s)'
            val = (id, 1)
            mycursor.execute(sql, val)
            mydb.commit()

        return jsonify({"Mensaje": "Producto agregado exitosamente"}), 200


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
    mycursor.execute('SELECT * FROM carrito where id = %s', (id,))
    producto = mycursor.fetchone()
    if producto == None:
        return jsonify({"Error": "Id Erroneo"}), 404
    else:
        if producto["cantidad"] > 1:
            sql = 'UPDATE carrito set cantidad = cantidad - 1 WHERE id = %s'
            val = (id, )
            mycursor.execute(sql, val)
            mydb.commit()
        else:   
            sql = "DELETE FROM carrito WHERE id = %s"
            val = (id,)
            mycursor.execute(sql, val)
            mydb.commit()
        
        return jsonify({"Mensaje": "Producto eliminado exitosamente"}), 200
    

@app.route('/carrito/vaciar', methods=["DELETE"])
def vaciar_carrito():
    """
    Vacía todo el carrito (uso interno para testing)
    ---
    responses:
        200:
            description: Muestra un mensaje de éxito al vaciar el carrito
            examples:
                application/json:
                    Mensaje: "Carrito vaciado exitosamente"
    """

    sql = 'DELETE FROM carrito'
    mycursor.execute(sql)
    mydb.commit()

    return jsonify({"Mensaje": "Carrito vaciado exitosamente"}), 200

@app.route('/', methods = ["GET"])
def devolver_index():
    return render_template("index.html")

@app.route('/cart', methods = ["GET"])
def devolver_carrito():
    return render_template("carrito.html")

if __name__ == "__main__": # Verifica que se este corriendo desde el main y no desde un import
    app.run(debug=True)    # Arranca el servidor con modo debug, recarga automaticamente cada vez que se  salva, sin necesidad de cortar y volver a arrancar el servidor

