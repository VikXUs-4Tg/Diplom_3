from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO =                              (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")
    BUTTON_TO_PERSONAL_ACCOUNT =        (By.XPATH, ".//a[@href='/account']")
    BUTTON_TO_CONSTRUCTOR =             (By.XPATH, ".//p[contains(text(), 'Конструктор')]")

class AuthorizationRegistrationAndPasswordRecoveryWindowsLocators:
    FIELD_FOR_ENTRY_NAME =              (By.XPATH, ".//input[@name='name']")
    FIELD_FOR_ENTRY_PASSWORD =          (By.XPATH, ".//input[@name='Пароль']")
    BUTTON_TO_LOGIN =                   (By.XPATH, ".//button[contains(text(), 'Войти')]")
    BUTTON_PASS_TO_REGISTRATION =       (By.XPATH, ".//a[@href='/register']")
    BUTTON_PASS_TO_PASSWORD_RECOVERY =  (By.XPATH, ".//a[@href='/forgot-password']")
    BUTTON_PASS_TO_LOGIN =              (By.XPATH, ".//a[@href='/login']")
    BUTTON_TO_REGISTRATION =            (By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]")
    FLAG_OF_INCORRECT_PASSWORD =        (By.XPATH, ".//p[@class='input__error text_type_main-default']")

class PersonalAccountLocators:
    TITLE_INFO =                        (By.XPATH, ".//p[@class='Account_text__fZAIn text text_type_main-default']")
    BUTTON_EXITING_FROM_ACCOUNT =       (By.XPATH, ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")

class ConstructorLocators:
    TITLE_ASSEMBLE_THE_BURGER =         (By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10']")
    BUTTON_PLACE_AN_ORDER =             (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    SCROLL_BAR_POSITION =               (By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
    SCROLL_BAR_SAUCES =                 (By.XPATH, "./span[contains(text(), 'Соусы')]")
    SCROLL_BAR_TOPPINGS =               (By.XPATH, "./span[contains(text(), 'Начинки')]")
    SCROLL_BAR_ROLLS =                  (By.XPATH, "./span[contains(text(), 'Булки')]")
    RADIOBUTTON_SAUCES =                (By.XPATH, ".//span[contains(text(), 'Соусы')]")
    RADIOBUTTON_TOPPINGS =              (By.XPATH, ".//span[contains(text(), 'Начинки')]")
    RADIOBUTTON_ROLLS =                 (By.XPATH, ".//span[contains(text(), 'Булки')]")
    TITLE_SAUCES =                      (By.XPATH, ".//h2[contains(text(), 'Соусы')]")
    TITLE_TOPPINGS =                    (By.XPATH, ".//h2[contains(text(), 'Начинки')]")
    TITLE_ROLLS =                       (By.XPATH, ".//h2[contains(text(), 'Булки')]")