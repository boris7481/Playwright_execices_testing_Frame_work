# Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality
from playwright.sync_api import Page, expect, Playwright
import time


# ---#termes = ID ,   .terms = class      09w0823@Freedom

def test_Verify_Scroll_Up_using_Arrow_button_and_Scroll_Down_functionality(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    #    expect(page.get_by_text("Subscription")).to_be_visible()

    # Scroll vers le bas pour faire apparaître le bouton
    page.mouse.wheel(0, 3000)
    expect(page.get_by_text("Subscription")).to_be_visible()
    btn = page.locator("#scrollUp")
    btn.wait_for(state="visible")
    time.sleep(4)
    btn.click()

    page.wait_for_function("window.scrollY === 0")
    time.sleep(4)
    expect(page.get_by_role("heading",
                            name="Full-Fledged practice website for Automation Engineers").first).to_be_visible()


# firefox
def test_Verify_Scroll_Up_using_Arrow_button_and_Scroll_Down_functionality_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()

    # Scroll vers le bas pour faire apparaître le bouton
    page.mouse.wheel(0, 3000)
    expect(page.get_by_text("Subscription")).to_be_visible()
    btn = page.locator("#scrollUp")
    btn.wait_for(state="visible")
    btn.click()

    page.wait_for_function("window.scrollY === 0")
    expect(page.get_by_role("heading",
                            name="Full-Fledged practice website for Automation Engineers").first).to_be_visible()
    firefoxBrowser.close()
