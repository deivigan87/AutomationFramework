import allure
import pytest
from hamcrest import assert_that

from d14_ui_service_tests_templates.ui_tests.pages.tamm_portal.services_page import ServicesPage

from d14_ui_framework.browser.browser import Browser
from d14_ui_service_tests_templates.ui_tests.steps.login_steps import LoginSteps
from ui_tests.pages.tamm_portal.portal import Portal

user_identifier = "784198732046960"


class TestLoginUAEPass:
    """Test login and logout via uaepass: BUAH-2645"""

    @pytest.mark.smoke
    def test_login_uae_pass(self):
        """Any info about test"""
        LoginSteps.login_service_uae_pass(user_identifier, required_login_page=True)

        """
        Example without required_login_page
        Browser.set_url("https://stage.tamm.abudhabi/en")
        LoginSteps.login_service_uae_pass(user_identifier)
        """

        if Browser.get_url() == "https://stage.tamm.abudhabi/en":
            with allure.step("Open 1st service"):
                portal_page = Portal()
                portal_page.click_1st_apply_btn()

            with allure.step("Check that service is opened"):
                service_page = ServicesPage()
                assert_that(service_page.is_table_present(), "Table is not present")
        else:
            with allure.step("Check that service is opened"):
                service_page = ServicesPage()
                assert_that(service_page.is_service_table_present(), "Table is not present")
