import allure

from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import URL


class TestPushScooterButton:

    @allure.title("Проверка перехода на главную страницу")
    def test_push_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.wait_for_load_title()
        main_page = MainPage(driver)
        main_page.click_order_button(0)
        order_page = OrderPage(driver)
        order_page.click_scooter_logo()
        url = main_page.get_current_url()
        expected_url = URL[0] + "/"
        assert url == expected_url
    