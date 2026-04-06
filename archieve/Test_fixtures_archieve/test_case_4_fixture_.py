from playwright.sync_api import Page, expect, Playwright

import time


# Test Case 4: Logout User

# ---#termes = ID ,   .terms = class
# Test Case : LVerify logout user
def test_Logout_User(go_to_page_login, credentials_valid):
    page = go_to_page_login
    page.locator('[data-qa="login-email"]').fill(credentials_valid["email"])
    page.locator('[data-qa="login-password"]').fill(credentials_valid["password"])
    page.locator('[data-qa="login-button"]').click()
    expect(page.get_by_text("Logged in as 09w0823@Freedom")).to_be_visible()
    page.get_by_role("link", name="logout").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()


# firefox
def test_Logout_User_firefox(test_login_User_firefox_login, credentials_valid):
    page = test_login_User_firefox_login
    page.locator('[data-qa="login-email"]').fill(credentials_valid["email"])
    page.locator('[data-qa="login-password"]').fill(credentials_valid["password"])
    page.locator('[data-qa="login-button"]').click()
    expect(page.get_by_text("Logged in as 09w0823@Freedom")).to_be_visible()
    page.get_by_role("link", name="logout").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
