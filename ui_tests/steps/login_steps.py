import re

import allure
from allure_commons.model2 import TestResult

from d14_ui_framework.constants import browsers
from d14_ui_framework.elements.base.element_state import ElementState

from d14_base.data_reader import DataReader

from d14_ui_framework.browser.browser import Browser

from d14_base.html_allure_report_listener import AllureListener
from d14_base.string_util import StringUtil
from d14_ui_framework.pages.base_page import BasePage
from d14_ui_service_tests_templates.ui_tests.pages.common_page import CommonPage
from d14_ui_service_tests_templates.ui_tests.pages.smart_pass.smart_pass_page import SmartPassPage
from ui_tests.pages.login_required_page import LoginRequiredPage
from ui_tests.pages.uae_pass.uae_pass_page import UaePassPage


class LoginSteps(BasePage):
    """Login Steps"""

    @staticmethod
    def login_service(login, password):
        with allure.step("Click to user icon"):
            common_page = CommonPage()
            common_page.click_user_icon()

        with allure.step("Click to smart pass button"):
            common_page.click_smart_pass()

        with allure.step("Send login and password"):
            smart_pass_page = SmartPassPage()
            smart_pass_page.send_username(login)
            smart_pass_page.send_password(password)

        with allure.step("Send data about user to a report"):
            LoginSteps.post_smartpass_user_info_to_report(login, password)

        with allure.step("Click to login button"):
            smart_pass_page.click_login()

    @staticmethod
    def login_service_uae_pass(identifier, required_login_page=False):
        """
        Login from UAE pass button without sending notification to mobile phone on STG env.
        :param identifier: str: unique of identifier of user: Emirates ID.
        :param required_login_page: bool: condition if test opens page where need to login via Uae pass button:
        Example of page: https://www.screencast.com/t/snrwiilzj
        """
        with allure.step("Click to user icon"):
            common_page = CommonPage()
            common_page.wait_page_to_load()
            common_page.click_user_icon()

        with allure.step("Check that Login Required page is opened"):
            if required_login_page:
                LoginSteps.get_and_set_url_uae_pass_login_required_page()
            else:
                LoginSteps.get_and_set_url_uae_pass()

        with allure.step("Send Email/Mobile number/Emirates ID"):
            uae_pass_page = UaePassPage()
            uae_pass_page.send_user_info(identifier)

        with allure.step("Send data about user to a report"):
            LoginSteps.post_uae_user_info_to_report(identifier)

        with allure.step("Click to login button"):
            uae_pass_page.click_login()

        with allure.step("Click to submit button"):
            uae_pass_page.click_submit()

    @staticmethod
    def get_and_set_url_uae_pass():
        """Get current URL of page and Set specific URL to a browser for login via UAE pass from the header button."""
        with allure.step("Get current URL"):
            current_url = Browser.get_url()

        with allure.step("Set UAE PASS redirection URL to browser"):
            LoginSteps.set_url_uae_pass(current_url)

    @staticmethod
    def get_and_set_url_uae_pass_login_required_page():
        """Get current URL of page and Set specific URL to a browser for login via UAE pass from the Required Login
        page."""
        LoginRequiredPage().uae_pass_btn.wait_for_element_state(ElementState.VISIBLE)
        with allure.step("Get current URL"):
            current_url = Browser.get_url()
            regex_current_url = re.compile("redirectUrl=(.*)")

        with allure.step("Set UAE PASS redirection URL to browser"):
            LoginSteps.set_url_uae_pass(regex_current_url.findall(current_url)[0])

    @staticmethod
    def set_url_uae_pass(current_url):
        """
        Set specific URL to a browser for login to STG env via UAE pass without sending request to Mobile device.

        :param current_url: str: current URL of page where need too login.
        """
        with allure.step("Set UAE PASS redirection URL to browser"):
            Browser.set_url("https://{}.tamm.abudhabi/searchresults/api/smartpass/"
                            "login?provider=uaepass&redirectUrl={}".format('stage' if DataReader().
                                                                           get_env() == "qa_stg" else "www",
                                                                           current_url) + '&testClient=1')
            if Browser.get_platform_name() == browsers.BROWSER_SAFARI:
                Browser.set_url("https://{}.tamm.abudhabi/searchresults/api/smartpass/"
                                "login?provider=uaepass&redirectUrl={}".format('stage' if DataReader().
                                                                               get_env() == "qa_stg" else "www",
                                                                               current_url) + '&testClient=1')

    @staticmethod
    def post_smartpass_user_info_to_report(username, password):
        """
        Method for sending info about smartpass user to a report.
        Method should bу called in your methods after login (look at example LoginSteps.login_service(login, password)).

        Username: str: User name.
        Password: str: Password.
        """
        if AllureListener.get_allure_listener():
            test_result = AllureListener.get_allure_listener().get_last_item(TestResult)
            test_result.name = StringUtil.get_method_name_for_allure_report(test_result.name)
            if test_result.description is None:
                test_result.description = \
                    "Logged user information:<br/>User name: {}, User password: {}".format(username, password)
            else:
                test_result.description += "<br/><br/>Logged user information:<br/>User name: {}, User password: {}".\
                    format(username, password)

    @staticmethod
    def post_uae_user_info_to_report(user_identifier):
        """
        Method for sending info about uae user to a report.
        Method should bу called in your methods after login (look at example LoginSteps.login_service_uae_pass(login,
        password)).

        User identifier: str: User identifier.
        """
        if AllureListener.get_allure_listener():
            test_result = AllureListener.get_allure_listener().get_last_item(TestResult)
            test_result.name = StringUtil.get_method_name_for_allure_report(test_result.name)
            if test_result.description is None:
                test_result.description = \
                    "Logged user information:<br/>User identifier: {}".format(user_identifier)
            else:
                test_result.description += "<br/><br/>Logged user information:<br/>User identifier: {}".\
                    format(user_identifier)
