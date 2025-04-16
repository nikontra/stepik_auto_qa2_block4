from selenium.webdriver.common.by import By


class BasePageLocators:
    """Класс локаторов общих для всех страниц"""
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class MainPageLocators:
    """Класс локаторов для главной страницы"""
    pass


class LoginPageLocators:
    """Класс локаторов для страницы авторизации"""
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '.form-group input[name="registration-email"]')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '.form-group input[name="registration-password1"]')
    REGISTRATION_CONFIRM = (By.CSS_SELECTOR, '.form-group input[name="registration-password2"]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    """Класс локаторов для страницы продукта"""
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_SUCCESS_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    MESSAGE_SUCCESS_ADD_TO_BASKET_TEXT = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    MESSAGE_BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_BASKET_TOTAL_PRICE_TEXT = (By.CSS_SELECTOR, ".alert-info strong")


class BasketPageLocators:
    """Класс локаторов для страницы корзины"""
    PRODUCT_IN_BASKET= (By.CSS_SELECTOR, ".basket-items")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")

