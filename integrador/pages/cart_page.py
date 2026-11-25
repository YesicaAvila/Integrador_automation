from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTON_REL = (By.TAG_NAME, "button")
    CHECKOUT_BUTTON = (By. ID, "checkout")

    def get_item_names(self):
        self.find_visible(self.CART_ITEM_NAMES)
        elements = self.driver.find_elements(*self.CART_ITEM_NAMES)
        return [element.text for element in elements]

    def remove_item_by_id(self, remove_button_id):
        # Hace clic en el botón "Remove" de un producto específico por su ID (ej. "remove-sauce-labs-fleece-jacket")
        self.click((By.ID, remove_button_id))
        return self

    def remove_first_item(self):
        first_item = self.find_visible(self.CART_ITEMS)
        first_item.find_element(*self.REMOVE_BUTTON_REL).click()
        return self

    def get_items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)