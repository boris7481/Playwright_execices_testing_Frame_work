from playwright.sync_api import expect


class CartPage:
    def __init__(self, page):
        self.page = page

    def check_the_product_in_cart(self):
        expect(self.page.get_by_text("Blue Top").first).to_be_visible()
        expect(self.page.get_by_text("Men Tshirt").first).to_be_visible()

    def go_to_art_page_Verify_that_those_products_are_visible_in_cart_after_login_aswell(self):
        self.page.get_by_role("link", name="Cart").click()
        expect(self.page.get_by_text("Premium Polo T-Shirts")).to_be_visible()