from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    # Основные элементы:
    TITLE_ORDER_FEED =                  (By.XPATH, "//h1[@class='text text_type_main-large mt-10 mb-5']")
    SOME_ORDERS_IN_FEED =               (By.XPATH, "//p[contains(text(), '###')]")
    ORDER_NUMBER_IN_DETAILS_WINDOW =    (By.XPATH, "//p[@class='text text_type_digits-default mb-10 mt-5']")
    COUNTER_BY_NEIGHBOUR =              (By.XPATH, "//p[contains(text(), '###')]/following-sibling::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    ORDERS_IN_WORK =                    (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")
