# Test Case 13: Verify Product quantity in Cart

from playwright.sync_api import Page, expect, Playwright

import time


# ---#termes = ID ,   .terms = class
# Test Case 6: Contact Us Form
def test_Verify_Product_quantity_in_Cart(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    page.get_by_role("link", name=" Products").click()
    page.get_by_role("link", name="View Product").first.click()
    expect(page.get_by_text("Blue Top")).to_be_visible()
    expect(page.get_by_text("Category: Women > Tops")).to_be_visible()
    expect(page.get_by_text("Rs. 500")).to_be_visible()
    page.locator("#quantity").fill("4")
    page.get_by_role("button", name="Add to cart").click()
    page.get_by_role("link", name="View Cart").click()
    expect(page.locator(".cart_quantity", has_text="4"))
    time.sleep(4)


#   blue_top = page.locator(".product-image-wrapper").filter(has_text="Blue Top").first
#   blue_top.hover()
#   blue_top.locator(".add-to-cart").first.click()

def test_Verify_Product_quantity_in_Cart_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    page.get_by_role("link", name=" Products").click()
    page.get_by_role("link", name="View Product").first.click()
    expect(page.get_by_text("Blue Top")).to_be_visible()
    expect(page.get_by_text("Category: Women > Tops")).to_be_visible()
    expect(page.get_by_text("Rs. 500")).to_be_visible()
    page.locator("#quantity").fill("4")
    page.get_by_role("button", name="Add to cart").click()
    page.get_by_role("link", name="View Cart").click()
    expect(page.locator(".cart_quantity", has_text="4"))
    time.sleep(4)
    firefoxBrowser.close()
