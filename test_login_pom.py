import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_login_exitoso(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url