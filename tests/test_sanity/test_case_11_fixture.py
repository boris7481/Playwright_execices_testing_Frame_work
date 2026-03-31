from playwright.sync_api import Page, expect, Playwright

import time


# Test Case 11: Verify Subscription in Cart page
# ---#termes = ID ,   .terms = class
# Test Case 6: Contact Us Form
def test__Verify_Subscription_in_Cart_page(go_to_page_einwilligen):
    page = go_to_page_einwilligen
    page.get_by_role("link", name="Cart").click()
    expect(page.get_by_text("Subscription")).to_be_visible()
    page.get_by_placeholder("Your email address").fill("freedomvision@gmail.com")
    page.locator("#subscribe").click()
    expect(page.get_by_text("You have been successfully subscribed")).to_be_visible()


# Firefox

def test__Verify_Subscription_in_Cart_page_firefox(test_login_User_firefox_consent):
    page = test_login_User_firefox_consent
    page.get_by_role("link", name="Cart").click()
    expect(page.get_by_text("Subscription")).to_be_visible()
    page.get_by_placeholder("Your email address").fill("freedomvision@gmail.com")
    page.locator("#subscribe").click()
    expect(page.get_by_text("You have been successfully subscribed")).to_be_visible()

