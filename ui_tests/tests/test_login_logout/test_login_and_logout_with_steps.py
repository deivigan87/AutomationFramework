import pytest

from d14_ui_framework.elements.base.element_state import ElementState
import ui_tests.steps.home_page_steps as home_page_steps
import ui_tests.steps.smartpass_steps as smartpass_steps

login = "persona.user65"
password = "P@ssword123"


class TestLoginLogout:
    """Test login and logout via smartpass: BUAH-2645"""

    @pytest.mark.smoke
    def test_login_and_logout(self):
        home_page_steps.click_user_icon()
        home_page_steps.click_smartpass_button()
        smartpass_steps.set_login_and_password(login, password)
        smartpass_steps.click_login_button()
        home_page_steps.click_logged_user_icon()
        home_page_steps.assert_profile_button_is_in_state(ElementState.EXISTS)
        home_page_steps.click_logout_button()
        home_page_steps.assert_guest_user_icon_is_present()
        home_page_steps.click_user_icon()
        home_page_steps.assert_profile_button_is_in_state(ElementState.ABSENT)
        home_page_steps.assert_smartpass_button_is_in_state(ElementState.ABSENT)
