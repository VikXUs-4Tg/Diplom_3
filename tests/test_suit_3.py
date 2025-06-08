from time import sleep as pause

import allure

from data import WEBPAGE
from helpers import Generators


class TestSuit3:

    @allure.title('3-1 Проверка перехода в окно "Конструктор" кликом по кнопке "Конструктор" в хедере')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», переходим в окно "Вход" через кнопку "Личный кабинет" в хедере, затем переходим в окно "Конструктор" через кнопку "Конструктор" в хедере, проверяем наличие надписи "Собери бургер" (ее текстовое содержимое)')
    @allure.story("Тестовый сценарий № 3")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_button_constructor_in_header_pass_to_constructor_menu(self, constructor_page):
        constructor_page.open_start_page()
        constructor_page.push_button_to_personal_account_on_header()
        constructor_page.wait_button_enter_of_window_entier_is_present()
        constructor_page.push_button_constructor_on_header()
        constructor_page.check_we_inside_constructor()

    @allure.title('3-2 Проверка перехода в окно "Лента заказов" кликом по кнопке "Лента заказов" в хедере')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», переходим в окно "Лента заказов" через кнопку "Лента заказов" в хедере, проверяем наличие надписи "Лента заказов" (ее текстовое содержимое)')
    @allure.story("Тестовый сценарий № 3")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_button_order_feed_in_header_pass_to_order_feed_menu(self, order_feed_page):
        order_feed_page.open_start_page()
        order_feed_page.push_button_to_order_feed_on_header()
        order_feed_page.check_we_inside_order_feed()

    @allure.title('3-3 Проверка появления всплывающего окна с деталями выбранного ингредиента')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», выбираем случайны ингредиент из списка и кликаем по нему, проверяем имя выбранного ингредиента в окне его свойств')
    @allure.story("Тестовый сценарий № 3")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_view_ingredient_info_by_clic_on_him_in_constructor_menu(self, constructor_page, random_ingredient=Generators.chose_random_ingredient()):
        constructor_page.open_start_page()
        constructor_page.click_on_element_ingredient_in_constructor_menu(ingredient=random_ingredient[0])
        constructor_page.check_chosen_ingredient_pop_up_window_by_name_of_ingredient(name_of_ingredient=random_ingredient[1])

    @allure.title('3-4 Проверка закрытия всплывающего окна с деталями выбранного ингредиента')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», выбираем случайны ингредиент из списка и кликаем по нему, нажимаем кнопку закрытия окна свойств ингредиента, проверяем, что окно свойств более не доступно')
    @allure.story("Тестовый сценарий № 3")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_close_property_of_ingredient_window_button_in_constructor_menu(self, constructor_page, random_ingredient=Generators.chose_random_ingredient()):
        constructor_page.open_start_page()
        constructor_page.click_on_element_ingredient_in_constructor_menu(ingredient=random_ingredient[0])
        constructor_page.click_on_close_property_of_ingredient_window_button_in_constructor_menu()
        constructor_page.check_chosen_ingredient_pop_up_window_is_not_available()
