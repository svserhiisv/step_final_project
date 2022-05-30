# -*- coding: utf-8 -*-
#

import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_URL_MARKER in self.browser.current_url, \
            f"`{LoginPageLocators.LOGIN_URL_MARKER}` should be included in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'

    def register_new_user(self, email, password):
        logging.debug(f"Registering `{email}` with `{password}`")

        WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable(LoginPageLocators.REG_EMAIL))

        email_input = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_input.send_keys(email)

        pwd1_input = self.browser.find_element(*LoginPageLocators.REG_PWD1)
        pwd1_input.send_keys(password)

        pwd2_input = self.browser.find_element(*LoginPageLocators.REG_PWD2)
        pwd2_input.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REG_SUBMIT)
        register_button.click()
