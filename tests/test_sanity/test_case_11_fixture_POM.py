from playwright.sync_api import Page, expect, Playwright

import time

from pages.home_page import HomePage


# Test Case 11: Verify Subscription in Cart page
# ---#termes = ID ,   .terms = class
# Test Case 6: Contact Us Form
def test__Verify_Subscription_in_Cart_page(page: Page):
    homepage = HomePage(page)
    homepage.navigate_without_login()
    homepage.navigate_and_click_of_cart_link()
    homepage.Verify_soucription_in_home_page_method()




# Firefox

def test__Verify_Subscription_in_Cart_page_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    page.get_by_role("link", name="Cart").click()
    expect(page.get_by_text("Subscription")).to_be_visible()
    page.get_by_placeholder("Your email address").fill("freedomvision@gmail.com")
    page.locator("#subscribe").click()
    expect(page.get_by_text("You have been successfully subscribed")).to_be_visible()
    time.sleep(4)
    firefoxBrowser.close()
