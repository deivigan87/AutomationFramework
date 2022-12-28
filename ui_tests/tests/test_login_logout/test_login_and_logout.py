import pytest
import allure
from hamcrest import assert_that

from d14_ui_service_tests_templates.ui_tests.pages.common_page import CommonPage
from d14_ui_service_tests_templates.ui_tests.steps.login_steps import LoginSteps

login = "persona.user65"
password = "P@ssword123"


class TestLoginLogout:
    """Test login and logout via smartpass: BUAH-2645"""

    @pytest.mark.smoke
    def test_login_and_logout(self):
        """Any info about test"""

        LoginSteps.login_service(login, password)

        with allure.step("Click to logged user icon"):
            home_page = CommonPage()
            home_page.click_logged_user_icon()

        with allure.step("Check the profile is present"):
            assert_that(home_page.is_profile_present(), "Profile label is absent")

        with allure.step("Click to logout button"):
            home_page.click_logout()

        with allure.step("Check the profile is not present"):
            home_page.wait_for_not_logged_user_icon_present()

        with allure.step("Click to user icon"):
            home_page = CommonPage()
            home_page.click_user_icon()

        with allure.step("Check the profile is not present"):
            assert_that(home_page.is_profile_absent(), "Profile label is present")
            assert_that(home_page.is_smart_pass_btn_present(), "Smartpass button is absent")
