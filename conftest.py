import pytest

from data import WEBPAGE, const
from selenium import webdriver
from page_objects.constructor_page import ConstructorPage
#from page_objects.make_order_page import MakeOrderPage

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

@pytest.fixture(scope='function')
def constructor_page(driver):
    constructor_page = ConstructorPage(driver=driver, wait_timer=const['WAIT_TIMER'], start_page=WEBPAGE)
    constructor_page.open_start_page()
    return constructor_page


"""
@pytest.fixture(scope='function')
def make_order_page(driver):
    make_order_page = MakeOrderPage(driver=driver, wait_timer=const['WAIT_TIMER'], start_page=const['WEBPAGE'])
    make_order_page.open_start_page()
    return make_order_page
    
"""