import conftest
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self):
        self.drive = conftest.driver

    def fill_element_by_Id(self, id, keys):
        return self.drive.find_element(*id).send_keys(keys)

    def click_button_by_id(self, id):
        return self.drive.find_element(*id).click()

    def get_text_element(self, locator):
        return self.drive.find_element(*locator).text
