from playwright.sync_api import expect


class HomePage:
# ceci est un commentaire juste pour tester un pull reqauest sur le git hub
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.automationexercise.com/")

    def selectordernavigationlink(self):
        self.page.get_by_role("button", name="Einwilligen").click()
        self.page.get_by_role("link", name="Signup / Login").click()
        expect(self.page.get_by_text("Video Tutorials")).to_be_visible()
