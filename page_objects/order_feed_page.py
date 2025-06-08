import allure

from data import results
from helpers import Tools
from page_objects.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators as OFPL


class OrderFeedPage(BasePage):

    @allure.step("Проверяем наличие надписи 'Лента заказов' в меню 'Лента заказов'")
    def check_we_inside_order_feed(self):
        Tools.check_text_of_element(expected_value=results['ORDER_FEED_TITLE_INFO_TEXT'], actually_value=self.get_element(OFPL.TITLE_ORDER_FEED).text)