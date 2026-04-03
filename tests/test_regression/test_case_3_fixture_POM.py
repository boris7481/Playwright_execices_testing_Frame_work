import time
from faker import Faker
from pages.login_page import LoginPage
from pages.home_page import HomePage

faker = Faker()

from playwright.sync_api import Page, expect, Playwright


def test_login_User_with_incorrect_email_and_password(page: Page, fake_credentials):
    user_name = fake_credentials["email_fake"]
    password = fake_credentials["password_fake"]

    # home page
    homepage = HomePage(page)
    homepage.navigate()
    homepage.selectordernavigationlink()

    # login page
    loginPage = LoginPage(page)  # object for loginPage class
    loginPage.login(user_name, password)
    expect(page.get_by_text("Login to your account")).to_be_visible()
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()  # final validation for this test


# Firefox test without POM only with fixture
def test_login_User_with_incorrect_email_and_password_firefox(test_login_User_firefox_login, fake_credentials):
    page = test_login_User_firefox_login
    page.locator('[data-qa="login-email"]').fill(fake_credentials["email_fake"])
    page.locator('[data-qa="login-password"]').fill(fake_credentials["password_fake"])
    page.locator('[data-qa="login-button"]').click()
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()
