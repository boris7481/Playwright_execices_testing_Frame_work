import pytest
from playwright.sync_api import Page, expect, Playwright
from pathlib import Path

file_path = Path(r"C:\Users\boris\OneDrive\Desktop\Testing_document.txt")


def test_Contact_Us_Form(go_to_page_login, credentials_valid):
    page = go_to_page_login
    page.locator('[data-qa="login-email"]').fill(credentials_valid["email"])
    page.locator('[data-qa="login-password"]').fill(credentials_valid["password"])
    page.locator('[data-qa="login-button"]').click()
    page.get_by_role("link", name=" Contact us").click()
    expect(page.get_by_text("GET IN TOUCH")).to_be_visible()
    page.get_by_placeholder("name").fill("freedom")
    page.locator('[data-qa="email"]').fill("test@test.com")
    page.get_by_placeholder("Subject").fill("Feedback")
    page.get_by_placeholder("Your Message Here").fill("I wnat to let you kkow that you are amazing")
    page.set_input_files('[name="upload_file"]', file_path)
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("link", name=" Home").click()
    expect(page.get_by_text("Features Items")).to_be_visible()



def test_Contact_Us_Form_firefox(test_login_User_firefox_login, credentials_valid):
    page = test_login_User_firefox_login
    page.locator('[data-qa="login-email"]').fill(credentials_valid["email"])
    page.locator('[data-qa="login-password"]').fill(credentials_valid["password"])
    page.locator('[data-qa="login-button"]').click()
    page.get_by_role("link", name=" Contact us").click()
    expect(page.get_by_text("GET IN TOUCH")).to_be_visible()
    page.get_by_placeholder("name").fill("freedom")
    page.locator('[data-qa="email"]').fill("test@test.com")
    page.get_by_placeholder("Subject").fill("Feedback")
    page.get_by_placeholder("Your Message Here").fill("I wnat to let you kkow that you are amazing")
    page.set_input_files('[name="upload_file"]', file_path)
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("link", name=" Home").click()
    expect(page.get_by_text("Features Items")).to_be_visible()
