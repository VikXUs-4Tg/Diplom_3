import allure

from page_objects.base_page import BasePage
#from locators.main_page_locators import MainPageLocators as MPL
from data import const



class ConstructorPage(BasePage):

    def check_drop_down_lists(self):
        print()