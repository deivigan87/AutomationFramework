from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.text_field import MobileTextbox
from mobile_tests.screens.base.intro_screens.login_uae_pass_page_screen import BaseLoginUAEPassPageScreen


class LoginUAEPassPageScreen(BaseLoginUAEPassPageScreen):

    def __init__(self):
        super().__init__(MobileBy.XPATH, "//XCUIElementTypeOther[@name='UAE PASS']")

    @property
    def _btn_uae_pass_test_user(self) -> MobileTextbox:
        return MobileTextbox(MobileBy.XPATH, "(//XCUIElementTypeLink[@name='urn:StressTest'])[1]", "Username")

    @property
    def _txb_emirates_id(self) -> MobileTextbox:
        return MobileTextbox(MobileBy.XPATH,
                             "//XCUIElementTypeOther[@name='UAE PASS']/XCUIElementTypeTextField", "Emirates ID")

    @property
    def _btn_sign_in(self) -> MobileButton:
        return MobileButton(MobileBy.ACCESSIBILITY_ID, 'Login', "Login")
