import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.landing_page.landing_page import LandingPage
from pages.login_page.login_page import LoginPage
from pages.wishlist_page.wishlist_page import WishlistPage
from pages.cart_page.cart_page import CartPage
from pages.account_page.account_page import AccountPage

# driver setups


@pytest.fixture
def set_driver():
    browser = "chrome"
    # browser = "firefox"
    # browser = "safari"

    # headless = True
    headless = False

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-popup-blocking")


        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()

    elif browser == "safari":
        if headless:
            raise ValueError("Safari does not support headless mode")
        driver = webdriver.Safari()

    else:
        raise ValueError("Unsupported browser")

    yield driver
    driver.quit()

@pytest.fixture()
def landing_page(set_driver):
    return LandingPage(set_driver)


@pytest.fixture()
def login_page(set_driver):
    return LoginPage(set_driver)


@pytest.fixture()
def wishlist_page(set_driver):
    return WishlistPage(set_driver)


@pytest.fixture()
def cart_page(set_driver):
    return CartPage(set_driver)


@pytest.fixture()
def account_page(set_driver):
    return AccountPage(set_driver)

# setup


@pytest.fixture()
def setup(set_driver, landing_page):
    landing_page.navigate()
    landing_page.handle_popup_with_retry()
