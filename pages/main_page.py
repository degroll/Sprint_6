import allure
from .base_page import BasePage
from locators.locators import BasePageLocators
from data import URL


class MainPage(BasePage):
    cookie_button = BasePageLocators.COOKIE_BUTTON
    questions = {
        0: BasePageLocators.FIRST_QUESTION,
        1: BasePageLocators.SECOND_QUESTION,
        2: BasePageLocators.THIRD_QUESTION,
        3: BasePageLocators.FOURTH_QUESTION,
        4: BasePageLocators.FIFTH_QUESTION,
        5: BasePageLocators.SIXTH_QUESTION,
        6: BasePageLocators.SEVENTH_QUESTION,
        7: BasePageLocators.EIGHTH_QUESTION
    }
    answers = {
        0: BasePageLocators.FIRST_ANSWER,
        1: BasePageLocators.SECOND_ANSWER,
        2: BasePageLocators.THIRD_ANSWER,
        3: BasePageLocators.FOURTH_ANSWER,
        4: BasePageLocators.FIFTH_ANSWER,
        5: BasePageLocators.SIXTH_ANSWER,
        6: BasePageLocators.SEVENTH_ANSWER,
        7: BasePageLocators.EIGHTH_ANSWER
    }
    order_buttons = {
        0: BasePageLocators.FIRST_ORDER_BUTTON,
        1: BasePageLocators.SECOND_ORDER_BUTTON
    }

    yandex_logo = BasePageLocators.YANDEX_LOGO
    url = URL[0]

    @allure.step("Инициализируем драйвер")
    def __init__(self, driver, url=None):
        super().__init__(driver, self.url)

    @allure.step("Нажимаем на логотип <<Яндекс>>")
    def click_yandex_logo(self):
        original_window = self.get_current_window_handle
        yandex = self.wait_for_clicable_element(self.yandex_logo)
        yandex.click()
        return original_window
    
    @allure.step("Получаем количество открытых окон")
    def get_window_count(self):
        return len(self.get_window_handles)
    
    @allure.step("Получаем текст ответа")
    def get_answer(self, number):
        cookie_button = self.find_element(self.cookie_button)
        cookie_button.click()
        self.wait_for_clicable_element(self.questions[number])
        self.click_element(self.questions[number])
        self.wait_for_visibility_element(self.answers[number])
        return self.get_text_element(self.answers[number])
    
    @allure.step("Нажимаем на кнопку заказа")
    def click_order_button(self, num):
        self.wait_for_clicable_element(self.order_buttons[num])
        self.click_element(self.order_buttons[num])
    
