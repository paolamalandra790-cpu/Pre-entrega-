import pytest
import requests

@pytest.mark.api
@pytest.mark.parametrize("email, password, esperado", [
    ("eve.holt@reqres.in", "cityslicka", 200),
    ("eve.holt@reqres.in", None, 400),
])
def test_login_api(email, password, esperado):
    url = "https://reqres.in/api/login"
    datos = {"email": email}
    if password:
        datos["password"] = password
    respuesta = requests.post(url, json=datos)
    assert respuesta.status_code == esperado
    if esperado == 200:
        assert "token" in respuesta.json()
