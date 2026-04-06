from playwright.sync_api import  expect


# Test Case 5: Register User with existing email
# ---#termes = ID ,   .terms = class

def test_Register_User_with_existing_emai(go_to_page_login, credentials_name_email):
    page = go_to_page_login
    expect(page.get_by_text("New User Signup!")).to_be_visible()
    page.locator('[data-qa="signup-name"]').fill(credentials_name_email["name"])
    page.locator('[data-qa="signup-email"]').fill(credentials_name_email["email"])
    page.locator('[data-qa="signup-button"]').click()
    expect(page.get_by_text("Email Address already exist")).to_be_visible()


# firefox
def test_Register_User_with_existing_emai_firefox(test_login_User_firefox_consent, credentials_name_email):
    page = test_login_User_firefox_consent
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("New User Signup!")).to_be_visible()
    page.locator('[data-qa="signup-name"]').fill(credentials_name_email["name"])
    page.locator('[data-qa="signup-email"]').fill(credentials_name_email["email"])
    page.locator('[data-qa="signup-button"]').click()
    expect(page.get_by_text("Email Address already exist")).to_be_visible()
