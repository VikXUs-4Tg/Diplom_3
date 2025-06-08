import pytest

from data import WEBPAGE, const
from helpers import RequestTools, Generators
from selenium import webdriver
from page_objects.constructor_page import ConstructorPage
from page_objects.personal_account_page import PersonalAccountPage

@pytest.fixture(scope='class', params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1920, 1080)
    elif request.param == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(options=firefox_options)
        driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

@pytest.fixture(scope='class')
def constructor_page(driver):
    constructor_page = ConstructorPage(driver=driver, wait_timer=const['WAIT_TIMER'], start_page=WEBPAGE)
    return constructor_page

@pytest.fixture(scope='class')
def personal_account_page(driver):
    personal_account_page = PersonalAccountPage(driver=driver, wait_timer=const['WAIT_TIMER'], start_page=WEBPAGE)
    return personal_account_page

@pytest.fixture(scope='function')
def random_user():
    user = Generators.generate_random_email()
    password = Generators.generate_random_password()
    random_user_api_data = {
        const['USER_EMAIL_PARAMETER_NAME']: user,
        const['USER_PASSWORD_PARAMETER_NAME']: password,
        const['USER_NAME_PARAMETER_NAME']: user[:user.find('@')]
    }
    RequestTools.try_to_register_new_user(user=random_user_api_data)
    yield user, password
    RequestTools.delete_user_after_test(user=random_user_api_data)

