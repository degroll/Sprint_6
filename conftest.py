import pytest

from selenium import webdriver
from data import URL

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    from pages.main_page import MainPage
    page = MainPage(driver)
    page.open()
    return page

@pytest.fixture
def dzen_page(driver):
    from pages.dzen_page import DzenPage
    return DzenPage(driver)
