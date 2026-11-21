import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

logger = logging.getLogger(__name__)

def before_all(context):
    logger.info("Configurando WebDriver una vez")
    options = Options()
    # options.add_argument("--headless") # si querés sin ventana
    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

def after_step(context, step):
    if step.status == "failed":
        os.makedirs("reports/screens", exist_ok=True)
        name = f"reports/screens/{context.scenario.name}_{step.name}.png"
        name = name.replace(" ", "_").replace("/", "_")
        context.driver.save_screenshot(name)
        logger.info(f"Screenshot guardado en: {name}")

def after_all(context):
    logger.info("Cerrando WebDriver y limpiando recursos")
    context.driver.quit()
