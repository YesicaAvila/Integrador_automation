from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(BasePage):
    """Representa el flujo de checkout (datos del comprador, resumen y confirmación de compra)."""

    #Localiza información del cliente y validación de errores
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    #Localiza la confirmacio final de la orden
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_customer_info(self, first_name, last_name, postal_code):
        """Completa los datos de envío en el primer paso del checkout y avanza al resumen."""

        #Asegura que los datos del cliente estén antes de interactuar con el formulario
        self.wait.until(EC.url_contains("checkout-step-one.html"))
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)
        return self

    def finish_order(self):
        """Confirma la compra en el resumen y espera hasta llegar a la pantalla final"""
        self.wait.until(EC.url_contains("checkout-step-two.html"))
        boton_finish = self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON))
        boton_finish.click()
        self.wait.until(EC.url_contains("checkout-complete.html"))
        return self

    def get_complete_header(self):
        """Devuelve el mensaje de confirmación al finalizar la compra"""
        return self.get_text(self.COMPLETE_HEADER)

    def get_error_message(self):
        """Recibe y devuelve el mensaje de error mostrado en el formulario de checkout."""
        return self.get_text(self.ERROR_MESSAGE)