from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    PRODUCT_CARDS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME_REL = (By.CLASS_NAME, "inventory_item_name")
    ADD_BUTTON_REL = (By.TAG_NAME, "button")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def get_products_count(self):
        self.find_visible(self.PRODUCT_CARDS)
        return len(self.driver.find_elements(*self.PRODUCT_CARDS))

    def add_first_product(self):
        first_card = self.find_visible(self.PRODUCT_CARDS)
        product_name = first_card.find_element(*self.PRODUCT_NAME_REL).text
        first_card.find_element(*self.ADD_BUTTON_REL).click()
        return product_name

    def add_product_by_id(self, add_button_id):
        self.click((By.ID, add_button_id))
        return self

    def get_cart_badge_count(self):
        return self.get_text(self.CART_BADGE)

    def go_to_cart(self):
        self.click(self.CART_LINK)