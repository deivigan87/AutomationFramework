import allure
from hamcrest import assert_that, not_
from pytest_bdd import when, then, parsers

from d14_ui_framework.elements.base.element_state import ElementState
from ui_tests.pages.common_page import CommonPage


@when("I click user icon")
def click_user_icon():
    with allure.step("Click user icon"):
        CommonPage().click_user_icon()


@when("I click SmartPass button")
def click_smartpass_button():
    with allure.step("Click SmartPass button"):
        CommonPage().click_smart_pass()


@when("I click logged user icon")
def click_logged_user_icon():
    with allure.step("Click logged user icon"):
        CommonPage().click_logged_user_icon()


@then(parsers.re("Profile icon is (?P<state>present|absent)"))
def assert_profile_button_is_in_state(state):
    with allure.step(f"Check if profile icon is in {state} state"):
        if state.lower() == ElementState.EXISTS.lower() or state.lower() == "present":
            assert_that(CommonPage().is_profile_present(), "Profile label is absent")
        else:
            assert_that(not_(CommonPage().is_profile_present()), "Profile label is present")


@when("I click logout button")
def click_logout_button():
    with allure.step("Click logout"):
        CommonPage().click_logout()


@then("Guest user icon is present")
def assert_guest_user_icon_is_present():
    with allure.step("Check if guest user icon is present"):
        CommonPage().wait_for_not_logged_user_icon_present()


@then(parsers.re("SmartPass button is (?P<state>present|absent)"))
def assert_smartpass_button_is_in_state(state):
    with allure.step(f"Check if SmartPass button is in {state} state"):
        if state.lower() == ElementState.EXISTS.lower() or state.lower() == "present":
            assert_that(CommonPage().is_smart_pass_btn_present(), "Smartpass button is absent")
        else:
            assert_that(not_(CommonPage().is_smart_pass_btn_present()), "Smartpass button is absent")
