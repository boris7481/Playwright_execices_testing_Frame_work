# Test Case 20: Search Products and Verify Cart After Login
import time

from playwright.sync_api import expect


# ---#termes = ID ,   .terms = class      09w0823@Freedom
def test_Search_Products_and_Verify_Cart_After_Login(go_to_page_einwilligen):
    page = go_to_page_einwilligen
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


# firefox
def test_Search_Products_and_Verify_Cart_After_Login_firefox(test_login_User_firefox_consent):
    page = test_login_User_firefox_consent
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
