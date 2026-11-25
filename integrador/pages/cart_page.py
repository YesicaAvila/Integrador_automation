from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By. ID, "checkout")

    def get_item_names(self):
        self.find_visible(self.CART_ITEM_NAMES)
        elements = self.driver.find_elements(*self.CART_ITEM_NAMES)
        return [element.text for element in elements]

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)