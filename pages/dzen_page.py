import allure

from selenium.webdriver.support import expected_conditions
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
    def wait_for_redirect_complete(self):
        try:
            self.wait.until(expected_conditions.url_to_be(self.expected_url))
            return True
        except:
            self.wait.until(expected_conditions.url_contains("dzen.ru"))
        return self.get_current_url()
    

    
