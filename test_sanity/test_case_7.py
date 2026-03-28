from playwright.sync_api import Page, expect, Playwright

import time
from pathlib import Path


# Test Case 7: Verify Test Cases Page
# ---#termes = ID ,   .terms = class
# Test Case 6: Contact Us Form
def test_Verify_Test_Cases_Page(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    expect(page.get_by_text("Features Items")).to_be_visible()
    page.get_by_role("button", name="Test Cases").click()
    expect(page.get_by_text("Feedback for Us")).to_be_visible()
    time.sleep(4)


# firefox
def test_Verify_Test_Cases_Page_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    expect(page.get_by_text("Features Items")).to_be_visible()
    page.get_by_role("button", name="Test Cases").click()
    expect(page.get_by_text("Feedback for Us")).to_be_visible()
    time.sleep(4)
    firefoxBrowser.close()
