# Test Case 21: Add review on product
import time

from playwright.sync_api import Page, expect, Playwright


# ---#termes = ID ,   .terms = class      09w0823@Freedom
def test_Add_review_on_product(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    page.get_by_role("link", name=" Products").click()
    expect(page.get_by_text("All Products")).to_be_visible()
    page.get_by_role("link", name="View Product").first.click()
    expect(page.get_by_text("Write Your Review")).to_be_visible()
    page.get_by_placeholder("name").fill("Boris")
    page.get_by_role("textbox", name="Your email address")  # was propose by the error log and work
    page.get_by_placeholder("review").fill("Boris did a review")
    page.get_by_role("button", name="submit").click()
    print(page.get_by_text("Thank you").all_text_contents())
    print(page.get_by_text("Thank you for your review.").count())  # --> the only way to validat ethis


# Firefox
def test_Add_review_on_product_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    page.get_by_role("link", name=" Products").click()
    expect(page.get_by_text("All Products")).to_be_visible()
    page.get_by_role("link", name="View Product").first.click()
    expect(page.get_by_text("Write Your Review")).to_be_visible()
    page.get_by_placeholder("name").fill("Boris")
    page.get_by_role("textbox", name="Your email address")  # was propose by the error log and work
    page.get_by_placeholder("review").fill("Boris did a review")
    page.get_by_role("button", name="submit").click()
    print(page.get_by_text("Thank you").all_text_contents())
    print(page.get_by_text("Thank you for your review.").count())  # --> the only way to validat ethis
