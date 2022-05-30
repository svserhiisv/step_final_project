# -*- coding: utf-8 -*-
#

import random
import time

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


def test_guest_cant_see_success_message(browser):
    product_url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, product_url)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    product_url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, product_url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.basket_total_should_equal_to(page.product_price())
    page.some_add_notification_should_include(page.product_name())


@pytest.mark.skip
@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
                                  pytest.param(
                                      'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
                                      marks=pytest.mark.xfail),
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'])
def test_guest_can_add_product_to_basket_bug(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.basket_total_should_equal_to(page.product_price())
    page.some_add_notification_should_include(page.product_name())


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, product_url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, product_url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_items()
    basket_page.should_be_empty_message_shown()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_url = 'http://selenium1py.pythonanywhere.com/accounts/login/'

        rand_number = random.randint(1000000000, 10000000000)
        reg_email = f"test_user_{str(time.time())}_{rand_number}@stepik.email"
        reg_pwd = f"pw_{rand_number}"

        page = LoginPage(browser, login_url)
        page.open()
        page.register_new_user(reg_email, reg_pwd)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(browser, product_url)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(browser, product_url)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.basket_total_should_equal_to(page.product_price())
        page.some_add_notification_should_include(page.product_name())
