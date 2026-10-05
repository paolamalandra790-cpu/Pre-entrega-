from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

titulo = driver.find_element(By.CLASS_NAME, "title").text
assert titulo == "Products"
print(f"Titulo verificado: {titulo}")

primer_producto = driver.find_element(By.CLASS_NAME, "inventory_item")
nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
print(f"Producto: {nombre} - {precio}")

driver.quit()