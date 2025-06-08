import allure
from time import sleep as pause

from data import WEBPAGE


class TestSuit2:

    @allure.title('2-1 Проверка перехода в окно "Вход" кликом по кнопке "Личный кабинет" в хедере для не авторизированного пользователя')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», переходим в окно "Вход" через кнопку "Личный кабинет" в хедере, проверяем наличие кнопки "Войти" (ее текстовое содержимое)')
    @allure.story("Тестовый сценарий № 2 'Личный кабинет'")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_button_personal_account_in_header_pass_to_window_enter_if_user_not_authorized(self, personal_account_page):
        personal_account_page.open_start_page()
        personal_account_page.push_button_to_personal_account_on_header()
        personal_account_page.check_that_login_button_is_present_in_menu_enter()

    @allure.title('2-2 Проверка перехода в окно личного кабинета кликом по кнопке "Личный кабинет" в хедере для авторизированного пользователя')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», входим в сервис под созданным пользователем, открываем главную страницу сервиса «Stellar Burgers», переходим в окно личного кабинета через кнопку "Личный кабинет" в хедере, проверяем наличие описательной надписи в личном кабинете (ее текстовое содержимое)')
    @allure.story("Тестовый сценарий № 2 'Личный кабинет'")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_button_personal_account_in_header_pass_to_window_enter_if_user_authorized(self, personal_account_page, random_user):
        personal_account_page.open_start_page()
        personal_account_page.logon_by_user(email=random_user[0], password=random_user[1])
        personal_account_page.push_button_to_personal_account_on_header()
        personal_account_page.check_we_inside_personal_account()

    @allure.title('2-3 Проверка перехода в переход в раздел "История заказов" кликом по соответствующей кнопке в личном кабинете')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», входим в сервис под созданным пользователем, открываем главную страницу сервиса «Stellar Burgers», переходим в окно личного кабинета через кнопку "Личный кабинет" в хедере, переходим в историю заказов кликом по соответствующей кнопке, проверяем наличие соответствующего поля с историей заказов')
    @allure.story("Тестовый сценарий № 2 'Личный кабинет'")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_button_order_history_in_personal_account_pass_to_order_history_dashboard(self, personal_account_page, random_user):
        personal_account_page.open_start_page()
        personal_account_page.logon_by_user(email=random_user[0], password=random_user[1])
        personal_account_page.push_button_to_personal_account_on_header()
        personal_account_page.click_button_order_history_in_personal_account()
        personal_account_page.check_orders_history_dashboard_is_present_in_order_history_of_personal_account()

    @allure.title('2-4 Проверка выход из аккаунта')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», входим в сервис под созданным пользователем, переходим в окно личного кабинета через кнопку "Личный кабинет" в хедере, нажимаем кнопку "Выйти", переходим в меню "Конструктор", нажимаем на кнопку "Личный кабинет" в хедере, проверяем наличие кнопки "Войти" в меню "Вход" (вариант для не авторизированного пользователя)')
    @allure.story("Тестовый сценарий № 2 'Личный кабинет'")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_button_exit_from_account_in_personal_account_exiting_from_account(self, personal_account_page, random_user):
        personal_account_page.open_start_page()
        personal_account_page.logon_by_user(email=random_user[0], password=random_user[1])
        personal_account_page.push_button_to_personal_account_on_header()
        personal_account_page.click_button_exit_from_account_in_personal_account()
        personal_account_page.push_button_to_personal_account_on_header()
        personal_account_page.check_that_login_button_is_present_in_menu_enter()
