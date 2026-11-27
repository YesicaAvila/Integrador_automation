from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    """Representa la vista de inventario/catálogo de productos y la navegación superior."""

    #Localiza productos y acciones del carrito
    PRODUCT_CARDS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME_REL = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE_REL = (By.CLASS_NAME, "inventory_item_price")
    ADD_BUTTON_REL = (By.TAG_NAME, "button")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    # controles de navegación y ordenamiento
    BURGER_MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def get_products_count(self):
        """Espera a que haya productos visibles y devuelve la cantidad total en el catálogo."""
        self.find_visible(self.PRODUCT_CARDS)
        return len(self.driver.find_elements(*self.PRODUCT_CARDS))

    def get_first_product_details(self):
        """Obtiene nombre y precio del primer producto visible en el inventario"""
        first_card = self.find_visible(self.PRODUCT_CARDS)
        name = first_card.find_element(*self.PRODUCT_NAME_REL).text
        price = first_card.find_element(*self.PRODUCT_PRICE_REL).text
        return name, price

    def add_first_product(self):
        """Agrega el primer producto al carrito y devuelve su nombre"""
        first_card = self.find_visible(self.PRODUCT_CARDS)
        product_name = first_card.find_element(*self.PRODUCT_NAME_REL).text
        first_card.find_element(*self.ADD_BUTTON_REL).click()
        return product_name

    def add_product_by_id(self, button_id):
        """Hace clic en el botón de agregar de un producto según su ID y retorna la página."""
        self.click((By.ID, button_id))
        return self

    def is_menu_visible(self):
        """Indica si el botón del menú lateral (hamburguesa) está visible."""
        return self.find_visible(self.BURGER_MENU_BUTTON).is_displayed()

    def is_filter_visible(self):
        """Verifica que el selector de ordenamiento/filtro esté visible"""
        return self.find_visible(self.SORT_DROPDOWN).is_displayed()

    def get_cart_badge_count(self):
        """Recibe y devuelve el contador numérico mostrado en el ícono del carrito."""
        return self.get_text(self.CART_BADGE)

    def go_to_cart(self):
        """Hace clic en el ícono del carrito para navegar a la vista del carrito."""
        self.click(self.CART_LINK)