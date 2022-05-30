# -*- coding: utf-8 -*-
#

from selenium.webdriver.common.by import By


class MainPageLocators():
    def __init__(self, *args, **kwargs):
        super(MainPageLocators, self).__init__(*args, **kwargs)


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini .btn-group a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')
    BROWSE_STORE = (By.CSS_SELECTOR, '.dropdown.active.open .dropdown-toggle')
    ALL_PRODUCTS_MENU_ITEM = (By.CSS_SELECTOR, '.dropdown.active.open .dropdown-menu li:nth-child(1) > a')
    PRODUCT_CARDS = (By.CSS_SELECTOR, '.product_pod')
    SEARCH_FIELD = (By.CSS_SELECTOR, "[type='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.navbar-right .btn-default')
    LANG_DROPDOWN = (By.CSS_SELECTOR, "[name='language']")
    CHANGE_LANG_BUTTON = (By.CSS_SELECTOR, '#language_selector .btn-default')


class BasketPageLocators():
    BASKET_CONTENT = (By.CSS_SELECTOR, '#content_inner')
    BASKET_ITEMS = (By.CSS_SELECTOR, '#basket-items')
    EMPTY_BASKET_MESSAGE = 'Your basket is empty.'


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_URL_MARKER = 'login'
    REG_EMAIL = (By.ID, 'id_registration-email')
    REG_PWD1 = (By.ID, 'id_registration-password1')
    REG_PWD2 = (By.ID, 'id_registration-password2')
    REG_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')
    BASKET_SUM = (By.CSS_SELECTOR, '.basket-mini')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    # STRONG_NOFIFICATION = (By.CSS_SELECTOR, '.alert-success .alertinner strong')
    NOTIFICATION = (By.CSS_SELECTOR, '.alert-success .alertinner')
    PRODUCT_ADDED_MESSAGE = 'has been added to your basket.'
    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-child(1)')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
