from selenium.webdriver.common.by import By


class BasePageLocators:
    # Основные элементы:
    LOGO =                              (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    BUTTON_TO_CONSTRUCTOR =             (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    BUTTON_TO_ORDER_FEED =              (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")
    BUTTON_TO_PERSONAL_ACCOUNT =        (By.XPATH, "//a[@href='/account']")
