from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.text_field import MobileTextbox
from mobile_tests.screens.base.intro_screens.login_uae_pass_page_screen import BaseLoginUAEPassPageScreen


class LoginUAEPassPageScreen(BaseLoginUAEPassPageScreen):

    def __init__(self):
        super().__init__(MobileBy.XPATH, "//*[@resource-id='flowSelectorForm']")

    @property
    def _btn_uae_pass_test_user(self) -> MobileTextbox:
        return MobileTextbox(MobileBy.XPATH, "//*[@resource-id='urn:StressTest']", "Username")

    @property
    def _txb_emirates_id(self) -> MobileTextbox:
        return MobileTextbox(MobileBy.XPATH, "//*[@resource-id='userIdentifier']", "Username")

    @property
    def _btn_sign_in(self) -> MobileButton:
        return MobileButton(MobileBy.XPATH, "//*[@resource-id='basicPasswordForm-submitButton']", "Login")
