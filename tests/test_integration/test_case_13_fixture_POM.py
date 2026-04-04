from playwright.sync_api import Page, expect, Playwright

import time

from pages.home_page import HomePage
from pages.products_page import ProductsPage


# ---#termes = ID ,   .terms = class
# Test Case 6: Contact Us Form
def test_Verify_Product_quantity_in_Cart(page: Page):
    homepage = HomePage(page)
    homepage.navigate_without_login()
    homepage.navigate_and_click_of_product_link()
    homepage.navigate_and_click_of_view_home_first_product_link()

    product_detail = ProductsPage(page)
    product_detail.Verify_product_detail_is_opened()

    product_detail.click_Add_to_cart_button()

    expect(page.locator(".cart_quantity", has_text="4"))


# Firefox
def test_Verify_Product_quantity_in_Cart_firefox(test_login_User_firefox_consent):
    page = test_login_User_firefox_consent
    page.get_by_role("link", name=" Products").click()
    page.get_by_role("link", name="View Product").first.click()
    expect(page.get_by_text("Blue Top")).to_be_visible()
    expect(page.get_by_text("Category: Women > Tops")).to_be_visible()
    expect(page.get_by_text("Rs. 500")).to_be_visible()
    page.locator("#quantity").fill("4")
    page.get_by_role("button", name="Add to cart").click()
    page.get_by_role("link", name="View Cart").click()
    expect(page.locator(".cart_quantity", has_text="4"))
