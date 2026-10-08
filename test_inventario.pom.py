from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_catalogo_visible(driver):
    LoginPage(driver).open()
    LoginPage(driver).login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    assert inventory.get_title() == "Products"
    assert inventory.is_displayed() == True