# TTest Case 16: Place Order: Login before Checkout
from playwright.sync_api import Page, expect, Playwright

import time
from faker import Faker

faker = Faker()
email = faker.email()


# ---#termes = ID ,   .terms = class      09w0823@Freedom
# Test Case 6: Contact Us Form
def test_Place_Order_login_before_Checkout(go_to_page_login, credentials_valid):
    page = go_to_page_login
    page.locator('[data-qa="login-email"]').fill(credentials_valid["email"])
    page.locator('[data-qa="login-password"]').fill(credentials_valid["password"])
    page.locator('[data-qa="login-button"]').click()
    expect(page.get_by_text("Logged in as 09w0823@Freedom")).to_be_visible()
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
    page.get_by_role("link", name="Cart").click()
    page.get_by_text("Proceed To Checkout").click()
    expect(page.get_by_text("Address Details")).to_be_visible()
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
    page.locator("[data-qa='continue-button']").click()


# firefox
def test_Place_Order_login_before_Checkout_firefox(go_to_page_login, credentials_valid):
    page = go_to_page_login
    page.locator('[data-qa="login-email"]').fill(credentials_valid["email"])
    page.locator('[data-qa="login-password"]').fill(credentials_valid["password"])
    page.locator('[data-qa="login-button"]').click()
    expect(page.get_by_text("Logged in as 09w0823@Freedom")).to_be_visible()
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
    page.get_by_role("link", name="Cart").click()
    page.get_by_text("Proceed To Checkout").click()
    expect(page.get_by_text("Address Details")).to_be_visible()
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
    page.locator("[data-qa='continue-button']").click()
