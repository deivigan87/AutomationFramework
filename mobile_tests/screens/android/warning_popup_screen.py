from appium.webdriver.common.mobileby import MobileBy
from d14_mobile_framework.framework.elements.button import MobileButton

from mobile_tests.screens.base.warning_popup_screen import BaseWarningPopupScreen


class WarningPopupScreen(BaseWarningPopupScreen):
    OK = ['//*[contains(@resource-id, "buttonOk")]']
    CANCEL = ['//*[contains(@resource-id, "buttonCancel")]']

    def __init__(self):
        super().__init__(MobileBy.XPATH, '//*[contains(@resource-id, "extViewDialogTitle")]')

    def _btn_system_button(self, value) -> MobileButton:
        return MobileButton(MobileBy.XPATH, value)

    def ok(self):
        self.wait_for_is_opened()
        self._click_button(self.OK)

    def cancel(self):
        self._click_button(self.CANCEL)
