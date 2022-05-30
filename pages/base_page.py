# -*- coding: utf-8 -*-
#

import logging
import math

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage():
    BROWSE_STORE_NAMES = {'en-gb': 'Browse store',
                          'es': 'Explorar la tienda'}

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket(self):
        button = self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON)
        button.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print('No second alert presented')

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def open_all_products(self):
        browse_store_menu_item = self.browser.find_element(*BasePageLocators.BROWSE_STORE)
        browse_store_menu_item.click()

        all_products_menu_item = self.browser.find_element(*BasePageLocators.ALL_PRODUCTS_MENU_ITEM)
        all_products_menu_item.click()

    def should_be_in_catalogue(self):
        current_url = self.browser.current_url.rstrip('/')
        logging.debug(f"current_url={current_url}")
        assert current_url.split('/')[-1] == 'catalogue', f"Catalogue page url expected, but got `{current_url}` instead"

    def should_more_than_n_product_cards_be_visible(self, n):
        product_cards = self.browser.find_elements(*BasePageLocators.PRODUCT_CARDS)
        visible_cards = list(filter(lambda x: x.is_displayed(), product_cards))
        assert len(visible_cards) > n, f"More than {n} product cards should be visible, but only {len(visible_cards)} currently visible now"

    def search(self, search_query):
        search_input = self.browser.find_element(*BasePageLocators.SEARCH_FIELD)
        search_input.send_keys(search_query)

        find_button = self.browser.find_element(*BasePageLocators.SEARCH_BUTTON)
        find_button.click()

    def should_url_include(self, substring):
        logging.debug(f"current_url={self.browser.current_url}")
        assert substring in self.browser.current_url, f"current url should include `{substring}` but got `{self.browser.current_url}` instead"

    def change_language(self, lang):
        lang_selector = Select(self.browser.find_element(*BasePageLocators.LANG_DROPDOWN))
        lang_selector.select_by_value(lang)
        change_language_button = self.browser.find_element(*BasePageLocators.CHANGE_LANG_BUTTON)
        change_language_button.click()

    def get_browse_store_name(self):
        return self.browser.find_element(*BasePageLocators.BROWSE_STORE).text

    def should_browse_store_name_equal_to(self, string):
        current_name = self.get_browse_store_name()
        assert current_name == string, \
        f"Browse store menu text should be equal to `{string}`, but got `{current_name}` instead"

    def language_should_be(self, lang):
        self.should_url_include(f"/{lang}/")
        self.should_browse_store_name_equal_to(self.BROWSE_STORE_NAMES[lang])