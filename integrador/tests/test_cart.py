from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_cart(driver):
    LoginPage(driver).open_login_page().login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)
    inventory_page.add_product_by_id("add-to-cart-sauce-labs-fleece-jacket")

    #Valida el contador del carrito y que el producto aparezca en el carrito
    assert inventory_page.get_cart_badge_count()=="1"
    inventory_page.go_to_cart()
    cart_page = CartPage(driver)
    assert "Sauce Labs Fleece Jacket" in cart_page.get_item_names()

def test_remove_prod_cart(driver):
    # Inicia sesión, agrega un producto y navega al carrito
    LoginPage(driver).open_login_page().login("standard_user", "secret_sauce")
    InventoryPage(driver).add_product_by_id("add-to-cart-sauce-labs-backpack")
    InventoryPage(driver).go_to_cart()

    # Elimina el producto usando el método de CartPage y verifica que quede vacío
    cart_page = CartPage(driver)
    assert cart_page.get_items_count() == 1
    #cart_page.remove_item_by_id("remove-sauce-labs-fleece-jacket")
    cart_page.remove_first_item()
    assert cart_page.get_items_count() == 0