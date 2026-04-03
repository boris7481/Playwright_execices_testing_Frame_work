from playwright.sync_api import Page, expect, Playwright
from pathlib import Path
from pages.contact_us_form_page import ContactUsPage
from pages.home_page import HomePage
from pages.login_page  import LoginPage

file_path = Path(r"C:\Users\boris\Desktop\test_document_contact_us_page.txt")


# Test Case 6: Contact Us Form


def test_Contact_Us_Form(page: Page, credentials_valid):

    user_name = credentials_valid["email"]
    password = credentials_valid["password"]

    # home page
    homepage = HomePage(page)
    homepage.navigate()
    homepage.selectordernavigationlink()

    # login page with valid credentials
    loginPage = LoginPage(page)  # object for loginPage class
    loginPage.login(user_name, password)

    # contact us page
    ContactUS = ContactUsPage(page)
    ContactUS.fill_infos()


#Firefox : I did not implemnt the POM here only the fixture is use
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