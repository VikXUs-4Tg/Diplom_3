import allure

from data import WEBPAGE
from helpers import Generators


class TestSuit1:

    @allure.title('1-1 Проверка перехода в подменю восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», переходим в окно логина через кнопку в хедере, нажимаем кнопку "Восстановить пароль", проверяем наличие кнопки "Восстановить" (ее текстовое содержимое)')
    @allure.story("Тестовый сценарий № 1")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_button_recovery_password_in_window_login_pass_to_password_recovery_window(self, personal_account_page):
        personal_account_page.push_button_to_personal_account_on_header()
        personal_account_page.click_button_restore_password_in_menu_login()
        personal_account_page.check_that_restore_button_is_present_in_menu_restore_password()

    @allure.title('1-2 Проверка ввода почты и прохождения клика по кнопке "Восстановить" в подменю восстановления пароля')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», переходим в окно логина через кнопку в хедере, нажимаем кнопку "Восстановить пароль", вводим значение случайного почтового ящика в поле "Email", нажимаем кнопку "Восстановить", проверяем наличие поля для ввода нового пароля (значение его атрибута "name")')
    @allure.story("Тестовый сценарий № 1")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_main_button_in_password_recovery_window_pass_to_change_password_menu_if_email_is_inputted(self, personal_account_page, random_email=Generators.generate_random_email()):
        personal_account_page.push_button_to_personal_account_on_header()
        personal_account_page.click_button_restore_password_in_menu_login()
        personal_account_page.entry_data_to_field_email(email=random_email)
        personal_account_page.click_main_button()
        personal_account_page.check_that_input_for_new_password_is_present_in_menu_restore_password()

    @allure.title('1-3 Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его в подменю восстановления пароля')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», переходим в окно логина через кнопку в хедере, нажимаем кнопку "Восстановить пароль", вводим значение случайного почтового ящика в поле "Email", нажимаем кнопку "Восстановить", вводим значение в поле присвоения нового пароля и нажимаем кнопку "Показать/скрыть", проверяем что пароль стал видимым (значение его атрибута "type")')
    @allure.story("Тестовый сценарий № 1")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_hide_button_in_password_recovery_window_show_password_when_clik(self, personal_account_page, random_email=Generators.generate_random_email(), random_password=Generators.generate_random_password()):
        personal_account_page.push_button_to_personal_account_on_header()
        personal_account_page.click_button_restore_password_in_menu_login()
        personal_account_page.entry_data_to_field_email(email=random_email)
        personal_account_page.click_main_button()
        personal_account_page.entry_data_to_field_password(password=random_password)
        personal_account_page.click_hide_password_button()
        personal_account_page.check_input_password_is_not_hide(password=random_password)
