# Test Case 21: Add review on product
import time

from playwright.sync_api import Page, expect, Playwright

from pages.home_page import HomePage
from pages.products_page import ProductsPage


# ---#termes = ID ,   .terms = class      09w0823@Freedom
def test_Add_review_on_product(page: Page):
    homepage = HomePage(page)
    homepage.navigate_without_login()
    homepage.navigate_and_click_of_product_link()

    product_review = ProductsPage(page)
    product_review.add_review_on_product_method()


# Firefox
def test_Add_review_on_product_firefox(test_login_User_firefox_login):
    page = test_login_User_firefox_login
    page.get_by_role("link", name=" Products").click()
    expect(page.get_by_text("All Products")).to_be_visible()
    page.get_by_role("link", name="View Product").first.click()
    expect(page.get_by_text("Write Your Review")).to_be_visible()
    page.get_by_placeholder("name").fill("Boris")
    page.get_by_role("textbox", name="Your email address")
    page.get_by_placeholder("review").fill("Boris did a review")
    page.get_by_role("button", name="submit").click()
    print(page.get_by_text("Thank you").all_text_contents())
    print(page.get_by_text("Thank you for your review.").count())
