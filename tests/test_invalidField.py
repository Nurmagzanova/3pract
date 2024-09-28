from playwright.sync_api import sync_playwright
from pages.login_po import LoginPage

def test_login_with_invalid_credentials():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Запуск браузера
        context = browser.new_context()
        page = context.new_page()
        
        login_page = LoginPage(page)
        login_page.open()  # Открываем страницу логина
        
        login_page.input_username('standard_user')  # Вводим некорректные данные
        login_page.input_password('wrong_password')
        login_page.click_login()
        
        error_message = login_page.get_error_message()
        assert error_message == "Epic sadface: Username and password do not match any user in this service", \
            f"Expected error message to be 'Epic sadface: Username and password do not match any user in this service', but got '{error_message}'"
        
        context.clear_cookies()  # Сброс состояния приложения
        browser.close()