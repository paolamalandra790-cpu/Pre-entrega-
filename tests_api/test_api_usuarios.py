import requests

def test_get_usuarios_devuelve_200():
    url = "https://jsonplaceholder.typicode.com/users"
    respuesta = requests.get(url)
    assert respuesta.status_code == 200

def test_get_usuario_existe():
    url = "https://jsonplaceholder.typicode.com/users/1"
    respuesta = requests.get(url)
    datos = respuesta.json()
    assert respuesta.status_code == 200
    assert datos["id"] == 1
    assert "name" in datos
