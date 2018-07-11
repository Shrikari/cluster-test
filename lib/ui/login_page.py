from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def wait_for_login_page_to_load(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of(self.driver.find_element_by_id('whiteBoxWithLogo')))

    def get_username_textbox(self):
        try:
            return self.driver.find_element_by_id('username')
        except:
            return None

    def get_password_textbox(self):
        try:
            return self.driver.find_element_by_name('pwd')
        except:
            return None

    def get_keep_me_logged_textbox(self):
        try:
            return self.driver.find_element_by_id('keepLoggedInCheckbox')
        except:
            return None

    def get_login_button(self):
        try:
            return self.driver.find_element_by_id('loginButton')
        except:
            return None

    def get_login_error_msg(self):
        try:
            return self.driver.find_element_by_xpath("//span[contains(text(), 'Please try again')]")
        except:
            return None