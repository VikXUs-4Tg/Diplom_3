import allure

from data import WEBPAGE


class TestSuit1:
    @allure.title('Проверка ответов на "Вопросы о важном"')
    @allure.description('На главной странице ищет веб элемент содержащий искомый "вопрос", нажимает на него и проверяет "ответ" в открывающимся снизу под ним окне (дочернем элементе)')
    @allure.story("Тестовый сценарий № 1")
    @allure.link(WEBPAGE, name='Учебный сервиса «Яндекс.Самокат» (стенд)')
    def test_drop_down_lists(self, constructor_page):
        constructor_page.open_start_page()

