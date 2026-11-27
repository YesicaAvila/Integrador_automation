from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    """Clase base para Page Objects tiene esperas y acciones de Selenium"""
    def __init__(self, driver, timeout=15):
        """Inicializa el WebDriver y la espera por defecto"""
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        """Abre la URL inidcada en el navegador y retorna el estado actual"""
        self.driver.get(url)
        return self

    def find_visible(self, locator):
        """Espera a que el elemento sea visible en el DOM y lo retorna"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        """Espera a que el elemento se vea, sea pueda clickear, y lo retorna"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def type_text(self, locator, text):
        """Limpia un campo visible y escribe el texto recibido."""
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)
        return self

    def click(self,locator):
        """Espera a que el elemento sea clickeable y ejecuta el clic."""
        self.find_clickable(locator).click()
        return self

    def get_text(self, locator):
        """Obtiene y devuelve el texto visible de un elemento."""
        return self.find_visible(locator).text