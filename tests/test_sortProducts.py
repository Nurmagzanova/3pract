from playwright.sync_api import sync_playwright
from pages.login_po import LoginPage
from pages.product_po import ProductsPage

def test_sort_products_low_to_high():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Запуск браузера
        context = browser.new_context()
        page = browser.new_page()
        
        login_page = LoginPage(page)
        products_page = ProductsPage(page)
        login_page.open()
        
        login_page.input_username('standard_user')
        login_page.input_password('secret_sauce')
        login_page.click_login()

        page.wait_for_selector('.inventory_list') 
        
        # Сортировка товаров по цене
        products_page.sort_of_products()
        
        # Проверка корректности сортировки
        prices = products_page.get_products_price()
        assert prices == sorted(prices), "Prices are not sorted correctly"

        context.clear_cookies()
        browser.close()