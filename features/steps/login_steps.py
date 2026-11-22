from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import logging

logger = logging.getLogger(__name__)

@when('que estoy en la página de login')
def step_open_login(context):
    logger.info("Abriendo página de login")
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when('ingreso el usuario "{user}" y la contraseña "{password}"')
def step_enter_credentials(context, user, password):
    logger.info(f"Ingresando credenciales usuario={user}")
    context.login_page.enter_username(user)
    context.login_page.enter_password(password)

@when('hago clic en el botón de login')
def step_click_login(context):
    logger.info("Click en botón login")
    context.login_page.click_login()

@then('debería ser redirigido al inventario')
def step_verify_inventory(context):
    logger.info("Verificando redirección a inventario")
    context.inventory_page = InventoryPage(context.driver)
    assert context.inventory_page.is_loaded()

@then('debería ver el título "{title}"')
def step_verify_title(context, title):
    assert context.inventory_page.get_title() == title

@then('debería ver el mensaje de error "{mensaje}"')
def step_verify_error(context, mensaje):
    error = context.login_page.get_error_message()
    assert mensaje in error, f"Esperado: {mensaje}, Obtenido: {error}"

@given('que estoy logueado con el usuario "{user}"')
def step_logged_in(context, user):
    logger.info(f"Login automático con {user}")
    context.login_page = LoginPage(context.driver)
    context.login_page.open()
    context.login_page.login(user, "secret_sauce")
    context.inventory_page = InventoryPage(context.driver)
