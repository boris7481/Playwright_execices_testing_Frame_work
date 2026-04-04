# Test Case 19: View & Cart Brand Products
from playwright.sync_api import Page, expect, Playwright

from pages.home_page import HomePage
from pages.products_page import ProductsPage


# I need to chech this test again
def test_View_and_Cart_Brand_Products(page: Page):
    homepage = HomePage(page)
    homepage.navigate_without_login()
    homepage.navigate_and_click_of_product_link()

    expect(page.get_by_text("Brands")).to_be_visible()

    product_brands = ProductsPage(page)
    product_brands.navigate_to_see_all_products_page_and_see_brands_product()


# firefox
def test_View_and_Cart_Brand_Products_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    expect(page.get_by_text("Brands")).to_be_visible()
    page.get_by_role("link", name=" Products").click()
    page.get_by_role("link", name="Polo").click()
    expect(page.get_by_text("Brand - Polo Products")).to_be_visible()
    page.get_by_role("link", name="H&M").click()
    expect(page.get_by_text("Brand - H&M Products")).to_be_visible()
