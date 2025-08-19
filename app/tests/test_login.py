import allure
from tests.pages.login_page import LoginPage

@allure.feature("Login")
@allure.story("Valid login flows")
def test_valid_login_orangehrm(page):
    lp = LoginPage(page)
    lp.open()
    lp.login("Admin", "admin123")
    # simple assertion: URL contains 'dashboard' or topbar visible
    page.wait_for_load_state("networkidle")
    assert page.locator("header .oxd-topbar-header").first.is_visible()
