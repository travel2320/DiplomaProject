import pytest
from allure import severity, feature, description, step, title, story


@feature("Landing page")
@story("Search functionality")
@severity("Critical")
class TestLandingPage:

    @title("Add item to cart")
    @description("This test performs flow of adding an item to cart")
    @pytest.mark.usefixtures("setup")
    def test_item_search(self, landing_page, cart_page):
        with step("Performing item search and add to cart"):
            landing_page.perform_item_search("TRUSSARDI")
        with step("Checking item were added to cart"):
            assert landing_page.check_item_added_to_cart(), "Expected item to be added to cart"
            with step("Clearing cart after tests"):
                cart_page.open_cart_page()
                cart_page.delete_item_form_cart()

    @title("Choose category")
    @description("This test chooses category on landing page")
    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("number, expected_value", [("1", "marcas"), ("6", "produtos-cabelo"), ("7", "tratamentos-corporais")])
    def test_choose_category(self, landing_page, number, expected_value):
        with step("Performing category chose"):
            current_url = landing_page.open_category(number)
        with step("Checking url is proper for chosen category"):
            assert expected_value in current_url, f"Expected {expected_value} to be in {current_url}"
