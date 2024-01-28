from allure_commons._allure import step

from pages.base_page import BasePage


class AccountPage(BasePage):

    URL = "https://www.primor.eu/es_es"

    EDIT_PROFILE_LOCATOR = "//div[@id='sidebar']//a[contains(@href,'edit')]"
    FIRST_NAME_LOCATOR = "//input[@id='firstname']"
    LAST_NAME_LOCATOR = "//input[@id='lastname']"
    GENDER_DROPDOWN_LOCATOR = "//select[@id='gender']"
    FEMALE_GENDER_SELECT_LOCATOR = "//select[@id='gender']/option[contains(text(),'Fem')]"
    SAVE_CHANGES_BUTTON_LOCATOR = "//button[@title='Guardar']"

    def navigate(self):
        with step("Opening url"):
            self.url_open(self.URL)

    def open_edit_tab(self):
        with step("Opening edit tab"):
            self.click(self.EDIT_PROFILE_LOCATOR)

    def edit_last_name(self, last_name):
        with step("Editing last name"):
            self.wait_for_element_presence(self.LAST_NAME_LOCATOR, 20)
            self.clear_element_text(self.LAST_NAME_LOCATOR)
            self.send_text(self.LAST_NAME_LOCATOR, last_name)

    def edit_first_name(self, first_name):
        with step("Editing first name"):
            self.wait_for_element_presence(self.FIRST_NAME_LOCATOR, 20)
            self.clear_element_text(self.FIRST_NAME_LOCATOR)
            self.send_text(self.FIRST_NAME_LOCATOR, first_name)

    def edit_gender_to_female(self):
        with step("Changing user gender field to female"):
            self.wait_for_element_presence(self.GENDER_DROPDOWN_LOCATOR, 20)
            self.click(self.GENDER_DROPDOWN_LOCATOR)
            self.wait_for_element_presence(self.FEMALE_GENDER_SELECT_LOCATOR, 20)
            self.click(self.FEMALE_GENDER_SELECT_LOCATOR)

    def edit_profile(self, first_name, last_name):
        with step("Editing profile"):
            self.edit_first_name(first_name)
            self.edit_last_name(last_name)
            self.edit_gender_to_female()
            self.click(self.SAVE_CHANGES_BUTTON_LOCATOR)

    def check_changes_saved(self, first_name, last_name):
        with step("Checking changes saved"):
            self.open_edit_tab()
            if first_name in self.get_element_value(self.FIRST_NAME_LOCATOR) \
                    and last_name in self.get_element_value(self.LAST_NAME_LOCATOR):
                return True
