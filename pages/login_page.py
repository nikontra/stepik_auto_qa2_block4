from selenium.webdriver import Keys

from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    """Класс для методов страницы авторизации"""
    def should_be_login_page(self):
        """Проверяет страницу авторизации"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверяет наличие слова "login" в адресе страницы"""
        assert "login" in self.driver.current_url, "Login not in url"

    def should_be_login_form(self):
        """Проверяет наличие формы авторизации"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        """Проверяет наличие формы регистрации"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        """Регистрирует нового пользователя"""
        self.driver.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.driver.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.driver.find_element(*LoginPageLocators.REGISTRATION_CONFIRM).send_keys(password)
        self.driver.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()