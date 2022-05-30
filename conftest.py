# -*- coding: utf-8 -*-
#

import os
import logging
import pytest
import time

from datetime import datetime
from selenium import webdriver

from selenium.webdriver.chrome.options import Options


logging.basicConfig(filename='./svsimon.log', level=logging.INFO, format="%(asctime)s [%(levelname)s] [%(module)s:%(lineno)d] [%(name)s]: %(message)s")


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Please choose localization language')
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser').lower()
    if browser_name == 'chrome':
        logging.debug('start chrome browser for test..')
        locale = request.config.getoption('language')
        logging.debug(f"`{locale}` locale selected")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"--lang={locale}")
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': locale})
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == 'firefox':
        logging.debug('start firefox browser for test..')
        browser = webdriver.Firefox()
    else:
        raise NotImplemented("Browser {} still is not implemented".format(browser_name))

    yield browser

    logging.debug('quit browser...')
    browser.quit()


@pytest.fixture(scope='function')
def browser_with_screenshots(request):
    browser_name = request.config.getoption('browser')
    if browser_name == 'chrome':
        print('\nstart chrome browser for test..')
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        print('\nstart firefox browser for test..')
        browser = webdriver.Firefox()
    else:
        print("Browser {} still is not implemented".format(browser_name))

    yield browser

    print('\nquit browser...')
    # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
    browser.save_screenshot("screenshot-%s.png" % now)
    browser.quit()