# Test Case 26: Verify Scroll Up without 'Arrow' button and Scroll Down functionality

# Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality
from playwright.sync_api import Page, expect, Playwright
import time


# ---#termes = ID ,   .terms = class      09w0823@Freedom
def test_Verify_Scroll_Up_using_Arrow_button_and_Scroll_Down_unctionality(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    # 1️ Scroll vers le bas
    page.mouse.wheel(0, 5000)
    time.sleep(2)
    # 2️ Vérifier texte en bas
    expect(page.get_by_text("Subscription").first).to_be_visible()
    time.sleep(2)  # --> to see well
    # 3️ Scroll vers le haut (sans cliquer)
    page.evaluate("window.scrollTo(0, 0)")
    time.sleep(2)  # --> to see well
    # Attendre que le scroll soit terminé
    page.wait_for_function("window.scrollY === 0")

    # 4️ Vérifier texte en haut
    expect(page.get_by_role("heading",name="Full-Fledged practice website for Automation Engineers").first).to_be_visible()


# firefox
def test_Verify_Scroll_Up_using_Arrow_button_and_Scroll_Down_unctionality_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    # 1️ Scroll vers le bas
    page.mouse.wheel(0, 5000)
    time.sleep(2)
    # 2️ Vérifier texte en bas
    expect(page.get_by_text("Subscription").first).to_be_visible()
    time.sleep(2)  # --> to see well
    # 3️ Scroll vers le haut (sans cliquer)
    page.evaluate("window.scrollTo(0, 0)")
    time.sleep(2)  # --> to see well
    # Attendre que le scroll soit terminé
    page.wait_for_function("window.scrollY === 0")
    # 4️ Vérifier texte en haut
    expect(page.get_by_role("heading",name="Full-Fledged practice website for Automation Engineers").first).to_be_visible()
    firefoxBrowser.close()
