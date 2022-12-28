from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.intro_screens.login_screen import BaseLoginScreen


class LoginScreen(BaseLoginScreen):

    def __init__(self):
        super().__init__(MobileBy.ID, 'loginLayout')

    @property
    def _btn_login_as_guest_user(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'buttonContinueAsGuest', 'Guest user')

    @property
    def _btn_smart_pass(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'smartPassLoginButton', 'Smart Pass')

    @property
    def _btn_uae_pass(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'uaePassLoginButton', 'UAE Pass')
