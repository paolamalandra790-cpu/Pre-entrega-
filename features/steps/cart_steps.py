from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('inicio sesion como "{user}" con la clave "{password}"')
def step_login(context, user, password):
    context.driver.delete_all_cookies()
    context.driver.get("https://www.saucedemo.com/")
    # Si quedó logueado del escenario anterior, salimos para poder entrar de nuevo
    try:
        context.driver.find_element(By.ID, "react-burger-menu-btn").click()
        WebDriverWait(context.driver, 3).until(
            EC.presence_of_element_located((By.ID, "logout_sidebar_link"))
        ).click()
    except:
        pass
    context.driver.find_element(By.ID, "user-name").send_keys(user)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

@when('agrego el producto "{product_name}" al carrito')
def step_agregar_producto(context, product_name):
    product_id = product_name.lower().replace(" ", "-")
    boton_id = f"add-to-cart-{product_id}"
    context.driver.find_element(By.ID, boton_id).click()

@then('el contador del carrito debe mostrar "{expected}"')
def step_verificar_contador(context, expected):
    badge = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert badge.text == expected, f"Esperaba {expected} pero el carrito muestra {badge.text}"
