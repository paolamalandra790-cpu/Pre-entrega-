from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        locator = (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[contains(@class, 'inventory_item')]//button")
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(1)

    def get_cart_count(self):
        for selector in [
            "[data-test='shopping-cart-badge']",
            ".shopping_cart_badge",
            ".shopping-cart-badge",
            ".shopping_cart_link",
        ]:
            try:
                el = self.driver.find_element(By.CSS_SELECTOR, selector)
                txt = el.text.strip()
                if txt.isdigit():
                    return int(txt)
            except:
                pass
        return 0

    def go_to_cart(self):
        cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_link.click()
