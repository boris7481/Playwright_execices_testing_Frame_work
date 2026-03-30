from playwright.sync_api import Page, expect, Playwright

import time
from pathlib import Path
file_path = Path(r"C:\Users\boris\OneDrive\Desktop\Testing_document.txt")


# ---#termes = ID ,   .terms = class
# Test Case 6: Contact Us Form
def test_Contact_Us_Form(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    page.get_by_role("link", name="Signup / Login").click()
#    page.get_by_role("link", name="Signup / Login").click()
    page.locator('[data-qa="login-email"]').fill("freedomvision@gmail.com")
    page.locator('[data-qa="login-password"]').fill("Freedom95")
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
    time.sleep(4)


# firefox
def test_Contact_Us_Form_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    page.get_by_role("link", name="Signup / Login").click()
    page.locator('[data-qa="login-email"]').fill("freedomvision@gmail.com")
    page.locator('[data-qa="login-password"]').fill("Freedom95")
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
    time.sleep(4)
    firefoxBrowser.close()
