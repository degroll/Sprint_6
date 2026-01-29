import allure

from .base_page import BasePage
from locators.locators import DzenPageLocator
from data import URL


class DzenPage(BasePage):
    expected_url = URL[3]
    DZEN_LOGO = DzenPageLocator.DZEN_LOGO

    @allure.step("Инициализируем драйвер")
    def __init__(self, driver):
        super().__init__(driver, self.expected_url)

    @allure.step("Ожидаем перенаправление и получаем url")
    def redirect_complete_and_url(self):
        self.wait_for_redirect_complete()
        return self.get_current_url()
    

    
