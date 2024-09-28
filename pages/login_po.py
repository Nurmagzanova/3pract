from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = 'input[name="user-name"]'  # Локатор для поля username
        self.password_input = 'input[name="password"]'   # Локатор для поля password
        self.login_button = 'input[type="submit"]'        # Локатор для кнопки Login
        self.error_message = 'h3[data-test="error"]'       # Локатор для сообщения об ошибке

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def input_username(self, username: str):
        self.page.fill(self.username_input, username)

    def input_password(self, password: str):
        self.page.fill(self.password_input, password)

    def click_login(self):
        self.page.click(self.login_button)

    def get_error_message(self) -> str:
        return self.page.locator(self.error_message).text_content()