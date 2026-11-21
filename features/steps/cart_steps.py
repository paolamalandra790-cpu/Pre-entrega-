from behave import when, then
import logging

logger = logging.getLogger(__name__)

@when('agrego el producto "{product}" al carrito')
def step_add_product(context, product):
    logger.info(f"Agregando producto: {product}")
    context.inventory_page.add_product_to_cart(product)

@then('el contador del carrito debería ser "{count}"')
def step_verify_cart_count(context, count):
    actual = context.inventory_page.get_cart_count()
    assert actual == count, f"Esperado: {count}, Obtenido: {actual}"
