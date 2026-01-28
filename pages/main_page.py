import allure
from .base_page import BasePage
from locators.locators import BasePageLocators
from data import URL


class MainPage(BasePage):
    yandex_logo = BasePageLocators.YANDEX_LOGO
    SCOOTER_LOGO = BasePageLocators.SCOOTER_LOGO
    HOME_HEADER_TEXT = BasePageLocators.HOME_HEADER_TEXT
    url = URL[0]

    @allure.step("Инициализируем драйвер")
    def __init__(self, driver):
        super().__init__(driver, self.url)

    @allure.step("Нажимаем на логотип <<Яндекс>>")
    def click_yandex_logo(self):
        original_window = self.driver.current_window_handle
        yandex = self.wait_for_clicable_element(self.yandex_logo)
        yandex.click()
        return original_window
    
    @allure.step("Получаем количество открытых окон")
    def get_window_count(self):
        return len(self.driver.window_handles)
    
