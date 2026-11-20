import requests

# Pruebas de API hechas por Romy - usuarios de prueba

def test_lista_usuarios_funciona():
    url = "https://jsonplaceholder.typicode.com/users"
    respuesta = requests.get(url)
    assert respuesta.status_code == 200
    assert len(respuesta.json()) > 0

def test_buscar_usuario_3():
    url = "https://jsonplaceholder.typicode.com/users/3"
    respuesta = requests.get(url)
    datos = respuesta.json()
    assert datos["id"] == 3
    assert "email" in datos

def test_crear_usuario_romy():
    url = "https://jsonplaceholder.typicode.com/users"
    nuevo_usuario = {"name": "Romy Malandra", "email": "romy.paverini@test.com"}
    respuesta = requests.post(url, json=nuevo_usuario)
    assert respuesta.status_code == 201
    assert respuesta.json()["name"] == "Romy Malandra"
