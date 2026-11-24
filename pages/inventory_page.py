class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")
        self.cart_button = page.locator(".shopping_cart_link")

    def get_title(self):
        return self.title.inner_text()

    def get_items_count(self):
        return self.inventory_items.count()

    def add_first_item_to_cart(self):
        self.page.locator(".inventory_item button").first.click()

    def open_cart(self):
        self.cart_button.click()
