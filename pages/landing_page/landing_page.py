from allure_commons._allure import step

from pages.base_page import BasePage
import time


class LandingPage(BasePage):

    URL = "https://www.primor.eu/es_es"

    MENU_CATEGORY_LOCATOR = "//nav[@id='mega-menu']/ul/li"

    LANDING_PAGE_LOCATOR = "//a[@aria-label='Home page link']"
    CONFIRM_REDIRECT_BUTTON = "//button[@id='destinoButton']"
    LOGIN_PAGE_BUTTON_LOCATOR = "//div[@class='header__buttons']//a[contains(@href, 'account')]"
    CART_BUTTON_LOCATOR = "//div[@class='header__buttons']//a[contains(@href, 'cart')]"
    WISHLIST_BUTTON_LOCATOR = "//div[@class='header__buttons']//a[contains(@href, 'wishlist')]"
    SEARCHBAR_LOCATOR = "//input[@id='search-doofinder']"
    SEARCH_BUTTON_LOCATOR = "//button[@data-testid='search-link']"
    ADD_TO_CART_BUTTON_LOCATOR = "//button[@id='product-addtocart-button']"
    SWATCH_OPTION_50_LOCATOR = "//div[contains(text(),'50ML')]"
    SWATCH_OPTION_100_LOCATOR = "//div[contains(text(),'100ML')]"
    QUANTITY_PLUS_BUTTON_LOCATOR = "//button[@data-testid='quantity-plus-button']"
    QUANTITY_MINUS_BUTTON_LOCATOR = "//button[@data-testid='quantity-minus-button']"
    QUANTITY_LOCATOR = "//*[@id='qty']"

    ACCEPT_COOKIES_BUTTON_LOCATOR = "//button[@data-amgdprcookie-js='accept']"
    SUCCESS_ITEM_ADDED_LOCATOR = "//div[@data-ui-id='message-success']"
    COOKIES_SUCCESS_LOCATOR = "//div[@data-ui-id='message-success']"
    COOKIES_POPUP_LOCATOR = "//*[@id='html-body']/div[7]/aside[5]/div/div"
    REDIRECT_POPUP_LOCATOR = "//*[@id='html-body']/div[7]/aside[2]/div/div"

    def navigate(self):
        with step("Opening url"):
            self.url_open(self.URL)

    def handle_popup_with_retry(self, max_retries=3, delay=2):
        with step("Handling popup and cookies"):
            retries = 0
            while retries < max_retries:
                try:
                    self.wait_for_page_loaded()
                    self.wait_for_element_presence(self.COOKIES_POPUP_LOCATOR, 5)
                    self.wait_for_element_presence(self.REDIRECT_POPUP_LOCATOR, 5)
                    self.wait_for_element_presence(self.CONFIRM_REDIRECT_BUTTON, 5)
                    self.wait_for_element_presence(self.ACCEPT_COOKIES_BUTTON_LOCATOR, 5)
                    self.js_click(self.ACCEPT_COOKIES_BUTTON_LOCATOR)
                    self.click(self.CONFIRM_REDIRECT_BUTTON)
                    self.wait_for_element_presence(self.COOKIES_SUCCESS_LOCATOR, 5)
                    self.refresh_page()
                    break

                except:
                    retries += 1
                    time.sleep(delay)
                    self.refresh_page()
            if retries == max_retries:
                pass

    def open_landing_page(self):
        with step("Opening login page"):
            self.click(self.LANDING_PAGE_LOCATOR)
            self.wait_for_page_loaded()

    def search_for_an_item_by_brand(self, brand_name):
        with step("Searching for an item by brand name"):
            self.send_text(self.SEARCHBAR_LOCATOR, brand_name)
            self.click(self.SEARCH_BUTTON_LOCATOR)

    def choose_item(self):
        with step("Choosing item from list"):
            SEARCH_TARGET_LOCATOR = "//*[@id='products-list']/div[2]/div"

            self.wait_for_element_presence(SEARCH_TARGET_LOCATOR, 20)
            self.click(SEARCH_TARGET_LOCATOR)

    def choose_volume(self):
        with step("Choosing item volume"):
            self.click(self.SWATCH_OPTION_50_LOCATOR)
            self.click(self.SWATCH_OPTION_100_LOCATOR)

    def choose_quantity(self, value):
        with step("Choosing item quantity"):
            i = 1
            while i != value:
                self.click(self.QUANTITY_PLUS_BUTTON_LOCATOR)
                i += 1

    def add_item_to_card(self):
        with step("Adding item to cart"):
            self.click(self.ADD_TO_CART_BUTTON_LOCATOR)

    def perform_item_search(self, brand_name):
        with step("Performing item search"):
            self.search_for_an_item_by_brand(brand_name)
            self.choose_item()
            self.choose_volume()
            self.choose_quantity(5)
            self.add_item_to_card()

    def check_item_added_to_cart(self):
        with step("Checking item were added to cart"):
            if self.wait_for_element_presence(self.SUCCESS_ITEM_ADDED_LOCATOR, 20):
                return True

    def open_category(self, number):
        with step("Opening category"):
            self.wait_for_element_presence(self.MENU_CATEGORY_LOCATOR + f'[{number}]', 10).click()
            self.wait_for_page_loaded()
            return self.get_current_url()
