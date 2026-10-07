from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Setup
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
wait = WebDriverWait(driver, 10)

# 2. Login - con las 3 estrategias que pide Matías en Clase 8
wait.unt(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "input#login-button").click()

# 3. Inventario
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))
driver.find_element(By.CSS_SELECTOR, "button.btn_primary").click()

# 4. Validación del carrito - sin sleep, solo espera explícita
badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

print(f"Carrito: {badge.text}")
assert badge.text == "1", "El carrito debería tener 1 producto"

print("Test Clase 8 - OK")

driver.quit()