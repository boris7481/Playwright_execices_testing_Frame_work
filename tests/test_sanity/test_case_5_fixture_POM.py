from playwright.sync_api import Page, expect, Playwright

import time

from pages.home_page import HomePage
from pages.login_page import LoginPage


# Test Case 5: Register User with existing email

# ---#termes = ID ,   .terms = class

def test_Register_User_with_existing_emai(page: Page, credentials_name_email):
    user_name = credentials_name_email["name"]
    email = credentials_name_email["email"]
    # home page
    homepage = HomePage(page)
    homepage.navigate_without_login()
    homepage.selectordernavigationlink_signup()

    siguPage = LoginPage(page)  # object for loginPage class
    siguPage.signup(user_name, email)
    expect(page.get_by_text("Email Address already exist")).to_be_visible()


# firefox
def test_Register_User_with_existing_emai_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("New User Signup!")).to_be_visible()
    page.locator('[data-qa="signup-name"]').fill("09w0823@Freedom")
    page.locator('[data-qa="signup-email"]').fill("freedomvision@gmail.com")
    page.locator('[data-qa="signup-button"]').click()
    expect(page.get_by_text("Email Address already exist")).to_be_visible()
    firefoxBrowser.close()
    time.sleep(2)
