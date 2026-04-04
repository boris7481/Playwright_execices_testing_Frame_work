from playwright.sync_api import Page, expect, Playwright
import time
# the part below has a smal issue

from pages.women_items_pages import Women
from pages.home_page import HomePage


# ---#termes = ID ,   .terms = class      09w0823@Freedom
# Test Case 6: Contact Us Form
def test_View_Category_Products(page: Page):
    homepage = HomePage(page)
    homepage.navigate_without_login()

    # Wemen
    women_items = HomePage(page)
    women_items.view_women_items()

    women_items_page = Women(page)
    women_items_page.access_women_itens()

    # # the part below has a smal issue
    men_items = HomePage(page)
    men_items.view_men_items()

    men_items_page = Women(page)
    men_items_page.view_men_items()

    #    page.locator("#Men").filter(has_text="MEN")
    #    page.get_by_text("Men").click()
