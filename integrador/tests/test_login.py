
from pages.login_page import LoginPage
from pages.login_page import LoginPage
from utils.csv_reader import leer_datos_login
import pytest
from utils.logger import get_logger

logger = get_logger(__name__)

def login(self, username, password):
    self.enter_username(username)
    self.enter_password(password)
    self.click_login()

def test_login_success(driver):
    logger.info("Inicio de sesión exitosa")
    login_page = LoginPage(driver)
    login_page.open_login_page().login("standard_user", "secret_sauce")

    assert "/inventory.html" in driver.current_url
    assert login_page.get_logo_text() == "Swag Labs"
    assert login_page.get_products_title() == "Products"

def test_login_fallido(driver):
    logger.info("Inicio de sesión fallida")
    login_page = LoginPage(driver)
    login_page.open_login_page().login("usuario_invalido", "clave_incorrecta")

    assert "Epic sadface" in login_page.get_error_message()

DATOS_LOGIN = leer_datos_login()

@pytest.mark.parametrize(
    "username, password, expected_success, expected_message",
    DATOS_LOGIN,
)

def test_login_parametizado(driver, username, password, expected_success, expected_message):
    logger.info(
        "Ejecutando login parametrizado | usuario='%s' | espera_exito=%s",
        username,
        expected_success,
    )
    try:
        login_page = LoginPage(driver)
        login_page.open_login_page().login(username, password)

        if expected_success:
            assert "/inventory.html" in driver.current_url
            assert login_page.get_logo_text() == "Swag Labs"
        else:
            assert "/inventory.html" not in driver.current_url
            assert expected_message in login_page.get_error_message()
            logger.info(
                "Login parametrizado rechazado como se esperaba para usuario='%s'",
                username,
            )
    except Exception:
            logger.exception("Error durante la prueba de login para usuario='%s'", username)
            raise