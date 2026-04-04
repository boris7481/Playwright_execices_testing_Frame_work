from playwright.sync_api import expect


class ProductsPage:
    def __init__(self, page):
        self.page = page
        
    def navigate_to_see_all_products_page(self):
        self.page.get_by_role("link", name="products").click()
        expect(self.page.get_by_text("All Products")).to_be_visible()
        expect(self.page.get_by_text("Category")).to_be_visible()
        expect(self.page.get_by_text("Brands")).to_be_visible()

    def navigate_to_see_all_products_page_and_the_first_item(self):
        self.page.get_by_role("link", name="View Product").first.click()
        expect(self.page.get_by_text("Blue Top")).to_be_visible()
        expect(self.page.get_by_text("Category: Women > Tops")).to_be_visible()
        expect(self.page.get_by_text("Rs. 500")).to_be_visible()
        expect(self.page.get_by_text("availability")).to_be_visible()
        expect(self.page.get_by_text("condition")).to_be_visible()
        expect(self.page.get_by_text("Brand:")).to_be_visible()


    def navigate_to_see_all_products_page_and_seach_product(self):
        self.page.get_by_role("link", name="products").click()
        expect(self.page.get_by_text("All Products")).to_be_visible()
        expect(self.page.get_by_text("All Products")).to_be_visible()
        self.page.get_by_placeholder("Search Product").fill("short")
        self.page.locator("#submit_search").click()
        expect(self.page.get_by_text("SEARCHED PRODUCTS")).to_be_visible()