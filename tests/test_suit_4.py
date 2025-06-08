import allure

from data import WEBPAGE, const
from helpers import Generators, Tools


class TestSuit4:

    @allure.title('4-1 Проверка открытия всплывающего окна с деталями при клике на заказ в "Лента заказов"')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», входим в сервис под созданным пользователем, создаем заказ с случайными ингредиентами, переходим в окно "Лента заказов", нажимаем на созданный заказ в списке, проверяем возникновение всплывающего окна с деталями заказа (текст с номером заказа)')
    @allure.story("Тестовый сценарий № 4 'Раздел «Лента заказов»'")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_opening_details_window_for_chosen_order_in_orders_feed(self, order_feed_page, constructor_page, personal_account_page, random_user, random_burger=Generators.generate_random_burger()):
        personal_account_page.open_start_page()
        personal_account_page.logon_by_user(email=random_user[0], password=random_user[1])
        constructor_page.push_button_constructor_on_header()
        order_identifier = constructor_page.make_order_and_return_identifier_number(burger=random_burger)
        order_feed_page.push_button_to_order_feed_on_header()
        order_feed_page.click_on_order_in_order_feed(order_identifier=order_identifier)
        order_feed_page.check_order_number_in_details_window_inside_order_feed(order_identifier=order_identifier)

    @allure.title('4-2 Проверка что заказы из истории в личном кабинете отображаются среди заказов в "Ленте заказов"')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», входим в сервис под созданным пользователем, создаем заказ с случайными ингредиентами, переходим в историю заказов в личном кабинете и узнаем там номер сделанного заказа, переходим в окно "Лента заказов" и ищем там заказ с полученным номером')
    @allure.story("Тестовый сценарий № 4 'Раздел «Лента заказов»'")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_that_orders_in_personal_account_history_presets_in_order_in_orders_feed(self, order_feed_page, constructor_page, personal_account_page, random_user, random_burger=Generators.generate_random_burger()):
        personal_account_page.open_start_page()
        personal_account_page.logon_by_user(email=random_user[0], password=random_user[1])
        constructor_page.push_button_constructor_on_header()
        constructor_page.make_order_and_return_identifier_number(burger=random_burger)
        personal_account_page.push_button_to_personal_account_on_header()
        personal_account_page.click_button_order_history_in_personal_account()
        order_identifier = personal_account_page.get_identifier_number_from_one_order_in_orders_history()
        order_feed_page.push_button_to_order_feed_on_header()
        order_feed_page.click_on_order_in_order_feed(order_identifier=order_identifier)
        order_feed_page.check_order_number_in_details_window_inside_order_feed(order_identifier=order_identifier)

    @allure.title('4-3 Проверка увеличения счетчика выполненных за все время заказов в "Ленте заказов" при создании нового заказа')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», входим в сервис под созданным пользователем, переходим в окно "Лента заказов" и запоминаем текущее значение счетчика заказов, сделанных за все время, переходим в окно конструктора и создаем заказ с случайными ингредиентами, снова переходим в окно "Лента заказов" и запоминаем новое значение счетчика заказов, сделанных за все время, сравниваем старое и новое значение счетчиков заказов')
    @allure.story("Тестовый сценарий № 4 'Раздел «Лента заказов»'")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_counter_all_time_orders_deal_in_orders_feed(self, order_feed_page, constructor_page, personal_account_page, random_user, random_burger=Generators.generate_random_burger()):
        personal_account_page.open_start_page()
        personal_account_page.logon_by_user(email=random_user[0], password=random_user[1])
        order_feed_page.push_button_to_order_feed_on_header()
        all_time_counter_value_1 =  order_feed_page.get_counter_value(counter=const['COUNTER_ALL_TIME_ORDERS_DEAL'])
        constructor_page.push_button_constructor_on_header()
        constructor_page.make_order_and_return_identifier_number(burger=random_burger)
        order_feed_page.push_button_to_order_feed_on_header()
        all_time_counter_value_2 = order_feed_page.get_counter_value(counter=const['COUNTER_ALL_TIME_ORDERS_DEAL'])
        Tools.check_that_value_differs_from_not_expected_value(not_expected_value=all_time_counter_value_1, actually_value=all_time_counter_value_2)

    @allure.title('4-4 Проверка увеличения счетчика выполненных за сегодня заказов в "Ленте заказов" при создании нового заказа')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», входим в сервис под созданным пользователем, переходим в окно "Лента заказов" и запоминаем текущее значение счетчика заказов, сделанных за сегодня, переходим в окно конструктора и создаем заказ с случайными ингредиентами, снова переходим в окно "Лента заказов" и запоминаем новое значение счетчика заказов, сделанных за сегодня, сравниваем старое и новое значение счетчиков заказов')
    @allure.story("Тестовый сценарий № 4 'Раздел «Лента заказов»'")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_counter_today_orders_deal_in_orders_feed(self, order_feed_page, constructor_page, personal_account_page, random_user, random_burger=Generators.generate_random_burger()):
        personal_account_page.open_start_page()
        personal_account_page.logon_by_user(email=random_user[0], password=random_user[1])
        order_feed_page.push_button_to_order_feed_on_header()
        all_time_counter_value_1 = order_feed_page.get_counter_value(counter=const['COUNTER_TODAY_ORDERS_DEAL'])
        constructor_page.push_button_constructor_on_header()
        constructor_page.make_order_and_return_identifier_number(burger=random_burger)
        order_feed_page.push_button_to_order_feed_on_header()
        all_time_counter_value_2 = order_feed_page.get_counter_value(counter=const['COUNTER_TODAY_ORDERS_DEAL'])
        Tools.check_that_value_differs_from_not_expected_value(not_expected_value=all_time_counter_value_1, actually_value=all_time_counter_value_2)

    @allure.title('4-5 Проверка появления в разделе "В работе" в "Ленте заказов" номера оформленного заказа')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», входим в сервис под созданным пользователем, переходим в окно конструктора и создаем заказ с случайными ингредиентами, переходим в окно "Лента заказов", ищем созданный заказ в разделе "В работе" (сверяем номер заказа)')
    @allure.story("Тестовый сценарий № 4 'Раздел «Лента заказов»'")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_order_number_in_progress_section_inside_order_feed_after_making_order(self, order_feed_page, constructor_page, personal_account_page, random_user, random_burger=Generators.generate_random_burger()):
        personal_account_page.open_start_page()
        personal_account_page.logon_by_user(email=random_user[0], password=random_user[1])
        constructor_page.push_button_constructor_on_header()
        order_identifier = constructor_page.make_order_and_return_identifier_number(burger=random_burger)
        order_feed_page.push_button_to_order_feed_on_header()
        order_feed_page.check_order_number_in_progress_section_inside_order_feed(order_identifier=order_identifier)
