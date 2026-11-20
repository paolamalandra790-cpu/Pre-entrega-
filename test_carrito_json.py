import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from utils.datos import leer_json_productos

PRODUCTOS = leer_json_productos("datos/productos.json")

@pytest.fixture
def usuario_logueado(driver):
    login = LoginPage(driver)
    login.abrir()
    login.iniciar_sesion("standard_user", "secret_sauce")
    return driver

@pytest.mark.parametrize("producto", PRODUCTOS)
def test_agregar_producto_desde_json(usuario_logueado, producto):
    driver = usuario_logueado
    boton = driver.find_element(By.ID, producto["id_boton"])
    boton.click()
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert carrito.text == "1"

@pytest.mark.smoke
def test_carrito_smoke(usuario_logueado):
    driver = usuario_logueado
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"
