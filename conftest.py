import pytest

from selenium import webdriver
from pages.main_page import MainPage
from pages.dzen_page import DzenPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open()
    return page

@pytest.fixture
def dzen_page(driver):
    return DzenPage(driver)
