from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        locator = (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[contains(@class, 'inventory_item')]//button")
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        btn.click()

    def get_cart_count(self):
        try:
            badge = self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")
            return int(badge.text)
        except:
            return 0

    def go_to_cart(self):
        cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_link.click()
