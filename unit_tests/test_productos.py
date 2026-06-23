import pytest
from app import app
from app import carrito

#fixture crea un cliente de prueba para los tests
@pytest.fixture
def cliente():
    app.config["TESTING"] = True #indicamos a la app que estamos en modo test
    with app.test_client() as cliente: #abre un cliente de prueba y lo cierra al terminar
        yield cliente #seria como un return,pero la diferencia es que pausa la funcion

def test_obtener_productos(cliente):
    respuesta = cliente.get("/productos")
    assert(respuesta.status_code == 200)
    assert(len(respuesta.get_json())==5)

@pytest.fixture
def carrito_limpio():
    # antes del test
    yield
    carrito.clear()

def test_agregar_producto_con_id_inexistente(cliente):
    respuesta = cliente.post("/carrito", json={"id":99, "cantidad": 3})
    assert(respuesta.status_code == 404)
    assert ("Error" in respuesta.get_json())

def test_agregar_producto_que_no_esta_en_carrito(cliente):
    respuesta = cliente.post("/carrito", json={"id":2, "cantidad": 1})
    assert(respuesta.status_code == 200)
    assert ("Mensaje" in respuesta.get_json())

def test_agregar_producto_que_ya_esta_en_carrito(cliente, carrito_limpio):
    respuesta = cliente.post("/carrito", json={"id":2, "cantidad": 1})
    respuesta = cliente.post("/carrito", json={"id":2, "cantidad": 1})
    assert(respuesta.status_code == 200)
    assert ("Mensaje" in respuesta.get_json())

def test_eliminar_producto_con_id_inexistente(cliente):
    respuesta = cliente.delete("/carrito", json={"id":99, "cantidad":2})
    assert(respuesta.status_code == 404)
    assert("Error" in respuesta.get_json())

def test_eliminar_correctamente_un_producto(cliente, carrito_limpio):
    respuesta = cliente.post("/carrito", json={"id":4, "cantidad": 2})
    respuesta = cliente.delete("/carrito", json={"id":4})
    assert(respuesta.status_code == 200)
    assert("Mensaje" in respuesta.get_json())

def test_mostrar_carrito_con_total(cliente, carrito_limpio):
    respuesta = cliente.post("/carrito", json={"id":4, "cantidad": 2})
    respuesta = cliente.post("/carrito", json={"id":1, "cantidad": 1})
    respuesta = cliente.get("/carrito")
    assert(respuesta.status_code == 200)
    assert(respuesta.get_json()["total"] == 7400)