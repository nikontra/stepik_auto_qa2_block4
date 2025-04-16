from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    """Класс для методов корзины"""
    def should_not_be_product_in_basket(self):
        """Проверяет отсутствие товара в корзине"""
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET) is True, "Items in the cart"

    def should_be_message_basket_is_empty(self):
        """Проверяет сообщение, что корзина пуста"""
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY) is True, "No text that the basket is empty"