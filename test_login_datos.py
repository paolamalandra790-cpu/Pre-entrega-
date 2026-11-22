import pytest
from Páginas.login_page import LoginPage
from utils.datos import leer_datos_login

@pytest.mark.parametrize("usuario, clave, resultado_esperado", leer_datos_login())
def test_login_con_datos(driver, usuario, clave, resultado_esperado):
    login = LoginPage(driver)
    login.abrir()
    login.iniciar_sesion(usuario, clave)
    if resultado_esperado == "ok":
        assert "inventory" in driver.current_url
    else:
        assert "inventory" not in driver.current_url
