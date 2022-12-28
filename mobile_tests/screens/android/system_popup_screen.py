from appium.webdriver.common.mobileby import MobileBy
from d14_mobile_framework.framework.elements.button import MobileButton

from mobile_tests.screens.base.system_popup_screen import BaseSystemPopupScreen


class SystemPopUpScreen(BaseSystemPopupScreen):
    ACCEPT_VALUES = ['//*[contains(@resource-id, "permission_allow_button")]']
    DECLINE_VALUES = ['//*[contains(@resource-id, "permission_deny_button")]']
    CONTINUE_VALUES = ['//*[contains(@resource-id, "permission_continue_button")]']
    CANCEL_VALUES = ['//*[contains(@resource-id, "permission_cancel_button")]']

    def __init__(self):
        super().__init__(MobileBy.XPATH, '//*[contains(@resource-id, "content_container") or '
                                         'contains(@resource-id, "desc_container")]')

    def _btn_system_button(self, value) -> MobileButton:
        return MobileButton(MobileBy.XPATH, value)

    def accept(self):
        self.wait_for_is_opened()
        self._click_button(self.ACCEPT_VALUES)

    def decline(self):
        self._click_button(self.DECLINE_VALUES)

    def continue_action(self):
        self._click_button(self.CONTINUE_VALUES)

    def cancel_action(self):
        self._click_button(self.CANCEL_VALUES)
