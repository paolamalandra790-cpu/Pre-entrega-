from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.user_input = (By.ID, "user-name")
        self.pass_input = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")

    def abrir(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, user, password):
        self.wait.until(EC.visibility_of_element_located(self.user_input)).send_keys(user)
        self.driver.find_element(*self.pass_input).send_keys(password)
        self.driver.find_element(*self.login_btn).click()