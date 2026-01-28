import allure
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import BasePageLocators
from pages.base_page import BasePage
from data import URL, ANSWERS


class TestBasePage:

    @allure.title("Проверка ответов на вопросы")
    @pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_get_answers(self, number, driver):
        base_page = BasePage(driver)
        base_page.open()
        base_page.wait_for_load_title()
        answer = base_page.get_answer(number)
        assert answer == ANSWERS[number]

    @allure.title("Проверка перенаправления на Дзен")
    def test_yandex_logo_open_dzen_in_new_window(self, driver, main_page, dzen_page):
        main_window = driver.current_window_handle
        main_page.click_yandex_logo()
        assert len(driver.window_handles) == 2
        for window in driver.window_handles:
            if window != main_window:
                driver.switch_to.window(window)
                break
        dzen_page.wait_for_redirect_complete()
        current_url = driver.current_url
        assert current_url == dzen_page.expected_url
        


