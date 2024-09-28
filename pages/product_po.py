from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = '.inventory_item:first-of-type button'
        self.cart_badge = '.shopping_cart_badge'
        self.sort_of_products_selector = "[data-test='product-sort-container']"  
        self.product_prices_selector = '.inventory_item_price'  

    def add_first_product_to_cart(self):
        self.page.click(self.add_to_cart_button)

    def get_cart_count(self) -> str:
        return self.page.inner_text(self.cart_badge)

    def sort_of_products(self):
        self.page.select_option(self.sort_of_products_selector, "lohi")

    def get_products_price(self):
        prices_elements = self.page.eval_on_selector_all(self.product_prices_selector, "elements => elements.map(e => e.innerText)")
        prices = [float(price.replace("$", "")) for price in prices_elements]
        return prices
