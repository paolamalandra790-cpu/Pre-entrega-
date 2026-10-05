from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

driver.find_element(By.XPATH, "(//button[text()='Add to cart'])[1]").click()
time.sleep(1)

contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
assert contador == "1"
print(f"Contador carrito: {contador}")

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)

producto_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
print(f"Producto en carrito: {producto_en_carrito} - Test OK")

driver.quit()