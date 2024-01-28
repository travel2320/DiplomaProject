from allure_commons._allure import step

from pages.base_page import BasePage


class WishlistPage(BasePage):

    URL = "https://www.primor.eu/pt_pt"

    LOGIN_PAGE_BUTTON_LOCATOR = "//div[@class='header__buttons']//a[contains(@href, 'account')]"
    CART_BUTTON_LOCATOR = "//div[@class='header__buttons']//a[contains(@href, 'cart')]"
    WISHLIST_BUTTON_LOCATOR = "//div[@class='header__buttons']//a[contains(@href, 'wishlist')]"

    ADD_NEW_WISHLIST_LOCATOR = "//a[contains(@class,'add-new-wishlist')]"
    WISHLIST_NAME_INPUT_LOCATOR = "//input[contains(@name,'new_wlname')]"
    CREATE_WISHLIST_BUTTON_LOCATOR = "//div[@data-role='focusable-scope']//button[@type='submit']"
    DELETE_WISHLIST_BUTTON_LOCATOR = "//a[@title='Apagar']"
    RENAME_WISHLIST_BUTTON_LOCATOR = "//a[@title='Rename']"
    RENAME_WISHLIST_INPUT_LOCATOR = "//input[@name='mWishlistName']"
    RENAME_WISHLIST_CONFIRM_BUTTON_LOCATOR = "//*[@id='rename-2']/form/div[2]/button"

    def navigate(self):
        with step("Opening url"):
            self.url_open(self.URL)

    def open_wishlist_page(self):
        with step("Opening wishlist page"):
            self.click(self.WISHLIST_BUTTON_LOCATOR)
            self.check_current_url(self.URL + "/wishlist")

    def create_new_wishlist(self, text):
        with step("Creating new wishlist"):
            self.wait_for_element_presence(self.ADD_NEW_WISHLIST_LOCATOR, 20)
            self.click(self.ADD_NEW_WISHLIST_LOCATOR)
            self.wait_for_element_presence(self.WISHLIST_NAME_INPUT_LOCATOR, 20)
            self.js_click(self.WISHLIST_NAME_INPUT_LOCATOR)
            self.send_text(self.WISHLIST_NAME_INPUT_LOCATOR, text)
            self.click(self.CREATE_WISHLIST_BUTTON_LOCATOR)

    def check_wishlist_created(self, text):
        with step("Checking wishlist created"):
            if self.wait_for_element_presence(f"//a[contains(text(),'{text}')]", 20):
                return True

    def delete_wishlist(self, text):
        with step("Deleting wishlist"):
            self.click(f"//a[contains(text(),'{text}')]")
            self.click(self.DELETE_WISHLIST_BUTTON_LOCATOR)
            return True

    def rename_wishlist(self, text):
        with step("Renaming wishlist"):
            self.click(f"//a[contains(text(),'{text}')]")
            self.wait_for_element_presence(self.RENAME_WISHLIST_BUTTON_LOCATOR, 20)
            self.click(self.RENAME_WISHLIST_BUTTON_LOCATOR)
            self.clear_element_text(self.RENAME_WISHLIST_INPUT_LOCATOR)
            self.send_text(self.RENAME_WISHLIST_INPUT_LOCATOR, text + "1")
            self.click(self.RENAME_WISHLIST_CONFIRM_BUTTON_LOCATOR)
            self.check_wishlist_created(text + "1")
            return True
