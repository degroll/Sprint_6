import allure

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import BasePageLocators
from data import URL
import time

class BasePage:
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
    
    TITLE_OF_PAGE = BasePageLocators.TITLE_OF_PAGE
    COOKIE_BUTTON = BasePageLocators.COOKIE_BUTTON

    @allure.step("Инициализируем драйвер")
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 3)

    @allure.step("Открываем страницу")
    def open(self):
        self.driver.get(URL[0])
        return self
    
    @allure.step("Ищем элемент")
    def find_element(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    
    @allure.step("Переключаемся на новое окно")
    def switch_to_new_window(self, main_window):
        self.wait.until(lambda d: len(d.window_handles) > len([main_window]))
        for window_handle in self.driver.window_handles:
            if window_handle != main_window:
                self.driver.switch_to.window(window_handle)
                return window_handle
        raise Exception("Новое окно не найдено")
    
    @allure.step("Ожидаем загрузку названия страницы")
    def wait_for_load_title(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.TITLE_OF_PAGE))

    @allure.step("Ожидаем, когда элемент станет видимым")
    def wait_for_visibility_element(self, element):
        return self.wait.until(expected_conditions.visibility_of_element_located(element))

    @allure.step("Ожидаем, когда элемент исчезнет")
    def wait_for_invisibility_element(self, element):
        return self.wait.until(expected_conditions.invisibility_of_element_located(element))

    @allure.step("Ожидаем, когда на элемент можно нажать")
    def wait_for_clicable_element(self, element):
        return self.wait.until(expected_conditions.element_to_be_clickable(element))

    @allure.step("Нажимаем на элемент")
    def click_element(self, element):
        current_element = self.driver.find_element(*element)
        current_element.location_once_scrolled_into_view
        action = ActionChains(self.driver)
        action.move_to_element(current_element).click().perform()

    @allure.step("Нажимаем на кнопку заказа")
    def click_order_button(self, num):
        self.wait_for_clicable_element(self.order_buttons[num])
        self.click_element(self.order_buttons[num])
    
    @allure.step("Получаем текст элемента")
    def get_text_element(self, element):
        return self.driver.find_element(*element).text
    
    @allure.step("Получаем url страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получаем текст ответа")
    def get_answer(self, number):
        cookie_button = self.driver.find_element(*self.COOKIE_BUTTON)
        cookie_button.click()
        self.wait_for_clicable_element(self.questions[number])
        self.click_element(self.questions[number])
        self.wait_for_visibility_element(self.answers[number])
        return self.get_text_element(self.answers[number])







    
