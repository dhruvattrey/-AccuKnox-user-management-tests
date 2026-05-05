from playwright.sync_api import sync_playwright
import time

def test_user_management_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        username = f"qa_auto_{int(time.time())}"
        #  Login into web app
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.wait_for_selector('input[name="username"]')
        page.fill('input[name="username"]', "Admin")
        page.fill('input[name="password"]', "admin123")
        page.click('button[type="submit"]')
        page.wait_for_url("**/dashboard/**")
        # Move to admin
        page.click("text=Admin")
        page.wait_for_timeout(2000)
        #  Add user 
        page.click("button:has-text('Add')")
        page.wait_for_timeout(2000)
        # User Role
        page.locator("(//div[contains(@class,'oxd-select-text')])[1]").click()
        page.click("text=ESS")
        # Employee Name 
        emp = page.locator("input[placeholder='Type for hints...']")
        emp.click()
        emp.fill("a")
        page.wait_for_timeout(3000)
        page.wait_for_selector(".oxd-autocomplete-option")
        page.locator(".oxd-autocomplete-option").first.click()
        # Status
        page.locator("//label[text()='Status']/following::div[contains(@class,'oxd-select-text')][1]").click()
        page.click("text=Enabled")
        # Username
        page.fill("(//input[@class='oxd-input oxd-input--active'])[2]", username)
        # Password
        page.fill("(//input[@type='password'])[1]", "Test@123")
        page.fill("(//input[@type='password'])[2]", "Test@123")
        # Save
        page.click("button:has-text('Save')")
        page.wait_for_timeout(5000)
        # search user
        page.fill("(//input[@class='oxd-input oxd-input--active'])[1]", username)
        page.click("button:has-text('Search')")
        page.wait_for_timeout(2000)
        assert page.locator(f"text={username}").is_visible()
        # edit user
        row = page.locator(f"//div[@role='row'][.//div[text()='{username}']]")
        row.locator("button i.bi-pencil-fill").click()
        page.wait_for_timeout(2000)
        # Change status to Disabled
        page.locator("//label[text()='Status']/following::div[contains(@class,'oxd-select-text')][1]").click()
        page.click("text=Disabled")
        page.click("button:has-text('Save')")
        page.wait_for_timeout(3000)
       # Check edits
        page.fill("(//input[@class='oxd-input oxd-input--active'])[1]", username)
        page.click("button:has-text('Search')")
       # wait to load
        page.wait_for_timeout(2000)
        row = page.locator(f"//div[@role='row']//div[text()='{username}']/ancestor::div[@role='row']")
       # check if status is disabled or not
        assert row.locator("text=Disabled").is_visible()
       # delete the above created user 
        row = page.locator(f"//div[@role='row']//div[text()='{username}']/ancestor::div[@role='row']")
       # click checkbox
        row.locator("span.oxd-checkbox-input").click()
        page.wait_for_timeout(1000)
       # then click delete
        page.click("button:has-text('Delete')")
        page.click("button:has-text('Yes, Delete')")
        page.wait_for_timeout(2000)
        page.wait_for_timeout(2000)
        #search again to confirm deletion
        page.fill("(//input[@class='oxd-input oxd-input--active'])[1]", username)
        page.click("button:has-text('Search')")
        page.wait_for_timeout(2000)

        print("User deleted successfully, test completed")
        page.wait_for_timeout(2000)
        browser.close()