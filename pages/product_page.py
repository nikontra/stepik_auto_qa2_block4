from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        """Добавляет товар в корзину"""
        self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def should_be_add_to_basket(self):
        """Проверяет страницу товара после добавления в корзину"""
        self.should_be_message_success_add_to_basket()
        self.should_be_message_basket_total_price()

    def should_be_message_success_add_to_basket(self):
        """Проверяет наличие сообщения об успешном добавлении товара в корзину"""
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_SUCCESS_ADD_TO_BASKET) is True, "Message success not in present"
        name_product = self.driver.find_element(*ProductPageLocators.NAME_PRODUCT).text
        assert name_product == self.driver.find_element(
            *ProductPageLocators.MESSAGE_SUCCESS_ADD_TO_BASKET_TEXT).text, "Name product not in message success"

    def should_be_message_basket_total_price(self):
        """Проверяет наличие сообщения об общей стоимости корзины"""
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_BASKET_TOTAL_PRICE) is True, "Message basket total price not in present"
        price = self.driver.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price == self.driver.find_element(
            *ProductPageLocators.MESSAGE_BASKET_TOTAL_PRICE_TEXT).text, "Price product not in message basket total price"

    def should_not_be_success_message(self):
        """Проверяет, что сообщение о добавлении товара в корзину не появилось"""
        assert self.is_not_element_present(
            *ProductPageLocators.MESSAGE_SUCCESS_ADD_TO_BASKET) is True, "Success message is present, but should be"

    def should_disappear_success_message(self):
        """Проверяет, что сообщение о добавлении товара в корзину исчезло"""
        assert self.is_disappeared(
            *ProductPageLocators.MESSAGE_SUCCESS_ADD_TO_BASKET) is True, "Success message is disappeared"
