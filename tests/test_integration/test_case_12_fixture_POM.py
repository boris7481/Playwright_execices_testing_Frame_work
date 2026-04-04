# Test Case 12: Add Products in Cart
from playwright.sync_api import Page, expect, Playwright

import time

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage


# ---#termes = ID ,   .terms = class
# Test Case 6: Contact Us Form
def test_Add_Products_in_Cart(page: Page):
    homepage = HomePage(page)
    homepage.navigate_without_login()
    homepage.navigate_and_click_of_product_link()

    product_adding_to_cart = ProductsPage(page)
    product_adding_to_cart.test_Add_Products_in_Cart_method()

    homepage.navigate_and_click_of_cart_link()  # from home page click

    check_product_in_cart = CartPage(page)
    check_product_in_cart.check_the_product_in_cart()


# Firefox
def test_Add_Products_in_Cart_firefox(test_login_User_firefox_consent):
    page = test_login_User_firefox_consent
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
