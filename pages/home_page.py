from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import conftest


class HomePage(BasePage):
    def __init__(self):
        self.drive = conftest.driver
        self.products_xpath = (By.XPATH, "//span[@class='title']")

    def  verify_text(self, text):
       xpath = self.get_text_element(self.products_xpath)
       assert xpath == text