import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@given('estoy logueado con el usuario "{user}"')
def step_logged_in(context, user):
    login_page = LoginPage(context.driver)
    login_page.login(user, "secret_sauce")
    context.inventory_page = InventoryPage(context.driver)

@when('agrego el producto "{product}" al carrito')
def step_add_to_cart(context, product):
    context.inventory_page.add_product_to_cart(product)
    time.sleep(1)

@then('el contador del carrito deberia ser "{count}"')
def step_cart_count(context, count):
    actual = context.inventory_page.get_cart_count()
    assert actual == int(count), f"Esperado: {count}, Obtenido: {actual}"

@then('el carrito deberia tener "{count}" productos')
def step_cart_products(context, count):
    actual = context.inventory_page.get_cart_count()
    assert actual == int(count), f"Esperado: {count}
