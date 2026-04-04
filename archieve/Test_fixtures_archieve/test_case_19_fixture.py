# Test Case 19: View & Cart Brand Products
from playwright.sync_api import Page, expect, Playwright


# I need to chech this test again
def test_View_and_Cart_Brand_Products(verify_all_product_fixture):
    page = verify_all_product_fixture
    expect(page.get_by_text("Brands")).to_be_visible()
    page.get_by_role("link", name=" Products").click()
    page.get_by_role("link", name="Polo").click()
    expect(page.get_by_text("Brand - Polo Products")).to_be_visible()
    page.get_by_role("link", name="H&M").click()
    expect(page.get_by_text("Brand - H&M Products")).to_be_visible()


# firefox
def test_View_and_Cart_Brand_Products_firefox(test_login_User_firefox_consent):
    page = test_login_User_firefox_consent
    expect(page.get_by_text("Brands")).to_be_visible()
    page.get_by_role("link", name=" Products").click()
    page.get_by_role("link", name="Polo").click()
    expect(page.get_by_text("Brand - Polo Products")).to_be_visible()
    page.get_by_role("link", name="H&M").click()
    expect(page.get_by_text("Brand - H&M Products")).to_be_visible()
