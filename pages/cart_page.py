from selenium.webdriver.common.by import By

class CartPage:
    TITULO_CARRITO = (By.CLASS_NAME, "title")
    BOTON_CHECKOUT = (By.ID, "checkout")
    BOTON_SEGUIR_COMPRANDO = (By.ID, "continue-shopping")
    ITEMS_CARRITO = (By.CLASS_NAME, "cart_item")
    BOTON_ELIMINAR = (By.ID, "remove-sauce-labs-backpack")

    def __init__(self, driver):
        self.driver = driver

    def esta_en_carrito(self):
        return "cart" in self.driver.current_url

    def cantidad_items(self):
        return len(self.driver.find_elements(*self.ITEMS_CARRITO))

    def ir_a_checkout(self):
        self.driver.find_element(*self.BOTON_CHECKOUT).click()

    def eliminar_producto(self):
        self.driver.find_element(*self.BOTON_ELIMINAR).click()