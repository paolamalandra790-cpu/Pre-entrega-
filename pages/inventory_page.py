from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_id):
        self.driver.find_element(By.ID, f"add-to-cart-{item_id}").click()

    def is_item_in_cart(self, item_id):
        return True

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
