# -*- coding: utf-8 -*-
#

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_items()
    basket_page.should_be_empty_message_shown()


@pytest.mark.need_review_custom_scenarios
def test_guest_can_see_all_goods(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()

    page.open_all_products()
    page.should_be_in_catalogue()
    page.should_more_than_n_product_cards_be_visible(5)


@pytest.mark.need_review_custom_scenarios
def test_guest_can_search_goods(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()

    search_query = 'books'
    page.search(search_query)
    page.should_url_include(search_query)
    page.should_more_than_n_product_cards_be_visible(5)


@pytest.mark.need_review_custom_scenarios
def test_guest_can_change_language(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()

    current_browse_store_name = page.get_browse_store_name()
    lang = 'en'
    page.change_language(lang)
    page.language_should_be(lang)
