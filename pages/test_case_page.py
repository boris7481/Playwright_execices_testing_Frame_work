from playwright.sync_api import expect


class TestCasePage:
    def __init__(self, page):
        self.page = page

    def test_Verify_Test_Cases_Page_methods(self):
        expect(self.page.get_by_text("Features Items")).to_be_visible()
        self.page.get_by_role("button", name="Test Cases").click()
        expect(self.page.get_by_text("Feedback for Us")).to_be_visible()

