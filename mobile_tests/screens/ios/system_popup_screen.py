from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.system_popup_screen import BaseSystemPopupScreen


class SystemPopUpScreen(BaseSystemPopupScreen):

    ACCEPT_VALUES = ['Allow', 'Accept']
    DECLINE_VALUES = ['Don’t Allow', 'Cancel']
    CONTINUE_VALUES = ['Continue', 'Continue']
    CANCEL_VALUES = ['Cancel', 'Cancel']

    def __init__(self):
        super().__init__(MobileBy.XPATH, '//XCUIElementTypeAlert')

    def _btn_system_button(self, value) -> MobileButton:
        return MobileButton(MobileBy.ACCESSIBILITY_ID, value, value)

    def accept(self):
        self._click_button(self.ACCEPT_VALUES)

    def decline(self):
        self._click_button(self.DECLINE_VALUES)

    def continue_action(self):
        self._click_button(self.CONTINUE_VALUES)

    def cancel_action(self):
        self._click_button(self.CANCEL_VALUES)
