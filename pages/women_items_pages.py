from playwright.sync_api import expect


class Women:

    def __init__(self, page):
        self.page = page

    def access_women_itens(self):
        expect(self.page.get_by_text("Women - Dress Products")).to_be_visible()