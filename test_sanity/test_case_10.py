from playwright.sync_api import Page, expect, Playwright

import time


# Test Case 10: Verify Subscription in home page
# ---#termes = ID ,   .terms = class
# Test Case 6: Contact Us Form
def test_Verify_Subscription_in_home_page(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    expect(page.get_by_text("Subscription")).to_be_visible()
    page.get_by_placeholder("Your email address").fill("freedomvision@gmail.com")
    page.locator("#subscribe").click()
    expect(page.get_by_text("You have been successfully subscribed")).to_be_visible()
    time.sleep(4)


# Firefox
def test_Verify_Subscription_in_home_page_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    expect(page.get_by_text("Subscription")).to_be_visible()
    page.get_by_placeholder("Your email address").fill("freedomvision@gmail.com")
    page.locator("#subscribe").click()
    expect(page.get_by_text("You have been successfully subscribed")).to_be_visible()
    time.sleep(4)
    firefoxBrowser.close()
