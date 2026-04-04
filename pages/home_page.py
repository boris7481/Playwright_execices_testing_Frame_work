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
      #  expect(self.page.get_by_text("Video Tutorials")).to_be_visible()

    def view_women_items(self):
        self.page.get_by_role("link", name="Women").click()
        self.page.get_by_role("link", name="Dress").click()

    def view_men_items(self):
        self.page.get_by_role("link", name="Men").click()
        self.page.get_by_role("link", name="Tshirts").click()

    def navigate_and_click_of_product_link(self):
        self.page.get_by_role("link", name=" Products").click()


