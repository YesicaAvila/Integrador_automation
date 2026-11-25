from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USER_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    LOGO = (By.CLASS_NAME, "app_logo")
    PRODUCTS_TITLE = (By.CSS_SELECTOR, "[data-test='title']")

    def open_login_page(self):
        self.open(self.URL)
        return self

    def enter_username(self, username):
        self.type_text(self.USER_INPUT, username)
        return self

    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_logo_text(self):
        return self.get_text(self.LOGO)

    def get_products_title(self):
        return self.get_text(self.PRODUCTS_TITLE)
