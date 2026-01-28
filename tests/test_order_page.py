import allure
import pytest

from pages.base_page import BasePage
from pages.order_page import OrderPage
from data import DATA_ORDER_FIRST, DATA_ORDER_SECOND, EXPECTED_TEXT


class TestOrderPage:

    @allure.title("Проверка кнопок для заказа 1")
    @allure.description("Используются первые данные")
    @pytest.mark.parametrize('number', [0, 1])
    def test_order_buttons_first_data(self, number, driver):
        base_page = BasePage(driver)
        base_page.open()
        base_page.wait_for_load_title()
        base_page.click_order_button(number)
        order_page = OrderPage(driver)
        name = DATA_ORDER_FIRST["name"][0]
        surname = DATA_ORDER_FIRST["surname"][0]
        address = DATA_ORDER_FIRST["address"][0]
        phone_number = DATA_ORDER_FIRST["phone_number"][0]
        order_page.fill_the_first_form(name, surname, address, phone_number)

        comment = DATA_ORDER_SECOND["comment"][0]
        order_page.fill_the_second_form(comment)

        order_page.confirm_the_order()

        expected_text = EXPECTED_TEXT["order_is_ready"]
        text = order_page.get_order_is_ready_text()
        assert expected_text in text

    @allure.title("Проверка кнопок для заказа 2")
    @allure.description("Используются вторые данные")
    @pytest.mark.parametrize('number', [0, 1])
    def test_order_buttons_second_data(self, number, driver):
        base_page = BasePage(driver)
        base_page.open()
        base_page.wait_for_load_title()
        base_page.click_order_button(number)
        order_page = OrderPage(driver)
        name = DATA_ORDER_FIRST["name"][1]
        surname = DATA_ORDER_FIRST["surname"][1]
        address = DATA_ORDER_FIRST["address"][1]
        phone_number = DATA_ORDER_FIRST["phone_number"][1]
        order_page.fill_the_first_form(name, surname, address, phone_number)

        comment = DATA_ORDER_SECOND["comment"][1]
        order_page.fill_the_second_form(comment)

        order_page.confirm_the_order()

        expected_text = EXPECTED_TEXT["order_is_ready"]
        text = order_page.get_order_is_ready_text()
        assert expected_text in text



