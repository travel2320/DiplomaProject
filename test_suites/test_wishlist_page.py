import pytest
from allure import severity, feature, description, step, title, story


@feature("Wishlist page")
@story("Wishlist functionality")
@severity("Critical")
class TestWishlistPage:

    @title("Create a new wishlist")
    @description("This test creates new wishlist")
    @pytest.mark.usefixtures("setup")
    def test_create_wishlist(self, wishlist_page, login_page, landing_page, wishlist_name="testWL2"):
        with step("Performing "):
            with step("Performing login in account"):
                login_page.login("lisankaxxx@gmail.com", "Annamak#23")
            with step("Opening wishlist tab"):
                wishlist_page.open_wishlist_page()
            with step("Creating new wishlist"):
                wishlist_page.create_new_wishlist(wishlist_name)
        with step("Check wishlist was created"):
            assert wishlist_page.check_wishlist_created(wishlist_name), "Wishlist was not created"

    @title("Rename existing wishlist")
    @description("This test renames existing wishlist")
    @pytest.mark.usefixtures("setup")
    def test_rename_wishlist(self, wishlist_page, login_page, landing_page, wishlist_name="testWL2"):
        with step("Performing "):
            with step("Performing login in account"):
                login_page.login("lisankaxxx@gmail.com", "Annamak#23")
            with step("Opening wishlist tab"):
                wishlist_page.open_wishlist_page()
        with step("Check wishlist renamed successfully"):
            assert wishlist_page.rename_wishlist(wishlist_name), "wishlist wasn't renamed"

    @title("Delete wishlist")
    @description("This test ")
    @pytest.mark.usefixtures("setup")
    def test_delete_wishlist(self, wishlist_page, login_page, landing_page, wishlist_name="testWL21"):
        with step("Performing "):
            with step("Performing login in account"):
                login_page.login("lisankaxxx@gmail.com", "Annamak#23")
            with step("Opening wishlist tab"):
                wishlist_page.open_wishlist_page()
        with step("Check wishlist deleted successfully"):
            assert wishlist_page.delete_wishlist(wishlist_name), "Wishlist wasn't deleted"
