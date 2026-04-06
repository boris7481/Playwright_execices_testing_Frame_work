# Test Case 20: Search Products and Verify Cart After Login
import time

from playwright.sync_api import Page, expect, Playwright

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage


# ---#termes = ID ,   .terms = class      09w0823@Freedom
def test_Search_Products_and_Verify_Cart_After_Login(page: Page, credentials_valid):

    user_name = credentials_valid["email"]
    password = credentials_valid["password"]

    homepage = HomePage(page)
    homepage.navigate_without_login()
    homepage.selectordernavigationlink()
    homepage.navigate_and_click_of_product_link()

    product_search_and_verify = ProductsPage(page)
    product_search_and_verify.Verify_all_the_products_related_to_search_are_visible()

    product_search_and_verify.Add_those_products_to_cart()
    page.locator('[data-qa="login-email"]').fill(user_name)
    page.locator('[data-qa="login-password"]').fill(password)
    page.locator('[data-qa="login-button"]').click()

    page.get_by_role("link", name="Cart").click()
    expect(page.get_by_text("Premium Polo T-Shirts")).to_be_visible()

    visible_in_cart_after_login_aswell = CartPage(page)
    visible_in_cart_after_login_aswell.go_to_art_page_Verify_that_those_products_are_visible_in_cart_after_login_aswell()


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
