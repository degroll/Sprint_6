import allure

from .main_page import MainPage
from locators.locators import DzenPageLocator
from data import URL


class DzenPage(MainPage):
    expected_url = URL[3]
    DZEN_LOGO = DzenPageLocator.DZEN_LOGO

    @allure.step("Инициализируем драйвер")
    def __init__(self, driver):
        super().__init__(driver, self.expected_url)

    @allure.step("Ожидаем перенаправление и получаем url")
    def redirect_complete_and_url(self):
        self.wait_for_redirect_complete()
        return self.get_current_url()
    
    @allure.step("Переключаемся на новое окно")
    def switch_to_new_window(self, main_window=None):
        if main_window is None:
            main_window = self.get_current_window_handle()
        for window in self.get_window_handles():
            if window != main_window:
                self.switch_to_window(window)
                break
    

    
