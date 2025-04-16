import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage:
    """Тесты для кнопки авторизации на главной странице"""
    def test_guest_should_see_login_link(self, driver):
        """Проверяет наличие кнопки авторизации при открытии
        главной страницы неавторизованным пользователем"""
        page = MainPage(driver, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, driver):
        """Проверяет переход на страницу авторизации с главной страницы неавторизованным пользователем"""
        page = MainPage(driver, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(driver, driver.current_url)
        login_page.should_be_login_page()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    """Проверяет переход на страницу корзины с главной страницы неавторизованным пользователем"""
    page = MainPage(driver, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_message_basket_is_empty()






