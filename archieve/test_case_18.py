# Test Case 18: View Category Products
from playwright.sync_api import Page, expect, Playwright
import time


# ---#termes = ID ,   .terms = class      09w0823@Freedom
# Test Case 6: Contact Us Form
def test_View_Category_Products(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    expect(page.get_by_text("Category")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    page.get_by_role("link", name="Women").click()
    page.get_by_role("link", name="Dress").click()
    expect(page.get_by_text("Women - Dress Products")).to_be_visible()

    #    page.locator("#Men").filter(has_text="MEN")
    #    page.get_by_text("Men").click()
    page.get_by_role("link", name="Men").click()
    page.get_by_role("link", name="Tshirts").click()
    expect(page.get_by_text("Men - Tshirts Products")).to_be_visible()
