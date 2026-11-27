from datetime import datetime
from pathlib import Path
import pytest
from selenium import webdriver
import base64
from selenium.webdriver.chrome.options import Options
import os

SCREENSHOTS_DIR = Path("screenshots")


# Inicializa el navegador antes de cada prueba
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-features=PasswordLeakDetection,SafeBrowsingPasswordCheck")
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    web_driver = webdriver.Chrome(options=options)
    if os.getenv("CI") != "true":
        web_driver.maximize_window()
    yield web_driver
    #Cierra el navegador
    web_driver.quit()

# Rcibe el resultado de cada etapa de la prueba (setup, call, teardown)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        web_driver = item.funcargs.get("driver")
        if web_driver:
            SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            archivo = SCREENSHOTS_DIR / file_name

            web_driver.save_screenshot(str(archivo))

            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html is not None:
                imagen_b64 = base64.b64encode(archivo.read_bytes()).decode("utf-8")
                extras = getattr(report, "extras", [])
                extras.append(pytest_html.extras.png(imagen_b64, name="Screenshot"))
                report.extras = extras