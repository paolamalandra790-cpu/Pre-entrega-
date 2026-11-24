from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('inicio sesion como "{user}" con la clave "{password}"')
def step_login(context, user, password):
    context.driver.get("https://www.saucedemo.com/")
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    campo_user = context.driver.find_element(By.ID, "user-name")
    campo_user.clear()
    campo_user.send_keys(user)
    campo_pass = context.driver.find_element(By.ID, "password")
    campo_pass.clear()
    campo_pass.send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

@when('agrego el producto "{product_name}" al carrito')
def step_agregar_producto(context, product_name):
    product_id = product_name.lower().replace(" ", "-")
    boton_id = f"add-to-cart-{product_id}"
    boton = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, boton_id))
    )
    context.driver.execute_script("arguments[0].scrollIntoView(true);", boton)
    boton.click()

@then('el contador del carrito debe mostrar "{expected}"')
def step_verificar_contador(context, expected):
    WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), expected)
    )
    badge = context.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == expected, f"Esperaba {expected} pero el carrito muestra {badge.text}"
