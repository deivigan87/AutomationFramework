from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.screens.base_screen import BaseScreen


class FeedbackReceivedScreen(BaseScreen):

    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, '{}', "Feedback Received Screen.title")

    @property
    def _btn_ok(self) -> MobileButton:
        return MobileButton(MobileBy.ACCESSIBILITY_ID, '{}', 'Ok', "Feedback Received Screen.ok")

    def click_ok(self, ):
        self._btn_ok.tap()
