from selenium.webdriver.common.by import By


class ConstructorLocators:
    TITLE_ASSEMBLE_THE_BURGER =         (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")
    BUTTON_PLACE_AN_ORDER =             (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    SCROLL_BAR_POSITION =               (By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
    SCROLL_BAR_SAUCES =                 (By.XPATH, "/span[contains(text(), 'Соусы')]")
    SCROLL_BAR_TOPPINGS =               (By.XPATH, "/span[contains(text(), 'Начинки')]")
    SCROLL_BAR_ROLLS =                  (By.XPATH, "/span[contains(text(), 'Булки')]")
    RADIOBUTTON_SAUCES =                (By.XPATH, "//span[contains(text(), 'Соусы')]")
    RADIOBUTTON_TOPPINGS =              (By.XPATH, "//span[contains(text(), 'Начинки')]")
    RADIOBUTTON_ROLLS =                 (By.XPATH, "//span[contains(text(), 'Булки')]")
    TITLE_SAUCES =                      (By.XPATH, "//h2[contains(text(), 'Соусы')]")
    TITLE_TOPPINGS =                    (By.XPATH, "//h2[contains(text(), 'Начинки')]")
    TITLE_ROLLS =                       (By.XPATH, "//h2[contains(text(), 'Булки')]")