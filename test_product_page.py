import time

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

from .pages.product_page import ProductPage

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link_promo = LINK + "?promo=offer"
LINK_LOGIN = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

promo_offers = ['0', '1', '2','3', '4', '5', '6',
                pytest.param('7', marks=pytest.mark.xfail),
                '8', '9']


@pytest.mark.parametrize('promo_offer', promo_offers)
def test_guest_can_add_product_to_basket(driver, promo_offer):
    """Проверяет добавление товара в корзину неавторизованным пользователем"""
    page = ProductPage(driver, link_promo+promo_offer)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_to_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    """Проверяет отсутствие сообщения об успешном добавлении товара в корзину
    при добавлении товара в корзину неавторизованным пользователем"""
    page = ProductPage(driver, LINK)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(driver):
    """Проверяет отсутствие сообщения об успешном добавлении товара в корзину
    при открытии страницы товара неавторизованным пользователем"""
    page = ProductPage(driver, LINK)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(driver):
    """Проверяет исчезновение сообщения об успешном добавлении товара в корзину
    при добавлении товара в корзину неавторизованным пользователем"""
    page = ProductPage(driver, LINK)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(driver):
    """Проверяет наличие кнопки авторизации при открытии
    страницы товара неавторизованным пользователем"""
    page = ProductPage(driver, LINK)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(driver):
    """Проверяет переход на страницу авторизации со страницы товара неавторизованным пользователем"""
    page = ProductPage(driver, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    """Проверяет переход на страницу корзины со страницы товара неавторизованным пользователем"""
    page = ProductPage(driver, LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_message_basket_is_empty()


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage:
    """Тесты для авторизованного пользователя"""
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        """Фикстура для регистрации и авторизации пользователя"""
        page = LoginPage(driver, LINK_LOGIN)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "fakepassword"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, driver):
        """Проверяет добавление товара в корзину авторизованным пользователем"""
        page = ProductPage(driver, LINK)
        page.open()
        page.add_product_to_basket()
        page.should_be_add_to_basket()

    def test_user_cant_see_success_message(self, driver):
        """Проверяет отсутствие сообщения об успешном добавлении товара в корзину
        при открытии страницы товара авторизованным пользователем"""
        page = ProductPage(driver, LINK)
        page.open()
        page.should_not_be_success_message()

