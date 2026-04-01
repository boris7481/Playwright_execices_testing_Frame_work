# Test Case 1-2: Register User : this test case did not delete the user after his cretion

import time
from faker import Faker

faker = Faker()

from playwright.sync_api import  expect


def test_Cases_1_Register_User_whithout_deleting_the_user_after_creation(go_to_page_einwilligen):
    email = faker.email()
    page = go_to_page_einwilligen
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


# firefox

def test_Cases_1_Register_User_whithout_deleting_the_user_after_creation_firefox(test_login_User_firefox_consent):
    email = faker.email()
    page = test_login_User_firefox_consent
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
