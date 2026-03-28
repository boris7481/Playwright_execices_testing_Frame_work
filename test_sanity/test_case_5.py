from playwright.sync_api import Page, expect, Playwright

import time


# Test Case 5: Register User with existing email

# ---#termes = ID ,   .terms = class

def test_Register_User_with_existing_emai(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("New User Signup!")).to_be_visible()
    page.locator('[data-qa="signup-name"]').fill("09w0823@Freedom")
    page.locator('[data-qa="signup-email"]').fill("freedomvision@gmail.com")
    page.locator('[data-qa="signup-button"]').click()
    expect(page.get_by_text("Email Address already exist")).to_be_visible()
    expect(page.get_by_text("Success! Your details have been submitted successfully")).to_be_visible()
    page.get_by_role("link", name="Home").click()
    time.sleep(2)


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
