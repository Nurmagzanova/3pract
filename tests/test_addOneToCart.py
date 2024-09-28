from playwright.sync_api import sync_playwright
from pages.login_po import LoginPage
from pages.product_po import ProductsPage

def test_add_single_item_to_cart():
    with sync_playwright() as p:
        # Запуск браузера
        browser = p.chromium.launch(headless=False)  
        context = browser.new_context()
        page = context.new_page()
        
        # Инициализация страниц
        login_page = LoginPage(page)
        products_page = ProductsPage(page)
        
        # Открытие страницы логина и вход в систему
        login_page.open()  
        login_page.input_username('standard_user')
        login_page.input_password('secret_sauce')
        login_page.click_login()
        
        # Ожидание загрузки страницы со списком продуктов
        page.wait_for_selector('.inventory_list')  
        
        # Добавление первого товара в корзину
        products_page.add_first_product_to_cart()
        
        # Проверка количества товаров в корзине
        cart_count = products_page.get_cart_count()
        assert cart_count == "1", f"Expected cart count to be '1', but got '{cart_count}'"
        
        # Сброс состояния приложения и закрытие браузера
        context.clear_cookies()  
        browser.close()