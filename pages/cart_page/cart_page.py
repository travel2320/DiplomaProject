from allure_commons._allure import step

from pages.base_page import BasePage


class CartPage(BasePage):
    URL = "https://www.primor.eu/es_es"

    CART_PAGE_BUTTON_LOCATOR = "//div[@class='header__buttons']//a[contains(@href, 'cart')]"

    COUPON_INPUT_LOCATOR = "//input[@id='coupon_code']"
    APPLY_COUPON_BUTTON_LOCATOR = "//button[@title='Apply coupon']"
    PROCEED_TO_CHECKOUT_LOCATOR = "//button[@data-role='proceed-to-checkout']"
    ITEM_IN_CART_LOCATOR = "//div[@class='cart-list-item ']"
    ITEM_IN_CART_NAME_LOCATOR = "//div[@class='cart-list-item ']/div/div/div"
    DELETE_ITEM_FROM_CART_LOCATOR = "//a[@title='Remover item']"

    def navigate(self):
        with step("Opening url"):
            self.url_open(self.URL)

    def open_cart_page(self):
        with step("Opening cart page"):
            self.click(self.CART_PAGE_BUTTON_LOCATOR)

    def check_coupon_status(self, status):
        with step("Checking coupon status"):
            self.wait_for_element_presence(f"//div[@data-role='checkout-messages']//*[contains(text(),'{status}')]", 10)

    def input_coupon(self, coupon):
        with step("Inputting coupon"):
            self.click(self.COUPON_INPUT_LOCATOR)
            self.send_text(self.COUPON_INPUT_LOCATOR, coupon)
            self.click(self.APPLY_COUPON_BUTTON_LOCATOR)

    def proceed_to_checkout(self):
        with step("Proceeding to checkout"):
            self.click(self.PROCEED_TO_CHECKOUT_LOCATOR)

    def check_checkout_page_appeared(self):
        with step("Checking checkout page loaded"):
            if "checkout" in self.get_current_url():
                return True

    def check_cart_is_not_empty(self):
        with step("Checking cart is not empty"):
            self.wait_for_element_presence(self.ITEM_IN_CART_LOCATOR, 10)

    def check_item_in_cart_name(self, expected_name):
        with step("Checking item in cart have proper name"):
            if expected_name in self.get_element_text(self.ITEM_IN_CART_NAME_LOCATOR):
                return True

    def delete_item_form_cart(self):
        with step("Deleting item from cart"):
            self.click(self.DELETE_ITEM_FROM_CART_LOCATOR)
            self.refresh_page()
            return True
