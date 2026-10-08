from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.title = (By.CLASS_NAME, "title")
        self.list = (By.CLASS_NAME, "inventory_list")

    def get_title(self):
        return self.driver.find_element(*self.title).text

    def is_displayed(self):
        return self.driver.find_element(*self.list).is_displayed()