import pytest
from allure import severity, feature, description, step, title, story


@feature("Login page")
@story("Login functionality")
@severity("Critical")
class TestLoginPage:

    @title("User login with valid credentials")
    @description("This test performs login into account with valid credentials")
    @pytest.mark.usefixtures("setup")
    def test_login_successful(self, login_page, landing_page):
        with step("Performing login in account"):
            login_page.login("lisankaxxx@gmail.com", "Annamak#23")
        with step("Checking login was successful"):
            assert login_page.check_login_successful(), "Login was not successful"

    @title("User login with invalid credentials")
    @description("This test performs login into account with invalid credentials")
    @pytest.mark.usefixtures("setup")
    def test_login_not_successful(self, login_page, landing_page):
        with step("Performing login in account with invalid credentials"):
            login_page.login("1lisankaxxx@gmail.com", "1Annamak#23")
        with step("Checking login was not successful"):
            assert login_page.check_invalid_cred_message_appeared(), "Expected login error message"

    @title("User logout")
    @description("This test performs logout from account")
    @pytest.mark.usefixtures("setup")
    def test_logout(self, login_page, landing_page):
        with step("Performing login-logout flow"):
            with step("Loging in account"):
                login_page.login("lisankaxxx@gmail.com", "Annamak#23")
            with step("Loging out of account"):
                login_page.logout()
        with step("Check logout completed"):
            assert login_page.check_logout_successful(), "Expected successful logout message"
