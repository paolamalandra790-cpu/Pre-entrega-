from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@given('inicio sesion con usuario "{user}" y contrasena "{password}"')
def step_login(context, user, password):
    login_page = LoginPage(context.driver)
    login_page.login(user, password)

@when('agrego el producto "{product_name}" al carrito')
def step_add_product(context, product_name):
    # Instancia la pagina del inventario
    inventory_page = InventoryPage(context.driver)
    inventory_page.add_product_to_cart(product_name)

@when('agrego los siguientes productos al carrito')
def step_add_multiple_products(context):
    inventory_page = InventoryPage(context.driver)
    for row in context.table:
        inventory_page.add_product_to_cart(row['producto'])
