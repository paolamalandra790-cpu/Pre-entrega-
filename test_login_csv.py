import pytest
from pages.login_page import LoginPage
from utils.datos import leer_csv_login

CASOS_LOGIN = leer_csv_login("datos/login.csv")

@pytest.mark.parametrize("usuario, clave, debe_funcionar, descripcion", CASOS_LOGIN)
def test_login_desde_csv(driver, usuario, clave, debe_funcionar, descripcion):
    login = LoginPage(driver)
    login.abrir()
    login.iniciar_sesion(usuario, clave)
    if debe_funcionar:
        assert "inventory" in driver.current_url, descripcion
    else:
        assert "inventory" not in driver.current_url, descripcion

@pytest.mark.smoke
def test_login_usuario_valido_smoke(driver):
    login = LoginPage(driver)
    login.abrir()
    login.iniciar_sesion("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url
