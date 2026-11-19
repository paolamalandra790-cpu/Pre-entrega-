import pytest
import requests

@pytest.mark.api
@pytest.mark.parametrize("nombre, trabajo", [
    ("Romy", "QA Tester"),
    ("Paola", "Automatizadora"),
    ("Romy Malandra", "Estudiante QA"),
])
def test_create_user_api(nombre, trabajo):
    url = "https://reqres.in/api/users"
    datos = {"name": nombre, "job": trabajo}
    respuesta = requests.post(url, json=datos)
    assert respuesta.status_code == 201
    assert "createdAt" in respuesta.json()
    assert "2026" in respuesta.json()["createdAt"]
