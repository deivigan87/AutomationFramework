import allure
from pytest_bdd import when, parsers

from d14_ui_service_tests_templates.ui_tests.pages.smart_pass.smart_pass_page import SmartPassPage


@when(parsers.parse("I set '{login}' login and '{password}' password"))
def set_login_and_password(login, password):
    with allure.step("Set username and password"):
        smartpass_page = SmartPassPage()
        smartpass_page.send_username(login)
        smartpass_page.send_password(password)


@when("I click login button")
def click_login_button():
    with allure.step("Click login button"):
        SmartPassPage().click_login()
