# Test Case 22: Add to cart from Recommended items
from playwright.sync_api import Page, expect, Playwright

from pages.home_page import HomePage


# ---#termes = ID ,   .terms = class      09w0823@Freedom
def test_Add_to_cart_from_Recommended_items(page: Page):

    homepage = HomePage(page)
    homepage.navigate_without_login()
    homepage.test_Add_to_cart_from_Recommended_items_method()

# Firefox
def test_Add_to_cart_from_Recommended_items_firefox(test_login_User_firefox_consent):
    page = test_login_User_firefox_consent
    expect(page.get_by_text("recommended items")).to_be_visible()
    add_btn = page.locator('[data-product-id="4"]:visible').first  # --> More precise
    add_btn.click()
    page.get_by_text("View Cart").click()
    expect(page.get_by_text("Stylish Dress")).to_be_visible()
