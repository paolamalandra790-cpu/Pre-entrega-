from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que estoy en la página de login')
def step_pagina_login(context):
    context.driver.get("https://www.saucedemo.com/")
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )

@when('ingreso el usuario "{user}" y la contraseña "{password}"')
def step_ingreso_datos(context, user, password):
    campo_user = context.driver.find_element(By.ID, "user-name")
    campo_user.clear()
    campo_user.send_keys(user)
    campo_pass = context.driver.find_element(By.ID, "password")
    campo_pass.clear()
    campo_pass.send_keys(password)

@when('hago clic en el botón de login')
def step_clic_login(context):
    context.driver.find_element(By.ID, "login-button").click()

@then('debería ser redirigido al inventario')
def step_verificar_inventario(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

@then('debería ver el título "{titulo}"')
def step_verificar_titulo(context, titulo):
    titulo_elemento = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    )
    assert titulo_elemento.text == titulo, f"Esperaba {titulo} pero vi {titulo_elemento.text}"

@then('debería ver el mensaje de error "{mensaje}"')
def step_verificar_error(context, mensaje):
    error = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    assert mensaje in error.text, f"Esperaba {mensaje} pero vi {error.text}"
