from playwright.sync_api import Page, expect, Playwright

import time
from pathlib import Path

from pages.home_page import HomePage
from pages.test_case_page import TestCasePage


# Test Case 7: Verify Test Cases Page
# ---#termes = ID ,   .terms = class
# Test Case 6: Contact Us Form
def test_Verify_Test_Cases_Page(page: Page):
    homepage = HomePage(page)
    homepage.navigate_without_login()
    test_cases_validation = TestCasePage(page)
    test_cases_validation.test_Verify_Test_Cases_Page_methods()




# firefox
def test_Verify_Test_Cases_Page_firefox(test_login_User_firefox_consent):
    page = test_login_User_firefox_consent
    expect(page.get_by_text("Features Items")).to_be_visible()
    page.get_by_role("button", name="Test Cases").click()
    expect(page.get_by_text("Feedback for Us")).to_be_visible()

