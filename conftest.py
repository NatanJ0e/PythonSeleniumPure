import pytest
from selenium import webdriver


driver: webdriver.Remote


@pytest.fixture
def set_base():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")


    yield

    driver.quit()