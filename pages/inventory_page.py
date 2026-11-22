from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self, product_name):
        product_name = product_name.lower().replace(" ", "-")
        button = (By.ID, f"add-to-cart-{product_name}")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button)
        ).click()

    def get_cart_count(self):
        try:
            badge = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.cart_badge)
            )
            return int(badge.text)
        except:
            return 0
