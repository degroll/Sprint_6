import allure

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import BasePageLocators
from data import URL



class BasePage:

    expected_url = URL[3]
    TITLE_OF_PAGE = BasePageLocators.TITLE_OF_PAGE

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
    
    @allure.step("Получаем текст элемента")
    def get_text_element(self, element):
        return self.driver.find_element(*element).text
    
    @allure.step("Получаем url страницы")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Ожидаем перенаправление")
    def wait_for_redirect_complete(self):
        try:
            self.wait.until(expected_conditions.url_to_be(self.expected_url))
            return True
        except:
            self.wait.until(expected_conditions.url_contains("dzen.ru"))

    @allure.step("Получаем текущий дескриптор окна")
    def get_current_window_handle(self):
        return self.driver.current_window_handle
    
    @allure.step("Получаем дескриптор окна")
    def get_window_handles(self):
        return self.driver.window_handles
    
    @allure.step("Переключаемся на другое окно")
    def switch_to_window(self, window):
        return self.driver.switch_to.window(window)







    
