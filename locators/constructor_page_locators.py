from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    # Основные элементы:
    TITLE_ASSEMBLE_THE_BURGER =         (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")
    BUTTON_PLACE_AN_ORDER =             (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    # Выбор ингредиентов:
    ELEMENT_INGREDIENT =                (By.XPATH, "//a[@href='/ingredient/###']")
    INGREDIENT_NAME_IN_PROPERTIES =     (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")
    BUTTON_CLOSE_PROPERTIES_WINDOW =    (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    SECTION_OF_INGREDIENT_PROPERTIES =  (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")
    # Локатор на странице входа в персональный аккаунт в целях стабилизации тесов
    MAIN_BUTTON =                       (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")