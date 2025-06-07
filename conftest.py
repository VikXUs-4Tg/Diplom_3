import pytest

from data import WEBPAGE, const
from selenium import webdriver
from page_objects.constructor_page import ConstructorPage
from page_objects.personal_account_page import PersonalAccountPage

@pytest.fixture(scope='class', params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1920, 1080)
    elif request.param == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        #firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(options=firefox_options)
        driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

@pytest.fixture(scope='class')
def constructor_page(driver):
    constructor_page = ConstructorPage(driver=driver, wait_timer=const['WAIT_TIMER'], start_page=WEBPAGE)
    constructor_page.open_start_page()
    return constructor_page

@pytest.fixture(scope='class')
def personal_account_page(driver):
    personal_account_page = PersonalAccountPage(driver=driver, wait_timer=const['WAIT_TIMER'], start_page=WEBPAGE)
    personal_account_page.open_start_page()
    return personal_account_page
