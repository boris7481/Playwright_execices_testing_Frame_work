from playwright.sync_api import expect
from pathlib import Path
file_path = Path(r"C:\Users\boris\Desktop\test_document_contact_us_page.txt")

class ContactUsPage:
    def __init__(self, page):
        self.page = page
        
        
    def fill_infos(self):
        self.page.get_by_role("link", name=" Contact us").click()
        expect(self.page.get_by_text("GET IN TOUCH")).to_be_visible()
        self.page.get_by_placeholder("name").fill("freedom")
        self.page.locator('[data-qa="email"]').fill("test@test.com")
        self.page.get_by_placeholder("Subject").fill("Feedback")
        self.page.get_by_placeholder("Your Message Here").fill("I wnat to let you kkow that you are amazing")
        self.page.set_input_files('[name="upload_file"]', file_path)
        self.page.get_by_role("button", name="Submit").click()
        self.page.get_by_role("link", name=" Home").click()
        expect(self.page.get_by_text("Features Items")).to_be_visible()