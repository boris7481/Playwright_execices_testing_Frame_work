from playwright.sync_api import expect


class HomePage:
    def __init__(self, page):
        self.page = page

    def navigate_without_login(self):
        self.page.goto("https://www.automationexercise.com/")
        self.page.get_by_role("button", name="Einwilligen").click()
        expect(self.page.get_by_text("Video Tutorials")).to_be_visible()

    def selectordernavigationlink(self):
        #  self.page.get_by_role("button", name="Einwilligen").click()
        self.page.get_by_role("link", name="Signup / Login").click()
        expect(self.page.get_by_text("Login to your account")).to_be_visible()

    def selectordernavigationlink_signup(self):
        self.page.get_by_role("link", name="Signup / Login").click()
        expect(self.page.get_by_text("New User Signup!")).to_be_visible()

    #  expect(self.page.get_by_text("Video Tutorials")).to_be_visible()

    def view_women_items(self):
        self.page.get_by_role("link", name="Women").click()
        self.page.get_by_role("link", name="Dress").click()

    def view_men_items(self):
        self.page.get_by_role("link", name="Men").click()
        self.page.get_by_role("link", name="Tshirts").click()

    def navigate_and_click_of_product_link(self):
        self.page.get_by_role("link", name=" Products").click()

    def navigate_and_click_of_cart_link(self):
        self.page.get_by_role("link", name="Cart").click()

    def navigate_and_click_of_view_home_first_product_link(self):
        self.page.get_by_role("link", name="View Product").first.click()

    def test_Add_to_cart_from_Recommended_items_method(self):
        expect(self.page.get_by_text("recommended items")).to_be_visible()
        add_btn = self.page.locator('[data-product-id="4"]:visible').first  # --> More precise
        add_btn.click()
        self.page.get_by_text("View Cart").click()
        expect(self.page.get_by_text("Stylish Dress")).to_be_visible()

    def logout_user_from_home_page(self):
        expect( self.page.get_by_text("Logged in as 09w0823@Freedom")).to_be_visible()
        self.page.get_by_role("link", name="logout").click()
        expect( self.page.get_by_text("Login to your account")).to_be_visible()

    def Verify_soucription_in_home_page_method(self):
        expect(self.page.get_by_text("Subscription")).to_be_visible()
        self.page.get_by_placeholder("Your email address").fill("freedomvision@gmail.com")
        self.page.locator("#subscribe").click()
        expect(self.page.get_by_text("You have been successfully subscribed")).to_be_visible()

    def scroll_up_and_down(self):
        self.page.mouse.wheel(0, 3000)
        expect(self.page.get_by_text("Subscription")).to_be_visible()
        btn = self.page.locator("#scrollUp")
        btn.wait_for(state="visible")

        btn.click()

        self.page.wait_for_function("window.scrollY === 0")

        expect(self.page.get_by_role("heading",
                                name="Full-Fledged practice website for Automation Engineers").first).to_be_visible()

    def scroll_up_and_down_and_wait_arrow(self):
        # 1️ Scroll vers le bas
        self.page.mouse.wheel(0, 5000)
     #   time.sleep(2)
        # 2️ Vérifier texte en bas
        expect(self.page.get_by_text("Subscription").first).to_be_visible()
     #   time.sleep(2)  # --> to see well
        # 3️ Scroll vers le haut (sans cliquer)
        self.page.evaluate("window.scrollTo(0, 0)")
     #   time.sleep(2)  # --> to see well
        # Attendre que le scroll soit terminé
        self.page.wait_for_function("window.scrollY === 0")

        # 4️ Vérifier texte en haut
        expect(self.page.get_by_role("heading",
                                name="Full-Fledged practice website for Automation Engineers").first).to_be_visible()



