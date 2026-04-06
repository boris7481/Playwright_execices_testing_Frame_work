from playwright.sync_api import expect


# Test Case 10: Verify Subscription in home page
# ---#termes = ID ,   .terms = class
# Test Case 6: Contact Us Form
def test_Verify_Subscription_in_home_page(go_to_page_einwilligen):
    page = go_to_page_einwilligen
    expect(page.get_by_text("Subscription")).to_be_visible()
    page.get_by_placeholder("Your email address").fill("freedomvision@gmail.com")
    page.locator("#subscribe").click()
    expect(page.get_by_text("You have been successfully subscribed")).to_be_visible()


# Firefox
def test_Verify_Subscription_in_home_page_firefox(go_to_page_einwilligen):
    page = go_to_page_einwilligen
    expect(page.get_by_text("Subscription")).to_be_visible()
    page.get_by_placeholder("Your email address").fill("freedomvision@gmail.com")
    page.locator("#subscribe").click()
    expect(page.get_by_text("You have been successfully subscribed")).to_be_visible()
