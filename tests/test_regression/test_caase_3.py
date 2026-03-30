# Test Case 3: Login User with incorrect email and password
import time
from faker import Faker

faker = Faker()

from playwright.sync_api import Page, expect, Playwright


# ---#termes = ID ,   .terms = class
def test_login_User_with_incorrect_email_and_password(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    page.locator('[data-qa="login-email"]').fill("flase@gmail.com")
    page.locator('[data-qa="login-password"]').fill("Freedom95")
    page.locator('[data-qa="login-button"]').click()
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()
    time.sleep(4)


# Firefox
def test_login_User_with_incorrect_email_and_password_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    page.locator('[data-qa="login-email"]').fill("flase@gmail.com")
    page.locator('[data-qa="login-password"]').fill("Freedom95")
    page.locator('[data-qa="login-button"]').click()
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()
    time.sleep(4)
    firefoxBrowser.close()
