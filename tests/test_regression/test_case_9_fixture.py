from playwright.sync_api import Page, expect, Playwright


# Test Case 9: Search Product
# ---#termes = ID ,   .terms = class
# Test Case 6: Contact Us Form
def test_Search_Product(go_to_page_einwilligen):
    page = go_to_page_einwilligen
    page.get_by_role("link", name="products").click()
    expect(page.get_by_text("All Products")).to_be_visible()
    page.get_by_placeholder("Search Product").fill("short")
    page.locator("#submit_search").click()
    expect(page.get_by_text("SEARCHED PRODUCTS")).to_be_visible()


# firefox
def test_Search_Product_firefox(test_login_User_firefox_consent):
    page = test_login_User_firefox_consent
    page.get_by_role("link", name="products").click()
    expect(page.get_by_text("All Products")).to_be_visible()
    page.get_by_placeholder("Search Product").fill("short")
    page.locator("#submit_search").click()
    expect(page.get_by_text("SEARCHED PRODUCTS")).to_be_visible()
