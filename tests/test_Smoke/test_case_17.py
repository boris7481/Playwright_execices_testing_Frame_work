# Test Case 17: Remove Products From Cart
from playwright.sync_api import Page, expect, Playwright

import time
from faker import Faker

faker = Faker()
email = faker.email()


# ---#termes = ID ,   .terms = class      09w0823@Freedom
# Test Case 6: Contact Us Form
def test_Remove_Products_From_Cart(page: Page):
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
    page.get_by_role("link", name="Cart").click()
    item = page.locator("table tbody tr", has_text="Blue Top")

    # Sauvegarder son texte
    item_text = item.inner_text()

    # Cliquer sur la croix
    item.locator(".cart_quantity_delete").click()

    # Vérifier disparition
    page.wait_for_selector(f"text={item_text}", state="detached")  # verification here


# ---#termes = ID ,   .terms = class      09w0823@Freedom
# firefox
def test_Remove_Products_From_Cart_firefox(playwright: Playwright):
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
    page.get_by_role("link", name="Cart").click()
    item = page.locator("table tbody tr", has_text="Blue Top")

    # Sauvegarder son texte
    item_text = item.inner_text()

    # Cliquer sur la croix
    item.locator(".cart_quantity_delete").click()

    # Vérifier disparition
    page.wait_for_selector(f"text={item_text}", state="detached")  # verification here
