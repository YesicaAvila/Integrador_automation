from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_checkout_completo(driver):
    """Valida el flujo completo de checkout desde el login hasta la confirmación de compra."""
    # 1. Inicia sesión y agrega un producto al carrito
    LoginPage(driver).open_login_page().login("standard_user", "secret_sauce")
    InventoryPage(driver).add_first_product()
    InventoryPage(driver).go_to_cart()

    # 2. Desde el carrito avanza hacia el checkout
    CartPage(driver).click_checkout()
    

    # 3. Completa los datos del comprador y finaliza la orden
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_customer_info("Ana", "Peñalosa", "1718").finish_order()

    # 4. Verifica que la compra se haya confirmado correctamente
    assert "checkout-complete.html" in driver.current_url
    assert checkout_page.get_complete_header() == "Thank you for your order!"

def test_checkout_datos_vacios(driver):
    """Verifica que enviar el formulario de checkout vacío muestre el error de nombre requerido."""
    #Prepara el carrito con unproducto y luego va a }l formulario de checkout
    LoginPage(driver).open_login_page().login("standard_user", "secret_sauce")
    InventoryPage(driver).add_first_product()
    InventoryPage(driver).go_to_cart()

    CartPage(driver).click_checkout()

    # Intenta continuar sin completar campos obligatorios
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_customer_info("", "", "")

    # Valida que la aplicación bloquee el avance e informe el campo faltante
    assert "First Name is required" in checkout_page.get_error_message()