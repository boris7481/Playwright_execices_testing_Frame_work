# Test Case 20: Search Products and Verify Cart After Login
import time

from playwright.sync_api import Page, expect, Playwright


# ---#termes = ID ,   .terms = class      09w0823@Freedom
def test_Search_Products_and_Verify_Cart_After_Login(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    page.get_by_role("link", name=" Products").click()
    expect(page.get_by_text("All Products")).to_be_visible()
    page.get_by_placeholder("Search Product").fill("Polo")
    page.locator("#submit_search").click()
    expect(page.get_by_text("Searched Products")).to_be_visible()
    product = page.locator(".product-image-wrapper").filter(has_text="Premium Polo T-Shirts").first
    product.hover()
    product.locator(".add-to-cart").first.click()
    page.get_by_role("link", name="View cart").click()
    expect(page.get_by_text("Premium Polo T-Shirts")).to_be_visible()
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    page.locator('[data-qa="login-email"]').fill("freedomvision@gmail.com")
    page.locator('[data-qa="login-password"]').fill("Freedom95")
    page.locator('[data-qa="login-button"]').click()
    page.get_by_role("link", name="Cart").click()
    expect(page.get_by_text("Premium Polo T-Shirts")).to_be_visible()
    time.sleep(2)


# firefox
def test_Search_Products_and_Verify_Cart_After_Login_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    page.get_by_role("link", name=" Products").click()
    expect(page.get_by_text("All Products")).to_be_visible()
    page.get_by_placeholder("Search Product").fill("Polo")
    page.locator("#submit_search").click()
    expect(page.get_by_text("Searched Products")).to_be_visible()
    product = page.locator(".product-image-wrapper").filter(has_text="Premium Polo T-Shirts").first
    product.hover()
    product.locator(".add-to-cart").first.click()
    page.get_by_role("link", name="View cart").click()
    expect(page.get_by_text("Premium Polo T-Shirts")).to_be_visible()
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    page.locator('[data-qa="login-email"]').fill("freedomvision@gmail.com")
    page.locator('[data-qa="login-password"]').fill("Freedom95")
    page.locator('[data-qa="login-button"]').click()
    page.get_by_role("link", name="Cart").click()
    expect(page.get_by_text("Premium Polo T-Shirts")).to_be_visible()
    time.sleep(2)
