import math

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    """Класс для базовых методов"""
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(10)


    def open(self):
        """Открывает страницу"""
        self.driver.get(self.url)

    def go_to_login_page(self):
        """Нажимает на кнопку авторизации"""
        login_link = self.driver.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basket_page(self):
        """Нажимает на кнопку корзины"""
        basket_link = self.driver.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def should_be_login_link(self):
        """Проверяет наличие кнопки авторизации"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not present."

    def is_element_present(self, how, what):
        """Проверяет, что элемент появляется на странице"""
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """Проверяет, что элемент не появляется на странице в течение заданного времени"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
            return False
        except TimeoutException:
            return True

    def is_disappeared(self, how, what, timeout=4):
        """Проверяет, что элемент исчезает"""
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
            return True
        except TimeoutException:
            return False

    def solve_quiz_and_get_code(self):
        """Вычисляет значение по формуле и подставляет в окно алерта"""
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_authorized_user(self):
        """Проверяет наличие значка авторизованного пользователя"""
        assert self.is_element_present(
            *BasePageLocators.USER_ICON), "User icon is not present, probably unauthorised user."

