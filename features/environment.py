import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

logger = logging.getLogger(__name__)

def before_all(context):
    logger.info("Configurando WebDriver una vez")
    options = Options()
    options.binary_location = '/usr/bin/google-chrome'
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-data-dir=/tmp/chrome-profile")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-extensions")
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(10)

def after_step(context, step):
    if step.status == "failed":
        if hasattr(context, "driver"):
            os.makedirs("reports/screenshots", exist_ok=True)
            name = f"reports/screenshots/{context.scenario.name}_{step.name}.png"
            name = name.replace("/", "_").replace(" ", "_")
            context.driver.save_screenshot(name)
            logger.info(f"Screenshot guardado en: {name}")

def after_all(context):
    logger.info("Cerrando WebDriver y limpiando recursos")
    if hasattr(context, "driver"):
        context.driver.quit()
