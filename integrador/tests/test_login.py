
from pages.login_page import LoginPage


def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page().login("standard_user", "secret_sauce")

    assert "/inventory.html" in driver.current_url
    assert login_page.get_logo_text() == "Swag Labs"
    assert login_page.get_products_title() == "Products"