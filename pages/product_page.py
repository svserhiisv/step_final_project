# -*- coding: utf-8 -*-
#

import logging

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return price

    def product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return name

    def basket_total_should_equal_to(self, expected_sum):
        total = self.browser.find_element(*ProductPageLocators.BASKET_SUM)
        total_text = total.text.split()
        logging.debug(f"total.text: {total.text}")
        logging.debug(f"total_text_splitted: {total_text}")
        total_sum = total_text[2]
        assert total_sum == expected_sum, f"{expected_sum} expected as basket total, but {total_sum} in fact"

    def some_add_notification_should_include(self, expected_name):
        item_added_message_found = False
        all_notifications = self.browser.find_elements(*ProductPageLocators.NOTIFICATION)
        expected_notification = f"{expected_name} {ProductPageLocators.PRODUCT_ADDED_MESSAGE}"
        for notification in all_notifications:
            logging.debug(f"notification: {notification.text}")
            if notification.text == expected_notification:
                item_added_message_found = True
        assert item_added_message_found, f"Some of notifications should be equal to `{expected_notification}`, but none found"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
