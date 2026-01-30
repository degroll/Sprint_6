from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE_OF_PAGE = (By.CLASS_NAME, "Home_Header__iJKdX")
    IMPORTANT_QUESTIONS = (By.CLASS_NAME, "accordion")
    FIRST_QUESTION = (By.ID, "accordion__heading-0")
    SECOND_QUESTION = (By.ID, "accordion__heading-1")
    THIRD_QUESTION = (By.ID, "accordion__heading-2")
    FOURTH_QUESTION = (By.ID, "accordion__heading-3")
    FIFTH_QUESTION = (By.ID, "accordion__heading-4")
    SIXTH_QUESTION = (By.ID, "accordion__heading-5")
    SEVENTH_QUESTION = (By.ID, "accordion__heading-6")
    EIGHTH_QUESTION = (By.ID, "accordion__heading-7")
    FIRST_ANSWER = (By.XPATH, ".//div[@id = 'accordion__panel-0']/p")
    SECOND_ANSWER = (By.XPATH, ".//div[@id = 'accordion__panel-1']/p")
    THIRD_ANSWER = (By.XPATH, ".//div[@id = 'accordion__panel-2']/p")
    FOURTH_ANSWER = (By.XPATH, ".//div[@id = 'accordion__panel-3']/p")
    FIFTH_ANSWER = (By.XPATH, ".//div[@id = 'accordion__panel-4']/p")
    SIXTH_ANSWER = (By.XPATH, ".//div[@id = 'accordion__panel-5']/p")
    SEVENTH_ANSWER = (By.XPATH, ".//div[@id = 'accordion__panel-6']/p")
    EIGHTH_ANSWER = (By.XPATH, ".//div[@id = 'accordion__panel-7']/p")

    SCOOTER_LOGO = (By.XPATH, ".//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, ".//img[@alt='Yandex']")

    HOME_HEADER_TEXT = (By.CLASS_NAME, "Home_Header__iJKdX")

    COOKIE_BUTTON = (By.CLASS_NAME, "App_CookieButton__3cvqF")

    FIRST_ORDER_BUTTON = (By.XPATH, ".//button[text()= 'Статус заказа']/../button[text()='Заказать']")
    SECOND_ORDER_BUTTON = (By.XPATH, ".//div[text()= 'Как это работает']/..//button[text()='Заказать']")

class DzenPageLocator:
    DZEN_LOGO = (By.CLASS_NAME, "dzen-layout--desktop-base-header__logoLink-2h")

class OrderPageFirstLocators:
    NAME_FIELD = (By.XPATH, ".//input[@placeholder= '* Имя']")
    SURNAME_FIELD = (By.XPATH, ".//input[@placeholder= '* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder= '* Адрес: куда привезти заказ']")
    SUBWAY_FIELD = (By.XPATH, ".//input[@placeholder= '* Станция метро']")
    SUBWAY_TEXT = (By.XPATH, ".//div[text()='Комсомольская']")
    PHONE_NUMBER_FIELD = (By.XPATH, ".//input[@placeholder= '* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()= 'Далее']")

class OrderPageSecondLocators:
    DATE_FIELD = (By.XPATH, ".//input[@placeholder= '* Когда привезти самокат']")
    DAY = (By.XPATH, ".//div[text()= '31']")
    RENTAL_PERIOD = (By.XPATH, ".//div[text()= '* Срок аренды']")
    TWO_DAYS_RENTAL = (By.XPATH, ".//div[text()= 'двое суток']")
    COLOUR_LABEL = (By.XPATH, ".//label[text()= 'серая безысходность']")
    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder= 'Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Назад']/../button[text()='Заказать']")

class ConfirmMadalWindowLocator:
    CONFIRM_BUTTON = (By.XPATH, ".//button[text()='Да']")

class CompletedMadalWindowLocator:
    SEE_STATUS_BUTTON = (By.XPATH, ".//button[text()='Посмотреть статус']")
    ORDER_IS_READY = (By.XPATH, ".//div[text()= 'Заказ оформлен']")

