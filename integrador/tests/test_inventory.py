from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_inventory(driver):
    """Verifica el catálogo, los datos del primer producto y los controles visibles en inventario"""
    # Inicia sesión reutilizando LoginPage (y el driver viene desde conftest.py)
    LoginPage(driver).open_login_page().login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    #Validación general de la vista y existencia de productos
    assert driver.title == "Swag Labs"
    assert inventory_page.get_products_count() > 0

    #Validación del primer producto (nombre y precio)
    name_product, price_product = inventory_page.get_first_product_details()
    assert name_product == "Sauce Labs Backpack"
    assert price_product == "$29.99"

    #Validación de visibilidad del menú y del filtro
    assert inventory_page.is_menu_visible()
    assert inventory_page.is_filter_visible()