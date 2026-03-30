# Test Case 22: Add to cart from Recommended items
from playwright.sync_api import Page, expect, Playwright


# ---#termes = ID ,   .terms = class      09w0823@Freedom
def test_Add_to_cart_from_Recommended_items(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    expect(page.get_by_text("recommended items")).to_be_visible()
    add_btn = page.locator('[data-product-id="4"]:visible').first  # --> More precise
    add_btn.click()
    page.get_by_text("View Cart").click()
    expect(page.get_by_text("Stylish Dress")).to_be_visible()


# Firefox

def test_Add_to_cart_from_Recommended_items_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    expect(page.get_by_text("recommended items")).to_be_visible()
    add_btn = page.locator('[data-product-id="4"]:visible').first  # --> More precise
    add_btn.click()
    page.get_by_text("View Cart").click()
    expect(page.get_by_text("Stylish Dress")).to_be_visible()
    firefoxBrowser.close()