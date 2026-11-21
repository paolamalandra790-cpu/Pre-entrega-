import pytest

@pytest.fixture
def driver():
    from selenium import webdriver
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()

def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.outcome == "failed":
        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot("foto_cuando_fallo.png")
            print("Se guardó la foto porque falló")
