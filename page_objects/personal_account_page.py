import allure

from data import results
from helpers import Tools
from page_objects.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocators as PAPL


class PersonalAccountPage(BasePage):

    @allure.step("Находим и нажимаем на кнопку 'Восстановить' в подменю 'Восстановление пароля'")
    def click_main_button(self):
        self.find_and_click_by_script(element=PAPL.MAIN_BUTTON)

    @allure.step("Вводим значение {email} в поле 'Email'")
    def entry_data_to_field_email(self, email):
        self.entry_data_to_field(element=PAPL.FIELD_FOR_ENTRY_EMAIL, data=email)

    @allure.step("Вводим значение {password} в поле 'Пароль'")
    def entry_data_to_field_password(self, password):
        self.entry_data_to_field(element=PAPL.FIELD_FOR_ENTRY_PASSWORD, data=password)

    @allure.step("Находим и нажимаем на кнопку 'Восстановить' в подменю 'Восстановление пароля'")
    def click_hide_password_button(self):
        self.find_and_click_by_script(element=PAPL.BUTTON_HIDE_PASSWORD)

    @allure.step("Находим и нажимаем на кнопку 'Восстановить пароль' в меню 'Вход'")
    def click_button_restore_password_in_menu_login(self):
        self.find_and_click_by_script(element=PAPL.BUTTON_PASS_TO_PASSWORD_RECOVERY)

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
