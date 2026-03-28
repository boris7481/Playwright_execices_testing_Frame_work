# Test Case 2: Login User with correct email and password
import time
from faker import Faker

faker = Faker()

from playwright.sync_api import Page, expect, Playwright


# ---#termes = ID ,   .terms = class
# this function allow you to recreate the account who was deleted by the foction below
def test_Cases_1_Register_User(page: Page):
    page.goto("https://www.automationexercise.com/signup")
    page.get_by_text("AutomationExercise").is_visible()
    page.get_by_role("button", name="Einwilligen").click()
    page.get_by_role("link", name="Signup / Login").click()
    page.get_by_text("New User Signup!").is_visible()
    page.locator('[data-qa="signup-name"]').fill("09w0823@Freedom")
    page.locator('[data-qa="signup-email"]').fill("freedomvision@gmail.com")
    page.locator('[data-qa="signup-button"]').click()
    page.get_by_text("'ENTER ACCOUNT INFORMATION'").is_visible()
    page.get_by_role("radio", name="Mr.").check()
    page.get_by_label("Password").fill("Freedom95")
    page.locator('[data-qa="days"]').select_option("20")
    page.locator('[data-qa="months"]').select_option("10")
    page.locator('[data-qa="years"]').select_option("2000")
    page.get_by_label("Sign up for our newsletter!").check()
    page.get_by_label("Receive special offers from our partners!").check()
    page.get_by_label("First name").fill("Freedom95")
    page.get_by_label("Last name").fill("Freedom")
    page.locator("[data-qa='company']").fill("Freedom und co")
    page.locator("[data-qa='address']").fill("Bicler str 10")
    page.locator("[data-qa='address2']").fill("Bicler str 100")
    page.locator("[data-qa='country']").select_option("Canada")
    page.locator("[data-qa='state']").fill("Monreal")
    page.locator("[data-qa='city']").fill("regensburg")
    page.locator("[data-qa='zipcode']").fill("93051")
    page.locator("[data-qa='mobile_number']").fill("23774814615")
    page.locator("[data-qa='create-account']").click()
    expect(page.get_by_text("ACCOUNT CREATED!")).to_be_visible()
    page.locator("[data-qa='continue-button']").click()
    expect(page.get_by_text("Logged in as 09w0823@Freedom")).to_be_visible()


def test_login_User_with_correct_email_and_password(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    page.locator('[data-qa="login-email"]').fill("freedomvision@gmail.com")
    page.locator('[data-qa="login-password"]').fill("Freedom95")
    page.locator('[data-qa="login-button"]').click()
    expect(page.get_by_text("Logged in as 09w0823@Freedom")).to_be_visible()
    page.get_by_role("link", name=" Delete Account").click()
    expect(page.get_by_text("ACCOUNT DELETED!")).to_be_visible()
    time.sleep(10)


# firefox
def test_login_User_with_correct_email_and_password_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    page.locator('[data-qa="login-email"]').fill("freedomvision@gmail.com")
    page.locator('[data-qa="login-password"]').fill("Freedom95")
    page.locator('[data-qa="login-button"]').click()
    expect(page.get_by_text("Logged in as 09w0823@Freedom")).to_be_visible()
    page.get_by_role("link", name=" Delete Account").click()
    expect(page.get_by_text("ACCOUNT DELETED!")).to_be_visible()
    firefoxBrowser.close()
    time.sleep(10)
