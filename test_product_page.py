import time

import pytest

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link_promo = LINK + "?promo=offer"

promo_offers = ['0', '1', '2','3', '4', '5', '6',
                pytest.param('7', marks=pytest.mark.xfail),
                '8', '9']


@pytest.mark.parametrize('promo_offer', promo_offers)
def test_guest_can_add_product_to_basket(driver, promo_offer):
    page = ProductPage(driver, link_promo+promo_offer)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_to_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    page = ProductPage(driver, LINK)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(driver):
    page = ProductPage(driver, LINK)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(driver):
    page = ProductPage(driver, LINK)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(driver):
    page = ProductPage(driver, LINK)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(driver):
    page = ProductPage(driver, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()