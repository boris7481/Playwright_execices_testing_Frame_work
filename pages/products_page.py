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

    def navigate_to_see_all_products_page_and_seach_product(self):
        self.page.get_by_role("link", name="products").click()
        expect(self.page.get_by_text("All Products")).to_be_visible()
        expect(self.page.get_by_text("All Products")).to_be_visible()
        self.page.get_by_placeholder("Search Product").fill("short")
        self.page.locator("#submit_search").click()
        expect(self.page.get_by_text("SEARCHED PRODUCTS")).to_be_visible()

    def navigate_to_see_all_products_page_and_see_brands_product(self):
        self.page.get_by_role("link", name="Polo").click()
        expect(self.page.get_by_text("Brand - Polo Products")).to_be_visible()
        self.page.get_by_role("link", name="H&M").click()
        expect(self.page.get_by_text("Brand - H&M Products")).to_be_visible()

    def add_review_on_product_method(self):
        expect(self.page.get_by_text("All Products")).to_be_visible()
        self.page.get_by_role("link", name="View Product").first.click()
        expect(self.page.get_by_text("Write Your Review")).to_be_visible()
        self.page.get_by_placeholder("name").fill("Boris")
        self.page.get_by_role("textbox", name="Your email address")  # was propose by the error log and work
        self.page.get_by_placeholder("review").fill("Boris did a review")
        self.page.get_by_role("button", name="submit").click()
        print(self.page.get_by_text("Thank you").all_text_contents())
        print(self.page.get_by_text("Thank you for your review.").count())

    def test_Add_Products_in_Cart_method(self):
        blue_top = self.page.locator(".product-image-wrapper").filter(has_text="Blue Top").first
        blue_top.hover()
        blue_top.locator(".add-to-cart").first.click()
        self.page.get_by_role("button", name="Continue Shopping").click()
        blue_top = self.page.locator(".product-image-wrapper").filter(has_text="Men Tshirt").first
        blue_top.hover()
        blue_top.locator(".add-to-cart").first.click()
        self.page.get_by_role("button", name="Continue Shopping").click()

    def Verify_product_detail_is_opened(self):
        expect(self.page.get_by_text("Blue Top")).to_be_visible()
        expect(self.page.get_by_text("Category: Women > Tops")).to_be_visible()
        expect(self.page.get_by_text("Rs. 500")).to_be_visible()
        self.page.locator("#quantity").fill("4")

    def click_Add_to_cart_button(self):
        self.page.get_by_role("button", name="Add to cart").click()

    def click_of_view_home_first_product_link(self):
        self.page.get_by_role("link", name="View Cart").click()


    def Verify_all_the_products_related_to_search_are_visible(self):
        expect(self.page.get_by_text("All Products")).to_be_visible()
        self.page.get_by_placeholder("Search Product").fill("Polo")
        self.page.locator("#submit_search").click()
        expect(self.page.get_by_text("Searched Products")).to_be_visible()


    def Add_those_products_to_cart(self):
        product = self.page.locator(".product-image-wrapper").filter(has_text="Premium Polo T-Shirts").first
        product.hover()
        product.locator(".add-to-cart").first.click()
        self.page.get_by_role("link", name="View cart").click()
        expect(self.page.get_by_text("Premium Polo T-Shirts")).to_be_visible()
        self.page.get_by_role("link", name="Signup / Login").click()
        expect(self.page.get_by_text("Login to your account")).to_be_visible()


