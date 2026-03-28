from playwright.sync_api import Page, expect, Playwright

import time
from pathlib import Path


# Test Case 8: Verify All Products and product detail page
# ---#termes = ID ,   .terms = class
# Test Case 6: Contact Us Form
def test_Verify_All_Products_and_product_detail_page(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    page.get_by_role("link", name="products").click()
    expect (page.get_by_text("All Products")).to_be_visible()
    expect(page.get_by_text("Category")).to_be_visible()
    expect(page.get_by_text("Brands")).to_be_visible()
    page.get_by_role("link", name="View Product").first.click()
    expect(page.get_by_text("Blue Top")).to_be_visible()
    expect(page.get_by_text("Category: Women > Tops")).to_be_visible()
    expect(page.get_by_text("Rs. 500")).to_be_visible()
    expect(page.get_by_text("availability")).to_be_visible()
    expect(page.get_by_text("condition")).to_be_visible()
    expect(page.get_by_text("Brand:")).to_be_visible()
    time.sleep(4)


# Firefox
def test_Verify_All_Products_and_product_detail_page_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    page.get_by_role("link", name="products").click()
    expect (page.get_by_text("All Products")).to_be_visible()
    expect(page.get_by_text("Category")).to_be_visible()
    expect(page.get_by_text("Brands")).to_be_visible()
    page.get_by_role("link", name="View Product").first.click()
    expect(page.get_by_text("Blue Top")).to_be_visible()
    expect(page.get_by_text("Category: Women > Tops")).to_be_visible()
    expect(page.get_by_text("Rs. 500")).to_be_visible()
    expect(page.get_by_text("availability")).to_be_visible()
    expect(page.get_by_text("condition")).to_be_visible()
    expect(page.get_by_text("Brand:")).to_be_visible()
    time.sleep(4)
    firefoxBrowser.close()
