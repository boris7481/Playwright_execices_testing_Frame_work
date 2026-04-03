# Test Case 3: Login User with incorrect email and password
import time
from faker import Faker
from pages.login_page import LoginPage
from pages.home_page import HomePage

faker = Faker()

from playwright.sync_api import Page, expect, Playwright


def test_login_User_with_incorrect_email_and_password(page: Page, fake_credentials):
    user_name = fake_credentials["email"]
    password = fake_credentials["password"]

    homepage = HomePage(page)
    homepage.navigate()
    homepage.selectordernavigationlink()
    #   expect(page.get_by_text("Video Tutorials")).to_be_visible()

    loginPage = LoginPage(page)  # object for loginPage class
    #   loginPage.navigate(page)
    loginPage.login(user_name, password)

    #   expect(page.get_by_text("Video Tutorials")).to_be_visible()
    #   page.get_by_role("button", name="Einwilligen").click()
    #   page.get_by_role("link", name="Signup / Login").click()
    #   expect(page.get_by_text("Login to your account")).to_be_visible()
    #  expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()
    time.sleep(2)

# Firefox
