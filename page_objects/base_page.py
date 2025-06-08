import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators as BPL


class BasePage:

    def __init__(self, driver, wait_timer, start_page):
        self.driver = driver
        self.wait_timer = wait_timer
        self.start_page = start_page
        self.wait = WDW(self.driver, wait_timer)

    @allure.step("Открываем страницу {page}")
    def open_page(self, page):
        self.driver.get(page)
        self.wait.until(EC.url_contains(page))

    def open_start_page(self):
        self.open_page(page=self.start_page)

    def find_and_focus_by_script(self, element):
        self.wait.until(EC.presence_of_element_located(element))
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*element))
        self.wait.until(EC.element_to_be_clickable(element))

    def find_and_click_by_script(self, element):
        self.find_and_focus_by_script(element=element)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*element))

    def find_and_click(self, element):
        self.find_and_focus_by_script(element=element)
        self.driver.find_element(*element).click()

    def find_equal_elements(self, elements):
        self.find_and_focus_by_script(element=elements)
        return self.driver.find_elements(*elements)

    def entry_data_to_field(self, element, data):
        self.find_and_focus_by_script(element=element)
        self.driver.find_element(*element).send_keys(data)

    def get_element(self, element):
        self.find_and_focus_by_script(element=element)
        return self.driver.find_element(*element)

    def wait_of_element(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def check_present_of_element(self, locator):
        try: self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException as e:
            assert False, f"\nОжидаемое значение:\n'Элемент присутствует и виден'\nФактическое значение:\nЭлемент не найден или не стал видимым в течение заданного времени ожидания"

    @allure.step("Находим и нажимаем на логотип 'Stellar Burgers' в хедере страницы")
    def push_logo_on_header(self):
        self.find_and_click_by_script(element=BPL.LOGO)

    @allure.step("Находим и нажимаем на кнопку 'Конструктор' в хедере страницы")
    def push_button_constructor_on_header(self):
        self.find_and_click_by_script(element=BPL.BUTTON_TO_CONSTRUCTOR)

    @allure.step("Находим и нажимаем на кнопку 'Лента Заказов' в хедере страницы")
    def push_button_to_order_feed_on_header(self):
        self.find_and_click_by_script(element=BPL.BUTTON_TO_ORDER_FEED)

    @allure.step("Находим и нажимаем на кнопку 'Личный кабинет' в хедере страницы")
    def push_button_to_personal_account_on_header(self):
        self.find_and_click_by_script(element=BPL.BUTTON_TO_PERSONAL_ACCOUNT)


    