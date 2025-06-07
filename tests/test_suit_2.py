from time import sleep as pause

import allure

from data import WEBPAGE

"""
class TestSuit1:

    @allure.title('2-1 Проверка перехода в подменю восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», переходим в окно логина через кнопку в хедере, нажимаем кнопку "Восстановить пароль", проверяем наличие кнопки "Восстановить" (ее текстовое содержимое)')
    @allure.story("Тестовый сценарий № 2")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_button_recovery_password_in_window_login_pass_to_password_recovery_window(self, personal_account_page):
        personal_account_page.push_button_to_personal_account_on_header()
        personal_account_page.click_button_restore_password_in_menu_login()
        personal_account_page.check_that_restore_button_is_present_in_menu_restore_password()
"""