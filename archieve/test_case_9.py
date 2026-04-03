from playwright.sync_api import Page, expect, Playwright

import time


# Test Case 9: Search Product
# ---#termes = ID ,   .terms = class
# Test Case 6: Contact Us Form
def test_Search_Product(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    page.get_by_role("link", name="products").click()
    expect(page.get_by_text("All Products")).to_be_visible()
    page.get_by_placeholder("Search Product").fill("short")
    page.locator("#submit_search").click()
    expect(page.get_by_text("SEARCHED PRODUCTS")).to_be_visible()
    time.sleep(4)


# firefox
def test_Search_Product_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    page.get_by_role("link", name="products").click()
    expect(page.get_by_text("All Products")).to_be_visible()
    page.get_by_placeholder("Search Product").fill("short")
    page.locator("#submit_search").click()
    expect(page.get_by_text("SEARCHED PRODUCTS")).to_be_visible()
    time.sleep(4)
    firefoxBrowser.close()
