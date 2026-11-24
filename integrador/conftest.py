from datetime import datetime
from pathlib import Path
import pytest
from selenium import webdriver

SCREENSHOTS_DIR = Path("screenshots")


# Inicializa el navegador antes de cada prueba
@pytest.fixture
def driver():
    web_driver = webdriver.Chrome()
    web_driver.maximize_window()
    yield web_driver
    #Cierra el navegador
    web_driver.quit()

# Obtiene el resultado de cada etapa de la prueba (setup, call, teardown)
@pytest.hookimpl(hookwrapper=True)
def pytest_runteste_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        web_driver = item.funcargs.get("driver")
        if web_driver:
            SCREENSHOTS_DIR.mkdir(exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            web_driver.save_screenshot(str(SCREENSHOTS_DIR / file_name))