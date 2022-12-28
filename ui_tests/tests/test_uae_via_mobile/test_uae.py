import time

import allure
import pytest
from d14_ui_service_tests_templates.ui_tests.steps.login_steps import LoginSteps
from hamcrest import assert_that


from d14_base.data_reader import DataReader
from d14_ui_service_tests_templates.ui_tests.pages.common_page import CommonPage
from d14_ui_service_tests_templates.ui_tests.steps.uae_pass.device_steps_uae import DeviceStepsUAE
from d14_ui_service_tests_templates.ui_tests.steps.uae_pass.uae_pass_actions_web import UAEPassActionsWeb


class TestUaePass:
    """Test UAE Password."""

    @pytest.mark.skip(reason="Manual run: Test only for UAE pass and real device")
    def test_uae(self, prepare_device_uae_password):
        with allure.step("Click to user icon"):
            home_page = CommonPage()
            home_page.click_user_icon()

        with allure.step("Click to uae pass button"):
            LoginSteps.login_service_uae_pass(DataReader().get_test_data("UAEPassword.emirates_id"))

            DeviceStepsUAE.confirm(lambda: (
                UAEPassActionsWeb.click_login_uae(),
                UAEPassActionsWeb.wait_confirm_page()))

            time.sleep(100)  # noqa: TS100. Need for a captcha.

        with allure.step("Click to logged user icon"):
            home_page.click_logged_user_icon()

        with allure.step("Check the profile is present"):
            assert_that(home_page.is_profile_present(), "Profile label is absent")
