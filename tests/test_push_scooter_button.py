import allure

from pages.base_page import BasePage
from pages.order_page import OrderPage
from data import URL


class TestPushScooterButton:

    @allure.title("Проверка перехода на главную страницу")
    def test_push_scooter(self, driver):
        base_page = BasePage(driver)
        base_page.open()
        base_page.wait_for_load_title()
        base_page.click_order_button(0)
        order_page = OrderPage(driver)
        order_page.click_scooter_logo()
        url = base_page.get_current_url()
        expected_url = URL[0] + "/"
        assert url == expected_url
    