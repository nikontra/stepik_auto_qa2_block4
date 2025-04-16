import json
from termios import CRDLY

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose the browser to run tests on')
    parser.addoption('--language', action='store', default='en',)


@pytest.fixture
def driver(request):
    """Фикстура для открытия браузера"""
    browser_name = request.config.getoption('--browser_name')
    language = request.config.getoption('--language')
    options_chrome = ChromeOptions()
    options_chrome.add_experimental_option('prefs', {'intl.accept_languages': language})
    option_firefox = FirefoxOptions()
    option_firefox.set_preference('intl.accept_languages', language)

    if browser_name == 'chrome':
        print("\nstart browser chrome for test")
        driver = webdriver.Chrome(options=options_chrome)
    elif browser_name == 'firefox':
        print("\nstart browser firefox for test")
        driver = webdriver.Firefox(options=option_firefox)
    else:
        raise ValueError("Browser name must be either 'chrome' or 'firefox'")
    yield driver
    driver.quit()
    print("\nend browser for test")

@pytest.fixture(scope="session")
def load_config():
    """Фикстура для файла конфигурации"""
    with open("config.json", "r") as f:
        config = json.load(f)
        return config