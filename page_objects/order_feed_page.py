import allure

from data import results
from helpers import Tools
from page_objects.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators as OFPL


class OrderFeedPage(BasePage):

    @allure.step("Находим и нажимаем на необходимый заказ (№ {order_identifier}) в меню 'Лента заказов'")
    def click_on_order_in_order_feed(self, order_identifier):
        locator_of_order = (OFPL.SOME_ORDERS_IN_FEED[0], Tools.replace_string_in_locator(locator=OFPL.SOME_ORDERS_IN_FEED[1], string_to_replace="###", new_string=order_identifier))
        self.find_and_click_by_script(element=locator_of_order)

    @allure.step("Находим и возвращаем значение счетчика выполненных заказов в меню 'Лента заказов'")
    def get_counter_value(self, counter):
        locator_of_counter = (OFPL.COUNTER_BY_NEIGHBOUR[0], Tools.replace_string_in_locator(locator=OFPL.COUNTER_BY_NEIGHBOUR[1], string_to_replace="###", new_string=counter))
        return self.get_element(element=locator_of_counter).text

    @allure.step("Проверяем наличие надписи 'Лента заказов' в меню 'Лента заказов'")
    def check_we_inside_order_feed(self):
        Tools.check_text_of_element(expected_value=results['ORDER_FEED_TITLE_INFO_TEXT'], actually_value=self.get_element(OFPL.TITLE_ORDER_FEED).text)

    @allure.step("Проверяем на соответствие номер заказа в окне детализации по заказу (№ {order_identifier}) в меню 'Лента заказов'")
    def check_order_number_in_details_window_inside_order_feed(self, order_identifier):
        Tools.check_text_of_element(expected_value=order_identifier, actually_value=self.get_element(OFPL.ORDER_NUMBER_IN_DETAILS_WINDOW).text)

    @allure.step("Проверяем на соответствие номер заказа в окне детализации по заказу (№ {order_identifier}) в меню 'Лента заказов'")
    def check_order_number_in_details_window_inside_order_feed(self, order_identifier):
        Tools.check_text_of_element(expected_value=order_identifier, actually_value=self.get_element(OFPL.ORDER_NUMBER_IN_DETAILS_WINDOW).text)
