from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a.btn-default')

class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_SUCCESS_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    MESSAGE_SUCCESS_ADD_TO_BASKET_TEXT = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    MESSAGE_BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_BASKET_TOTAL_PRICE_TEXT = (By.CSS_SELECTOR, ".alert-info strong")

class BasketPageLocators:
    PRODUCT_IN_BASKET= (By.CSS_SELECTOR, ".basket-items")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")

