import pytest
from allure import severity, feature, description, step, title, story


@feature("Cart page")
@story("Cart functionality")
@severity("Critical")
class TestCartPage:

    @title("Add item to cart and check item added")
    @description("This test adds item to cart and checks that item added")
    @pytest.mark.usefixtures("setup")
    def test_add_item_to_cart(self, login_page, landing_page, cart_page, item_name="Trussardi"):
        with step("Performing login in account and adding item to cart"):
            landing_page.handle_popup_with_retry()
            login_page.login("lisankaxxx@gmail.com", "Annamak#23")
            landing_page.open_landing_page()
            landing_page.perform_item_search(item_name.capitalize())
        with step("Opening cart page"):
            cart_page.open_cart_page()
        with step("Check cart is not empty"):
            cart_page.check_cart_is_not_empty()
        with step("Check proper item were added to cart"):
            cart_page.check_item_in_cart_name(item_name)
            with step("Proceeding to checkout"):
                cart_page.proceed_to_checkout()
        with step("Checking checkout page is opened"):
            assert cart_page.check_checkout_page_appeared(), "Expected checkout page to appear"

    @title("Use coupon")
    @description("This test applies coupon to cart item")
    @pytest.mark.usefixtures("setup")
    def test_use_coupon(self, login_page, landing_page, cart_page, coupon="testcoupon"):
        with step("Performing login in account and adding item to cart"):
            login_page.login("lisankaxxx@gmail.com", "Annamak#23")
        with step("Opening cart page"):
            cart_page.open_cart_page()
        with step("Input coupon"):
            cart_page.input_coupon(coupon)
        with step("Checking coupon status"):
            assert cart_page.check_coupon_status(coupon), "Expected to have a coupon status displayed"

    @title("Delete item from cart")
    @description("This test deletes item from cart")
    @pytest.mark.usefixtures("setup")
    def test_delete_item_from_cart(self, login_page, landing_page, cart_page):
        with step("Performing login in account and adding item to cart"):
            login_page.login("lisankaxxx@gmail.com", "Annamak#23")
        with step("Opening cart page"):
            cart_page.open_cart_page()
        with step("Checking cart is not empty"):
            cart_page.check_cart_is_not_empty()
        assert cart_page.delete_item_form_cart(), "Item is not deleted"
