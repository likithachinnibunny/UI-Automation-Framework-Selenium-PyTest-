from pages.login_page import LoginPage
from utils.config import BASE_URL, VALID_USER, VALID_PASS

def test_valid_login(driver):
    page = LoginPage(driver)
    page.open(BASE_URL)
    page.login(VALID_USER, VALID_PASS)
    assert "You logged into a secure area!" in page.get_flash()

def test_invalid_login(driver):
    page = LoginPage(driver)
    page.open(BASE_URL)
    page.login("wrong", "wrong")
    assert "Your username is invalid!" in page.get_flash()
