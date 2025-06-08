import allure

from data import results
from helpers import Tools
from page_objects.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocators as PAPL


class PersonalAccountPage(BasePage):

    @allure.step("Находим и нажимаем на кнопку 'Войти' ('Зарегистрироваться', 'Восстановить' или 'Сохранить') в меню 'Вход' ('Регистрация' или 'Восстановление пароля')")
    def click_main_button(self):
        self.find_and_click_by_script(element=PAPL.MAIN_BUTTON)

    @allure.step("Вводим значение {email} в поле 'Email'")
    def entry_data_to_field_email(self, email):
        self.entry_data_to_field(element=PAPL.FIELD_FOR_ENTRY_EMAIL, data=email)

    @allure.step("Вводим значение {password} в поле 'Пароль'")
    def entry_data_to_field_password(self, password):
        self.entry_data_to_field(element=PAPL.FIELD_FOR_ENTRY_PASSWORD, data=password)

    @allure.step("Находим и нажимаем на кнопку 'Показать/скрыть пароль'")
    def click_hide_password_button(self):
        self.find_and_click_by_script(element=PAPL.BUTTON_HIDE_PASSWORD)

    @allure.step("Находим и нажимаем на кнопку 'Зарегистрироваться' в меню 'Вход'")
    def click_button_registration_in_menu_login(self):
        self.find_and_click_by_script(element=PAPL.BUTTON_PASS_TO_REGISTRATION)

    @allure.step("Находим и нажимаем на кнопку 'Восстановить пароль' в меню 'Вход'")
    def click_button_restore_password_in_menu_login(self):
        self.find_and_click_by_script(element=PAPL.BUTTON_PASS_TO_PASSWORD_RECOVERY)

    @allure.step("Находим и нажимаем на кнопку 'История заказов' в личном кабинете")
    def click_button_order_history_in_personal_account(self):
        self.find_and_click_by_script(element=PAPL.BUTTON_ORDERS_HISTORY)

    @allure.step("Производим регистрацию нового пользователя с почтой:{email} и паролем:{password}")
    def register_new_user(self, email, password):
        names = self.find_equal_elements(elements=PAPL.FIELD_FOR_ENTRY_EMAIL)
        names[0].send_keys(email[:email.find('@')])
        names[1].send_keys(email)
        self.entry_data_to_field_password(password=password)
        self.click_main_button()
        self.wait_of_element(PAPL.BUTTON_HIDE_PASSWORD)

    @allure.step("Производим авторизацию пользователя с почтой:{email} и паролем:{password}")
    def logon_by_user(self, email, password):
        self.push_button_to_personal_account_on_header()
        self.entry_data_to_field_email(email=email)
        self.entry_data_to_field_password(password=password)
        self.click_main_button()
        self.wait_of_element(PAPL.TITLE_ASSEMBLE_THE_BURGER)

    @allure.step("Проверяем наличие и отображение кнопки 'Восстановить' в подменю 'Восстановление пароля'")
    def check_that_restore_button_is_present_in_menu_restore_password(self):
        Tools.check_text_of_element(expected_value=results['BUTTON_TO_RECOVERY_TEXT'], actually_value=self.get_element(PAPL.MAIN_BUTTON).text)

    @allure.step("Проверяем наличие и отображение поля для ввода нового пароля в подменю 'Восстановление пароля'")
    def check_that_input_for_new_password_is_present_in_menu_restore_password(self):
        Tools.check_text_of_element(expected_value=results['FIELD_TO_CHANGE_PASSWORD_TEXT'], actually_value=self.get_element(PAPL.FIELD_FOR_ENTRY_PASSWORD).get_attribute('name'))

    @allure.step("Проверяем атрибут 'type' элемента, имеющего значение атрибута 'value' равное {password}, на соответствие значению 'text' - что характеризует его как поле без сокрытия значения внутри")
    def check_input_password_is_not_hide(self, password):
        field_vs_password_locator = (PAPL.FIELD_VS_PASSWORD[0], Tools.replace_string_in_locator(locator=PAPL.FIELD_VS_PASSWORD[1], string_to_replace="###", new_string=password))
        Tools.check_text_of_element(expected_value=results['FIELD_WITH_OUT_HIDE_TYPE'], actually_value=self.get_element(field_vs_password_locator).get_attribute('type'))

    @allure.step("Проверяем наличие и отображение кнопки 'Войти' в меню 'Вход'")
    def check_that_login_button_is_present_in_menu_enter(self):
        Tools.check_text_of_element(expected_value=results['BUTTON_LOGIN_TEXT'], actually_value=self.get_element(PAPL.MAIN_BUTTON).text)

    @allure.step("Проверяем наличие описательной надписи в личном кабинете авторизованного пользователя")
    def check_we_inside_personal_account(self):
        Tools.check_text_of_element(expected_value=results['PERSONAL_ACCOUNT_TITLE_INFO_TEXT'], actually_value=self.get_element(PAPL.TITLE_INFO).text)

    @allure.step("Проверяем наличие поля для отображения истории заказов в соответствующем подменю личного кабинета")
    def check_orders_history_dashboard_is_present_in_order_history_of_personal_account(self):
        self.check_present_of_element(PAPL.ORDERS_HISTORY_DASHBOARD)