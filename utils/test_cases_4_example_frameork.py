# Test Case 14: Place Order: Register while Checkout
from pathlib import Path
import json
import  pytest
from playwright.sync_api import Page, expect, Playwright

import time

# ---#termes = ID ,   .terms = class
# Test Case 6: Contact Us Form

# json file ->util->access into test
file_path = Path(__file__).parent.parent / "data" / "test_users.json"
with open(file_path) as f:
    test_data = json.load(f)  # --> Json file will be transform in python object
    print(test_data)
user_credentials_list = test_data["user_credentials"]


# user_credentials is like our iterable one credentials will be pick on user_credentials_list
# this will be store in user_credentials and run the test and so on for all credentials in user_credentials_list
@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_Logout_User_frmaework(page: Page, user_credentials):
    # the user_credentials in the definition here is a fixture that we need to define in conftest
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    page.locator('[data-qa="login-email"]').fill(user_credentials["userEmail"])
    page.locator('[data-qa="login-password"]').fill(user_credentials["userPassword"])
    page.locator('[data-qa="login-button"]').click()
    expect(page.get_by_text("Logged in as 09w0823@Freedom")).to_be_visible()
    page.get_by_role("link", name="logout").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    time.sleep(2)
