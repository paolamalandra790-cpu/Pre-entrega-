import pytest
import requests

@pytest.mark.api
def test_users_api():
    url = "https://reqres.in/api/users?page=1"
    respuesta = requests.get(url)
    assert respuesta.status_code == 200
    datos = respuesta.json()["data"]
    assert len(datos) > 0
    for usuario in datos:
        assert "id" in usuario
        assert "email" in usuario
        assert "first_name" in usuario
        assert "last_name" in usuario
        assert usuario["avatar"].endswith(".jpg")
