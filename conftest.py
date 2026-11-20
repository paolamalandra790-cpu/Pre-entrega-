import pytest
from selenium import webdriver
import os
import logging
from datetime import datetime

# Carpeta de logs
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/test_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Screenshot cuando falla + log en el reporte
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            nombre = f"reports/screenshots/{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            driver.save_screenshot(nombre)
            logging.error(f"Test fallido: {item.name} - Screenshot: {nombre}")
