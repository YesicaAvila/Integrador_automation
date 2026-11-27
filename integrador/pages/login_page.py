from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

# módulo para registrar interacciones en la pantalla de login
logger = get_logger(__name__)


class LoginPage(BasePage):
    """Representa la página de inicio de sesión de SauceDemo y sus validaciones luego autenticar"""

    URL = "https://www.saucedemo.com/"

    # Localizadores del formulario de autenticación y mensajes de error
    USER_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    ## Localizadores visibles tras ingresar al catálogo para verificar la sesión
    LOGO = (By.CLASS_NAME, "app_logo")
    PRODUCTS_TITLE = (By.CSS_SELECTOR, "[data-test='title']")

    def open_login_page(self):
        """Abre la URL de inicio de sesión y retorna la instancia de la página."""
        self.open(self.URL)
        return self

    def enter_username(self, username):
        """Escribe el nombre de usuario en el campo correspondiente"""
        self.type_text(self.USER_INPUT, username)
        return self

    def enter_password(self, password):
        """Escribe la contraseña en el campo correspondiente"""
        self.type_text(self.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        """Hace clic en el botón de iniciar sesión."""
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        """Completa usuario y contraseña y envía el formulario de inicio de sesión."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """Recibe y devuelve el texto del mensaje de error mostrado en el login."""
        return self.get_text(self.ERROR_MESSAGE)

    def get_logo_text(self):
        """Recibe y devuelve el texto del logo principal de la aplicación."""
        return self.get_text(self.LOGO)

    def get_products_title(self):
        """Recibe y devuelve el título de la vista de productos tras iniciar sesión."""
        return self.get_text(self.PRODUCTS_TITLE)
