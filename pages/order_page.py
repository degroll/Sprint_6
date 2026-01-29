import allure

from selenium.webdriver.common.action_chains import ActionChains
from locators.locators import BasePageLocators, OrderPageFirstLocators, OrderPageSecondLocators, ConfirmMadalWindowLocator, CompletedMadalWindowLocator
from .main_page import MainPage

from data import URL

class OrderPage(MainPage):
    scooter_logo = BasePageLocators.SCOOTER_LOGO
    url = URL[0]
    name_field = OrderPageFirstLocators.NAME_FIELD
    surname_field = OrderPageFirstLocators.SURNAME_FIELD
    address_field = OrderPageFirstLocators.ADDRESS_FIELD
    subway_field = OrderPageFirstLocators.SUBWAY_FIELD
    subway_station = OrderPageFirstLocators.SUBWAY_TEXT
    phone_number_field = OrderPageFirstLocators.PHONE_NUMBER_FIELD

    next_button = OrderPageFirstLocators.NEXT_BUTTON

    date_field = OrderPageSecondLocators.DATE_FIELD
    day = OrderPageSecondLocators.DAY
    rental_period = OrderPageSecondLocators.RENTAL_PERIOD
    two_days_rental = OrderPageSecondLocators.TWO_DAYS_RENTAL
    colour = OrderPageSecondLocators.COLOUR_LABEL
    comment_field = OrderPageSecondLocators.COMMENT_FIELD
    order_button = OrderPageSecondLocators.ORDER_BUTTON

    confirm_button = ConfirmMadalWindowLocator.CONFIRM_BUTTON

    see_status_button = CompletedMadalWindowLocator.SEE_STATUS_BUTTON
    order_is_ready = CompletedMadalWindowLocator.ORDER_IS_READY

    @allure.step("Инициализируем драйвер")
    def __init__(self, driver):
        super().__init__(driver, self.url)

    @allure.step("Заполняем данные в элемент")
    def send_keys(self, element, data):
        return self.find_element(element).send_keys(data)
    
    @allure.step("Нажимаем на логотип <<Самокат>>")
    def click_scooter_logo(self):
        self.wait_for_visibility_element(self.phone_number_field)
        self.click_element(self.scooter_logo)
    
    @allure.step("Нажимаем на dropdown и выбираем нужный элемент")
    def select_from_dropdown(self, element, text):
        self.wait_for_clicable_element(element)
        current_element = self.find_element(element)
        current_element.location_once_scrolled_into_view
        actions = ActionChains(self.driver)
        actions.move_to_element(current_element).click().perform()
        current_text = self.find_element(text)
        current_text.location_once_scrolled_into_view
        actions = ActionChains(self.driver)
        actions.move_to_element(current_text).click().perform()
    
    @allure.step("Заполняем данные в первую форму")
    def fill_the_first_form(self, name, surname, address, phone_number):
        self.wait_for_visibility_element(self.phone_number_field)
        self.send_keys(self.name_field, name)
        self.send_keys(self.surname_field, surname)
        self.send_keys(self.address_field, address)
        self.select_from_dropdown(self.subway_field, self.subway_station)
        self.send_keys(self.phone_number_field, phone_number)
        self.click_element(self.next_button)

    @allure.step("Заполняем данные во вторую форму")
    def fill_the_second_form(self, comment):
       self.wait_for_visibility_element(self.date_field)
       self.select_from_dropdown(self.date_field, self.day)
       self.wait_for_invisibility_element(self.day)
       self.select_from_dropdown(self.rental_period, self.two_days_rental)
       self.click_element(self.colour)
       self.send_keys(self.comment_field, comment)
       self.click_element(self.order_button)

    @allure.step("Подтверждаем заказ")
    def confirm_the_order(self):
        self.wait_for_visibility_element(self.date_field)
        self.click_element(self.confirm_button)

    @allure.step("Получаем текст, что заказ оформлен")
    def get_order_is_ready_text(self):
        return self.find_element(self.order_is_ready).text







