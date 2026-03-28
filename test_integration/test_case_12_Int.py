# Test Case 12: Add Products in Cart
from playwright.sync_api import Page, expect, Playwright

import time


# ---#termes = ID ,   .terms = class
# Test Case 6: Contact Us Form
def test_Add_Products_in_Cart(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    page.get_by_role("link", name=" Products").click()
    blue_top = page.locator(".product-image-wrapper").filter(has_text="Blue Top").first
    blue_top.hover()
    blue_top.locator(".add-to-cart").first.click()
    page.get_by_role("button", name="Continue Shopping").click()
    blue_top = page.locator(".product-image-wrapper").filter(has_text="Men Tshirt").first
    blue_top.hover()
    blue_top.locator(".add-to-cart").first.click()
    page.get_by_role("button", name="Continue Shopping").click()
    page.get_by_role("link", name="Cart").click()
    expect(page.get_by_text("Blue Top")).to_be_visible()
    expect(page.get_by_text("Men Tshirt")).to_be_visible()
    time.sleep(2)


#   blue_top = page.locator(".product-image-wrapper").filter(has_text="Blue Top").first
#   blue_top.hover()
#   blue_top.locator(".add-to-cart").first.click()

# Firefox
def test_Add_Products_in_Cart_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    page.get_by_role("link", name=" Products").click()
    blue_top = page.locator(".product-image-wrapper").filter(has_text="Blue Top").first
    blue_top.hover()
    blue_top.locator(".add-to-cart").first.click()
    page.get_by_role("button", name="Continue Shopping").click()
    blue_top = page.locator(".product-image-wrapper").filter(has_text="Men Tshirt").first
    blue_top.hover()
    blue_top.locator(".add-to-cart").first.click()
    page.get_by_role("button", name="Continue Shopping").click()
    page.get_by_role("link", name="Cart").click()
    expect(page.get_by_text("Blue Top")).to_be_visible()
    expect(page.get_by_text("Men Tshirt")).to_be_visible()
    time.sleep(2)
