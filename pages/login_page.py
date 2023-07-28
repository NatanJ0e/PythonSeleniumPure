from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import conftest


class LoginPage(BasePage):

    def __init__(self):
        self.drive = conftest.driver
        self.username = (By.ID, "user-name")
        self.key = (By.ID, "password")
        self.button = (By.ID, "login-button")
        self.err_xpath = (By.XPATH, "//div[@class='error-message-container error']")


    def login_access(self, user, key):
        self.fill_element_by_Id(self.username, user)
        self.fill_element_by_Id(self.key, key)
        self.click_button_by_id(self.button)

    def verify_text_error(self, text):
        xpath = self.get_text_element(self.err_xpath)
        assert xpath == text

