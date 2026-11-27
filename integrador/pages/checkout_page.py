from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_customer_info(self, first_name, last_name, postal_code):
        self.wait.until(EC.url_contains("checkout-step-one.html"))
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)
        return self

    def finish_order(self):
        #Confirma la compra
        self.wait.until(EC.url_contains("checkout-step-two.html"))
        boton_finish = self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON))
        boton_finish.click()
        self.wait.until(EC.url_contains("checkout-complete.html"))
        return self

    def get_complete_header(self):
        #Devuelve el mensaje
        return self.get_text(self.COMPLETE_HEADER)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)