from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators as BPL
from data import const
import allure


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
        self.open_page(self.start_page)

    def find_and_focus_by_script(self, element):
        self.wait.until(EC.presence_of_element_located(element))
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*element))
        self.wait.until(EC.element_to_be_clickable(element))

    @allure.step("Находим и нажимаем на элемент {element}")
    def find_and_click(self, element):
        self.find_and_focus_by_script(element)
        self.driver.find_element(*element).click()

    @allure.step("Находим и нажимаем на элемент {element}")
    def find_and_click_by_script(self, element):
        self.wait.until(EC.presence_of_element_located(element))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*element))

    @allure.step("Находим текстовое поле {element} и вводим в него значение {data}")
    def entry_data_to_field(self, element, data):
        self.find_and_focus_by_script(element)
        self.driver.find_element(*element).send_keys(data)

    @allure.step("Возвращаем искомый элемент {element}")
    def get_element(self, element):
        self.find_and_focus_by_script(element)
        return self.driver.find_element(*element)