from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.text_field import MobileTextbox
from mobile_tests.screens.base.intro_screens.login_smart_pass_page_screen import BaseLoginSmartPassPageScreen


class LoginSmartPassPageScreen(BaseLoginSmartPassPageScreen):

    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, "{}", "Login Page Screen.username")

    @property
    def _txb_username(self) -> MobileTextbox:
        return MobileTextbox(MobileBy.ACCESSIBILITY_ID, "{}", "Username", "Login Page Screen.username")

    @property
    def _txb_password(self) -> MobileTextbox:
        return MobileTextbox(MobileBy.ACCESSIBILITY_ID, "{}", "Password", "Login Page Screen.password")

    @property
    def _btn_sign_in(self) -> MobileButton:
        return MobileButton(MobileBy.XPATH, '(//XCUIElementTypeButton[@name="{}"])[1]',
                            "Login", "Login Page Screen.login")
