import pytest
from allure import severity, feature, description, step, title, story


@feature("Account page")
@story("Account data functionality")
@severity("Critical")
class TestAccountPage:

    @title("Edit user info")
    @description("This test performs editing user profile info")
    @pytest.mark.usefixtures("setup")
    def test_edit_user_data(self, landing_page, login_page, account_page, first_name="HANNA", last_name="MAKAVETS"):
        with step("Performing edit user data"):
            with step("Performing login in account"):
                login_page.login("lisankaxxx@gmail.com", "Annamak#23")
            with step("Opening edit tab"):
                account_page.open_edit_tab()
            with step("Editing profile"):
                account_page.edit_profile(first_name, last_name)
        with step("Opening edit tab"):
            assert account_page.check_changes_saved(first_name, last_name), "Changes weren't saved"
