import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By

import conftest


@pytest.mark.usefixtures("set_base")
class TestLogin:

    def test_valid_login(self):
        text = "Products"
        login_page = LoginPage()
        home_page = HomePage()
        login_page.login_access("standard_user", "secret_sauce")
        home_page.verify_text(text)

    def test_invalid_login(self):
        text = "Epic sadface: Username and password do not match any user in this service"
        login_page = LoginPage()
        home_page = HomePage()
        login_page.login_access("standardfsdfr", "secret_savsahef")
        login_page.verify_text_error(text)
