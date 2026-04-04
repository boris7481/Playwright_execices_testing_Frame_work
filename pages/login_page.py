from playwright.sync_api import expect


class LoginPage:

    def __init__(self, page):
        self.page = page

    #     def navigate(self):
    #     self.page.goto("https://www.automationexercise.com/")

    def login(self, username, password):
        self.page.locator('[data-qa="login-email"]').fill(username)
        self.page.locator('[data-qa="login-password"]').fill(password)
        self.page.locator('[data-qa="login-button"]').click()
    #    expect(self.page.get_by_text("Login to your account")).to_be_visible()
    #    expect(self.page.get_by_text("Your email or password is incorrect!")).to_be_visible()


