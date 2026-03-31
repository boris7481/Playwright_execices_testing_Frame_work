from playwright.sync_api import  expect


# Test Case 7: Verify Test Cases Page
# ---#termes = ID ,   .terms = class
# Test Case 6: Contact Us Form
def test_Verify_Test_Cases_Page(go_to_page_einwilligen):
    page = go_to_page_einwilligen
    expect(page.get_by_text("Features Items")).to_be_visible()
    page.get_by_role("button", name="Test Cases").click()
    expect(page.get_by_text("Feedback for Us")).to_be_visible()


# firefox
def test_Verify_Test_Cases_Page_firefox(test_login_User_firefox_consent):
    page = test_login_User_firefox_consent
    expect(page.get_by_text("Features Items")).to_be_visible()
    page.get_by_role("button", name="Test Cases").click()
    expect(page.get_by_text("Feedback for Us")).to_be_visible()
