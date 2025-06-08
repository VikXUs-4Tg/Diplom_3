from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    # Основные элементы:
    FIELD_FOR_ENTRY_EMAIL =             (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='text']")
    FIELD_FOR_ENTRY_PASSWORD =          (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='password']")
    MAIN_BUTTON =                       (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    # Кнопки навигации в главном меню:
    BUTTON_PASS_TO_LOGIN =              (By.XPATH, "//a[@href='/login']")
    BUTTON_PASS_TO_REGISTRATION =       (By.XPATH, "//a[@href='/register']")
    BUTTON_PASS_TO_PASSWORD_RECOVERY =  (By.XPATH, "//a[@href='/forgot-password']")
    # Элементы для работы с полем, содержащим пароль:
    BUTTON_HIDE_PASSWORD =              (By.XPATH, "//div[@class='input__icon input__icon-action']")
    FIELD_VS_PASSWORD =                 (By.XPATH, "//input[@value='###']")
    FLAG_OF_INCORRECT_PASSWORD =        (By.XPATH, "//p[@class='input__error text_type_main-default']")
    # Элементы в личном кабинете:
    BUTTON_PROFILE =                    (By.XPATH, "//a[@href='/account/profile']")
    BUTTON_ORDERS_HISTORY =             (By.XPATH, "//a[@href='/account/order-history']")
    BUTTON_EXITING_FROM_ACCOUNT =       (By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")
    TITLE_INFO =                        (By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']")
    # Элементы в истории заказов:
    ORDERS_HISTORY_DASHBOARD =          (By.XPATH, "//ul[@class='OrderHistory_profileList__374GU OrderHistory_list__KcLDB']")
    # Локатор на странице конструктора в целях стабилизации тесов
    TITLE_ASSEMBLE_THE_BURGER =         (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")
