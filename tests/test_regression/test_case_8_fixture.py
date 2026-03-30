from playwright.sync_api import expect


def test_Verify_All_Products_and_product_detail_page(verify_all_product_fixture):
    page = verify_all_product_fixture
    page.get_by_role("link", name="products").click()
    expect(page.get_by_text("All Products")).to_be_visible()
    expect(page.get_by_text("Category")).to_be_visible()
    expect(page.get_by_text("Brands")).to_be_visible()
    page.get_by_role("link", name="View Product").first.click()
    expect(page.get_by_text("Blue Top")).to_be_visible()
    expect(page.get_by_text("Category: Women > Tops")).to_be_visible()
    expect(page.get_by_text("Rs. 500")).to_be_visible()
    expect(page.get_by_text("availability")).to_be_visible()
    expect(page.get_by_text("condition")).to_be_visible()
    expect(page.get_by_text("Brand:")).to_be_visible()


def test_Verify_All_Products_and_product_detail_page_firefox(test_login_User_firefox_consent):
    page = test_login_User_firefox_consent
    page.get_by_role("link", name="products").click()
    expect(page.get_by_text("All Products")).to_be_visible()
    expect(page.get_by_text("Category")).to_be_visible()
    expect(page.get_by_text("Brands")).to_be_visible()
    page.get_by_role("link", name="View Product").first.click()
    expect(page.get_by_text("Blue Top")).to_be_visible()
    expect(page.get_by_text("Category: Women > Tops")).to_be_visible()
    expect(page.get_by_text("Rs. 500")).to_be_visible()
    expect(page.get_by_text("availability")).to_be_visible()
    expect(page.get_by_text("condition")).to_be_visible()
    expect(page.get_by_text("Brand:")).to_be_visible()
