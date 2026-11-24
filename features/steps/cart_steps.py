from behave import given, when, then
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@given('inicio sesion con usuario "{user}" y contrasena "{password}"')
def step_login(context, user, password):
    login_page = LoginPage(context.driver)
    login_page.open()
    login_page.login(user, password)

@when('agrego "{product_name}" al carrito')
def step_add_product(context, product_name):
    products_page = ProductsPage(context.driver)
    products_page.add_product_to_cart(product_name)

@when('agrego los siguientes productos al carrito')
def step_add_multiple_products(context):
    products_page = ProductsPage(context.driver)
    for row in context.table:
        products_page.add_product_to_cart(row['producto'])

@then('el carrito debe contener {count:d} producto(s)')
def step_verify_cart_count(context, count):
    cart_page = CartPage(context.driver)
    actual_count = cart_page.get_cart_count()
    assert actual_count == count, f"Se esperaba {count} producto(s) en el carrito, pero se encontraron {actual_count}"
