from playwright.sync_api import expect


class LoginPage:

    def __init__(self, page):
        self.page = page

    #     def navigate(self):
    #     self.page.goto("https://www.automationexercise.com/")

    def login(self, user_name, password):
        self.page.locator('[data-qa="login-email"]').fill(user_name)
        self.page.locator('[data-qa="login-password"]').fill(password)
        self.page.locator('[data-qa="login-button"]').click()
    #    expect(self.page.get_by_text("Login to your account")).to_be_visible()
    #    expect(self.page.get_by_text("Your email or password is incorrect!")).to_be_visible()

    def signup(self, user_name, email):
        self.page.locator('[data-qa="signup-name"]').fill(user_name)
        self.page.locator('[data-qa="signup-email"]').fill(email)
        self.page.locator('[data-qa="signup-button"]').click()


