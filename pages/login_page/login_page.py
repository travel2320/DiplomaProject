from allure_commons._allure import step

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.primor.eu/es_es"

    EMAIL_INPUT_LOCATOR = "//input[@id='email']"
    PASSWORD_INPUT_LOCATOR = "//input[@id='password']"
    LOGIN_BUTTON_LOCATOR = "//button[@class='button account-form__button']"
    LOGIN_PAGE_BUTTON_LOCATOR = "//div[@class='header__buttons']//a[contains(@href, 'account')]"
    SIDEBAR_LOCATOR = "//div[@id='sidebar']"
    LOGOUT_BUTTON_LOCATOR = "//*[@id='sidebar']/div/div[3]/a"
    LOGIN_CRED_ERROR_LOCATOR = "//div[@data-ui-id='message-error']"
    LOGOUT_SUCCESS_LOCATOR = "//*[@id='maincontent']/h1"

    def navigate(self):
        with step("Opening url"):
            self.url_open(self.URL)

    def open_login_page(self):
        with step("Opening login page"):
            self.click(self.LOGIN_PAGE_BUTTON_LOCATOR)

    def check_invalid_cred_message_appeared(self):
        with step("Checking that invalid login credentials message appeared"):
            if self.wait_for_element_presence(self.LOGIN_CRED_ERROR_LOCATOR, 20):
                return True

    def check_login_successful(self):
        with step("Checking login successful"):
            if self.wait_for_element_presence(self.SIDEBAR_LOCATOR, 20):
                return True

    def check_logout_successful(self):
        with step("Checking logout successful"):
            if self.wait_for_element_presence(self.LOGOUT_SUCCESS_LOCATOR, 20):
                return True

    def logout(self):
        with step("Performing logout"):
            self.wait_for_element_presence(self.LOGOUT_BUTTON_LOCATOR, 20)
            self.scroll_down()
            self.js_click(self.LOGOUT_BUTTON_LOCATOR)

    def login(self, email, password):
        with step("Performing login"):
            self.open_login_page()
            self.send_text(self.EMAIL_INPUT_LOCATOR, email)
            self.send_text(self.PASSWORD_INPUT_LOCATOR, password)
            self.click(self.LOGIN_BUTTON_LOCATOR)
