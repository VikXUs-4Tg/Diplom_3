import allure

from data import results
from helpers import Tools
from page_objects.base_page import BasePage
from locators.constructor_page_locators import ConstructorPageLocators as CPL


class ConstructorPage(BasePage):

    @allure.step("Ожидаем отображения элемента кнопки 'Войти' меню 'Вход', что бы убедится, что переход в другое меню был осуществлен")
    def wait_button_enter_of_window_entier_is_present(self):
        self.wait_of_element(element=CPL.MAIN_BUTTON)

    @allure.step("Находим и нажимаем на ингредиент c id={ingredient} в меню 'Конструктор'")
    def click_on_element_ingredient_in_constructor_menu(self, ingredient):
        locator_of_ingredient = (CPL.ELEMENT_INGREDIENT[0], Tools.replace_string_in_locator(locator=CPL.ELEMENT_INGREDIENT[1], string_to_replace="###", new_string=ingredient))
        self.find_and_click(element=locator_of_ingredient)

    @allure.step("Находим и нажимаем на кнопку закрытия окна свойств ингредиента")
    def click_on_close_property_of_ingredient_window_button_in_constructor_menu(self):
        parent = self.wait_of_element(element=CPL.SECTION_OF_INGREDIENT_PROPERTIES)
        self.find_in_parent(parent_of_element=parent, element=CPL.BUTTON_CLOSE_PROPERTIES_WINDOW).click()

    @allure.step("Проверяем наличие надписи 'Собери бургер' в меню 'Конструктор'")
    def check_we_inside_constructor(self):
        Tools.check_text_of_element(expected_value=results['CONSTRUCTOR_TITLE_INFO_TEXT'], actually_value=self.get_element(CPL.TITLE_ASSEMBLE_THE_BURGER).text)

    @allure.step("Проверяем появление всплывающего окна выбранного ингредиента (по отображаемому имени ингредиента)")
    def check_chosen_ingredient_pop_up_window_by_name_of_ingredient(self, name_of_ingredient):
        Tools.check_text_of_element(expected_value=name_of_ingredient, actually_value=self.get_element(CPL.INGREDIENT_NAME_IN_PROPERTIES).text)

    @allure.step("Проверяем, что всплывающее окно свойств выбранного ингредиента стало недоступным (по отображаемому имени ингредиента в всплывающем окне)")
    def check_chosen_ingredient_pop_up_window_is_not_available(self):
        self.check_not_present_of_element(CPL.INGREDIENT_NAME_IN_PROPERTIES)