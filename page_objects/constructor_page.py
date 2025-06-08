import allure

from data import results
from helpers import Tools
from page_objects.base_page import BasePage
from locators.constructor_page_locators import ConstructorPageLocators as CPL
from selenium.common.exceptions import TimeoutException


class ConstructorPage(BasePage):

    @allure.step("Ожидаем отображения элемента кнопки 'Войти' меню 'Вход', что бы убедится, что переход в другое меню был осуществлен")
    def wait_button_enter_of_window_entier_is_present(self):
        self.wait_of_element(element=CPL.MAIN_BUTTON)

    @allure.step("Находим и нажимаем кнопку 'Оформить заказ' в меню 'Конструктор'")
    def click_button_to_make_order_in_constructor_menu(self):
        self.find_and_click_by_script(element=CPL.BUTTON_PLACE_AN_ORDER)

    @allure.step("Находим и нажимаем на ингредиент c id={ingredient} в меню 'Конструктор'")
    def click_on_element_ingredient_in_constructor_menu(self, ingredient):
        locator_of_ingredient = (CPL.ELEMENT_INGREDIENT[0], Tools.replace_string_in_locator(locator=CPL.ELEMENT_INGREDIENT[1], string_to_replace="###", new_string=ingredient))
        self.find_and_click_by_script(element=locator_of_ingredient)

    @allure.step("Находим и нажимаем на кнопку закрытия окна свойств ингредиента")
    def click_on_close_button_for_property_window_in_constructor_menu(self):
        parent = self.wait_of_element(element=CPL.SECTION_OF_CONSTRUCTOR_PROPERTIES)
        button_to_close = self.find_in_parent(parent_of_element=parent, element=CPL.BUTTON_CLOSE_PROPERTIES_WINDOW)
        self.click_by_script(element=button_to_close)

    @allure.step("Делаем заказ и получаем номер заказа")
    def make_order_and_return_identifier_number(self, burger):
        self.assemble_the_burger_to_basket(burger=burger)
        self.find_and_click_by_script(element=CPL.BUTTON_PLACE_AN_ORDER)
        try: self.wait_text_change_of_element(element=CPL.IDENTIFIER_OF_CREATED_ORDER,not_expected_text_value=results['UNEXPECTED_IDENTIFIER_VALUE'])
        except TimeoutException: pass
        identifier = self.get_element(CPL.IDENTIFIER_OF_CREATED_ORDER).text
        self.click_on_close_button_for_property_window_in_constructor_menu()
        return identifier

    @allure.step("Собираем в корзине бургер из ингредиентов ({burger})")
    def assemble_the_burger_to_basket(self, burger):
        for ingredient in burger:
            self.drag_and_drop_ingredient_in_basket(ingredient=ingredient)

    @allure.step("Добавляем ингредиент с id={ingredient} к заказу")
    def drag_and_drop_ingredient_in_basket(self, ingredient):
        locator_of_ingredient = (CPL.ELEMENT_INGREDIENT[0], Tools.replace_string_in_locator(locator=CPL.ELEMENT_INGREDIENT[1], string_to_replace="###", new_string=ingredient))
        web_element_ingredient = self.wait_of_element(element=locator_of_ingredient)
        web_element_basket = self.wait_of_element(element=CPL.BASKET_OF_BURGER_CONSTRUCTOR)
        self.drag_and_drop_element(element=web_element_ingredient,destination=web_element_basket)

    @allure.step("Проверяем наличие надписи 'Собери бургер' в меню 'Конструктор'")
    def check_we_inside_constructor(self):
        Tools.check_text_of_element(expected_value=results['CONSTRUCTOR_TITLE_INFO_TEXT'], actually_value=self.get_element(CPL.TITLE_ASSEMBLE_THE_BURGER).text)

    @allure.step("Проверяем появление всплывающего окна выбранного ингредиента (по отображаемому имени ингредиента)")
    def check_chosen_ingredient_pop_up_window_by_name_of_ingredient(self, name_of_ingredient):
        Tools.check_text_of_element(expected_value=name_of_ingredient, actually_value=self.get_element(CPL.INGREDIENT_NAME_IN_PROPERTIES).text)

    @allure.step("Проверяем, что всплывающее окно свойств выбранного ингредиента стало недоступным (по отображаемому имени ингредиента в всплывающем окне)")
    def check_chosen_ingredient_pop_up_window_is_not_available(self):
        self.check_not_present_of_element(CPL.INGREDIENT_NAME_IN_PROPERTIES)

    @allure.step("Проверяем что значение счетчика добавленного ингредиента с id={ingredient} больше 0")
    def check_that_counter_of_ingredient_not_zero(self, ingredient):
        locator_of_ingredient = (CPL.ELEMENT_INGREDIENT[0], Tools.replace_string_in_locator(locator=CPL.ELEMENT_INGREDIENT[1], string_to_replace="###", new_string=ingredient))
        parent = self.get_element(element=locator_of_ingredient)
        counter_value = self.find_in_parent(parent_of_element=parent, element=CPL.COUNTER_OF_INGREDIENT).text
        Tools.check_that_value_differs_from_not_expected_value(not_expected_value=results['UNEXPECTED_COUNTER_VALUE'], actually_value=counter_value)

    @allure.step("Проверяем, что заказ будет оформлен (ожидаем появления номера заказа)")
    def check_created_order_get_identifier(self):
        try: self.wait_text_change_of_element(element=CPL.IDENTIFIER_OF_CREATED_ORDER,not_expected_text_value=results['UNEXPECTED_IDENTIFIER_VALUE'])
        except TimeoutException: pass
        Tools.check_that_value_differs_from_not_expected_value(not_expected_value=results['UNEXPECTED_IDENTIFIER_VALUE'], actually_value=self.get_element(CPL.IDENTIFIER_OF_CREATED_ORDER).text)