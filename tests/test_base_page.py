import allure
import pytest
from pages.main_page import MainPage
from pages.dzen_page import DzenPage
from data import ANSWERS


class TestBasePage:

    @allure.title("Проверка ответов на вопросы")
    @pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_get_answers(self, number, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.wait_for_load_title()
        answer = main_page.get_answer(number)
        assert answer == ANSWERS[number]

    @allure.title("Проверка перенаправления на Дзен")
    def test_yandex_logo_open_dzen_in_new_window(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_window = main_page.get_current_window_handle()
        main_page.click_yandex_logo()
        assert len(main_page.get_window_handles()) == 2
        dzen_page = DzenPage(driver)
        dzen_page.switch_to_new_window(main_window)
        dzen_page.redirect_complete_and_url()
        current_url = dzen_page.get_current_url()
        assert current_url == dzen_page.expected_url
        


