# -*- coding: utf-8 -*-
#

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        self.should_be_no_items()
        self.should_be_empty_message_shown()

    def should_be_empty_message_shown(self):
        basket_content = self.browser.find_element(*BasketPageLocators.BASKET_CONTENT)
        assert BasketPageLocators.EMPTY_BASKET_MESSAGE in basket_content.text

    def should_be_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            'Some items are in basket, but should not be'
