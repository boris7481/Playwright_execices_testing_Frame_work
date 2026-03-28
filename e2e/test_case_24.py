# Test Case 24: Download Invoice after purchase order

from playwright.sync_api import Page, expect, Playwright
import os
import time
from faker import Faker

faker = Faker()
email = faker.email()


# ---#termes = ID ,   .terms = class      09w0823@Freedom
def test_Download_Invoice_after_purchase_order(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    page.get_by_role("link", name=" Products").click()
    blue_top = page.locator(".product-image-wrapper").filter(has_text="Blue Top").first
    blue_top.hover()
    blue_top.locator(".add-to-cart").first.click()
    page.get_by_role("button", name="Continue Shopping").click()
    blue_top = page.locator(".product-image-wrapper").filter(has_text="Men Tshirt").first
    blue_top.hover()
    blue_top.locator(".add-to-cart").first.click()
    page.get_by_role("button", name="Continue Shopping").click()
    page.get_by_role("link", name="Cart").click()
    expect(page.get_by_text("Blue Top")).to_be_visible()
    expect(page.get_by_text("Men Tshirt")).to_be_visible()
    #    page.get_by_role("link", name="Cart").click()
    page.get_by_text("Proceed To Checkout").click()
    #

    page.get_by_role("link", name="Register / Login").click()
    page.get_by_role("link", name="Signup / Login").click()
    page.get_by_text("New User Signup!").is_visible()
    page.locator('[data-qa="signup-name"]').fill("09w0823@Freedom")
    page.locator('[data-qa="signup-email"]').fill(email)
    page.locator('[data-qa="signup-button"]').click()
    page.get_by_text("'ENTER ACCOUNT INFORMATION'").is_visible()
    page.get_by_role("radio", name="Mr.").check()
    page.get_by_label("Password").fill("Freedom95")
    page.locator('[data-qa="days"]').select_option("20")
    page.locator('[data-qa="months"]').select_option("10")
    page.locator('[data-qa="years"]').select_option("2000")
    page.get_by_label("Sign up for our newsletter!").check()
    page.get_by_label("Receive special offers from our partners!").check()
    page.get_by_label("First name").fill("Freedom95")
    page.get_by_label("Last name").fill("Freedom")
    page.locator("[data-qa='company']").fill("Freedom und co")
    page.locator("[data-qa='address']").fill("Bicler str 10")
    page.locator("[data-qa='address2']").fill("Bicler str 100")
    page.locator("[data-qa='country']").select_option("Canada")
    page.locator("[data-qa='state']").fill("Monreal")
    page.locator("[data-qa='city']").fill("regensburg")
    page.locator("[data-qa='zipcode']").fill("93051")
    page.locator("[data-qa='mobile_number']").fill("23774814615")
    page.locator("[data-qa='create-account']").click()
    expect(page.get_by_text("ACCOUNT CREATED!")).to_be_visible()
    page.locator("[data-qa='continue-button']").click()
    expect(page.get_by_text("Logged in as 09w0823@Freedom")).to_be_visible()
    page.get_by_role("link", name="Cart").click()
    page.get_by_text("Proceed To Checkout").click()
    expect(page.get_by_text("Address Details")).to_be_visible()
    expect(page.locator(".address_delivery = .address_invoice"))

    expect(page.get_by_text("Review Your Order")).to_be_visible()
    page.locator(".form-control").fill("everything is op")
    page.get_by_role("link", name="Place Order").click()
    page.locator("[data-qa='name-on-card']").fill("Master Card")
    page.locator("[data-qa='card-number']").fill("10-2-30")
    page.locator("[data-qa='cvc']").fill("200")
    page.locator("[data-qa='expiry-month']").fill("10-02-30")
    page.locator("[data-qa='expiry-year']").fill("2030")
    page.locator("[data-qa='pay-button']").click()
    expect(page.get_by_text("Congratulations! Your order has been confirmed!")).to_be_visible()

    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download Invoice").click()

    download = download_info.value

    # Sauvegarde
    file_path = f"./downloads/{download.suggested_filename}"
    download.save_as(file_path)

    # Vérifications
    assert os.path.exists(file_path)
    assert os.path.getsize(file_path) > 0  # --> to check the size
    assert "invoice" in download.suggested_filename.lower()

    page.locator("[data-qa='continue-button']").click()


# firefox

def test_Download_Invoice_after_purchase_order_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    page.get_by_role("link", name=" Products").click()
    blue_top = page.locator(".product-image-wrapper").filter(has_text="Blue Top").first
    blue_top.hover()
    blue_top.locator(".add-to-cart").first.click()
    page.get_by_role("button", name="Continue Shopping").click()
    blue_top = page.locator(".product-image-wrapper").filter(has_text="Men Tshirt").first
    blue_top.hover()
    blue_top.locator(".add-to-cart").first.click()
    page.get_by_role("button", name="Continue Shopping").click()
    page.get_by_role("link", name="Cart").click()
    expect(page.get_by_text("Blue Top")).to_be_visible()
    expect(page.get_by_text("Men Tshirt")).to_be_visible()
    #    page.get_by_role("link", name="Cart").click()
    page.get_by_text("Proceed To Checkout").click()

    page.get_by_role("link", name="Register / Login").click()
    page.get_by_role("link", name="Signup / Login").click()
    page.get_by_text("New User Signup!").is_visible()
    page.locator('[data-qa="signup-name"]').fill("09w0823@Freedom")
    page.locator('[data-qa="signup-email"]').fill(email)
    page.locator('[data-qa="signup-button"]').click()
    page.get_by_text("'ENTER ACCOUNT INFORMATION'").is_visible()
    page.get_by_role("radio", name="Mr.").check()
    page.get_by_label("Password").fill("Freedom95")
    page.locator('[data-qa="days"]').select_option("20")
    page.locator('[data-qa="months"]').select_option("10")
    page.locator('[data-qa="years"]').select_option("2000")
    page.get_by_label("Sign up for our newsletter!").check()
    page.get_by_label("Receive special offers from our partners!").check()
    page.get_by_label("First name").fill("Freedom95")
    page.get_by_label("Last name").fill("Freedom")
    page.locator("[data-qa='company']").fill("Freedom und co")
    page.locator("[data-qa='address']").fill("Bicler str 10")
    page.locator("[data-qa='address2']").fill("Bicler str 100")
    page.locator("[data-qa='country']").select_option("Canada")
    page.locator("[data-qa='state']").fill("Monreal")
    page.locator("[data-qa='city']").fill("regensburg")
    page.locator("[data-qa='zipcode']").fill("93051")
    page.locator("[data-qa='mobile_number']").fill("23774814615")
    page.locator("[data-qa='create-account']").click()
    expect(page.get_by_text("ACCOUNT CREATED!")).to_be_visible()
    page.locator("[data-qa='continue-button']").click()
    expect(page.get_by_text("Logged in as 09w0823@Freedom")).to_be_visible()
    page.get_by_role("link", name="Cart").click()
    page.get_by_text("Proceed To Checkout").click()
    expect(page.get_by_text("Address Details")).to_be_visible()
    expect(page.locator(".address_delivery = .address_invoice"))

    expect(page.get_by_text("Review Your Order")).to_be_visible()
    page.locator(".form-control").fill("everything is op")
    page.get_by_role("link", name="Place Order").click()
    page.locator("[data-qa='name-on-card']").fill("Master Card")
    page.locator("[data-qa='card-number']").fill("10-2-30")
    page.locator("[data-qa='cvc']").fill("200")
    page.locator("[data-qa='expiry-month']").fill("10-02-30")
    page.locator("[data-qa='expiry-year']").fill("2030")
    page.locator("[data-qa='pay-button']").click()
    expect(page.get_by_text("Congratulations! Your order has been confirmed!")).to_be_visible()

    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download Invoice").click()

    download = download_info.value

    # Sauvegarde
    file_path = f"./downloads/{download.suggested_filename}"
    download.save_as(file_path)

    # Vérifications
    assert os.path.exists(file_path)
    assert os.path.getsize(file_path) > 0  # --> to check the size
    assert "invoice" in download.suggested_filename.lower()

    page.locator("[data-qa='continue-button']").click()
