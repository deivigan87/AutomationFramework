from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.intro_screens.login_screen import BaseLoginScreen


class LoginScreen(BaseLoginScreen):

    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, '{}', 'Login Screen.select_language')

    @property
    def _btn_login_as_guest_user(self) -> MobileButton:
        return MobileButton(MobileBy.ACCESSIBILITY_ID, 'continueAsGuestButton_unselected', 'Continue As Guest')

    @property
    def _btn_smart_pass(self) -> MobileButton:
        return MobileButton(MobileBy.ACCESSIBILITY_ID, 'LoginOrRegisterBtn_unselected', 'Smart pass')

    @property
    def _btn_uae_pass(self) -> MobileButton:
        return MobileButton(MobileBy.ACCESSIBILITY_ID, 'UAEBtn_unselected', 'UAE pass')
