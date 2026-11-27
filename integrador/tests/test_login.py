
from pages.login_page import LoginPage
from pages.login_page import LoginPage
from utils.csv_reader import leer_datos_login
import pytest
from utils.logger import get_logger

# Registra el flujo y resultado de las pruebas de login
logger = get_logger(__name__)

def login(self, username, password):
    """Completa usuario y contraseña y envía el formulario de inicio de sesión."""
    self.enter_username(username)
    self.enter_password(password)
    self.click_login()

def test_login_success(driver):
    """Verifica que credenciales válidas permitan acceder al inventario de productos."""
    logger.info("Inicio de sesión exitosa")
    login_page = LoginPage(driver)
    login_page.open_login_page().login("standard_user", "secret_sauce")

    # Valida redirección al catálogo y presencia de elementos clave de la sesión
    assert "/inventory.html" in driver.current_url
    assert login_page.get_logo_text() == "Swag Labs"
    assert login_page.get_products_title() == "Products"
    # assert False, "Fallo forzado para probar captura"

def test_login_fallido(driver):
    """Valida que credenciales inválidas muestren el mensaje de error esperado."""
    logger.info("Inicio de sesión fallida")
    login_page = LoginPage(driver)
    login_page.open_login_page().login("usuario_invalido", "clave_incorrecta")

    assert "Epic sadface" in login_page.get_error_message()

# Datos cargados para cubrir casos positivos y negativos
DATOS_LOGIN = leer_datos_login()

@pytest.mark.parametrize(
    "username, password, expected_success, expected_message",
    DATOS_LOGIN,
)

def test_login_parametizado(driver, username, password, expected_success, expected_message):
    """Ejecuta escenarios de login parametrizados validando acceso o rechazo según el caso."""
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
            # Registra el detalle completo antes de relanzar para que Pytest marque el fallo
            logger.exception("Error durante la prueba de login para usuario='%s'", username)
            raise