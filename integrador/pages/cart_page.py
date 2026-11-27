from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    """Representa la vista del carrito de compras y permite gestionar sus productos"""

    #Localizadores de elementos dentro de la seccion carrito
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTON_REL = (By.TAG_NAME, "button")
    CHECKOUT_BUTTON = (By. ID, "checkout")

    def get_item_names(self):
        """Espera a que haya productos visbles y devuelve uan lista con sus textos"""
        self.find_visible(self.CART_ITEM_NAMES)
        elements = self.driver.find_elements(*self.CART_ITEM_NAMES)
        return [element.text for element in elements]

    def remove_item_by_id(self, remove_button_id):
        """ Hace clic en el botón "Remove" de un producto específico por su ID """
        self.click((By.ID, remove_button_id))
        return self

    def remove_first_item(self):
        """Elimina el primer producto del carrito y espera a que disminuya la cantidad total."""
        items_antes = self.get_items_count()
        first_item = self.find_visible(self.CART_ITEMS)
        first_item.find_element(*self.REMOVE_BUTTON_REL).click()
        self.wait.until(lambda d: self.get_items_count() < items_antes)
        return self

    def get_items_count(self):
        """Devuelve la cantidad actual de productos presentes en el carrito."""
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def click_checkout(self):
        """Hace clic en el botón Checkout para avanzar al formulario de compra."""
        self.click(self.CHECKOUT_BUTTON)