from selenium.webdriver.common.by import By

class LoginPage:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def login(self, user, pwd):
        self.driver.find_element(*self.USERNAME).send_keys(user)
        self.driver.find_element(*self.PASSWORD).send_keys(pwd)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def get_flash(self):
        return self.driver.find_element(*self.FLASH).text
