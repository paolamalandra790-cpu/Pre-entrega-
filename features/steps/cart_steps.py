from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@given('inicio sesion como "{user}" con la clave "{password}"')
def step_login(context, user, password):
    login_page = LoginPage(context.driver)
    login_page.login(user, password)
    context.inventory_page = InventoryPage(context.driver)

@when('agrego el producto "{product}" al carrito')
def step_add_to_cart(context, product):
    context.inventory_page.add_product_to_cart(product)

@then('el contador del carrito debe mostrar "{count}"')
def step_cart_count(context, count):
    actual = context.inventory_page.get_cart_count()
    assert actual == int(count), f"Esperado: {count}, actual: {actual}"

@then('el producto "{product}" debe estar en el carrito')
def step_product_in_cart(context, product):
    assert context.inventory_page.is_product_in_cart(product)
