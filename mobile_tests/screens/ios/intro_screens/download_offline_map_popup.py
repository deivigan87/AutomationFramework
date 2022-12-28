from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.intro_screens.download_offline_map_popup import BaseDownloadOfflineMapPopup
from mobile_tests.screens.ios.spinner_screen import SpinnerScreen


class DownloadOfflineMapPopup(BaseDownloadOfflineMapPopup):

    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, '{}', 'Download Offline Map Screen.download_offline_map')

    @property
    def _btn_cancel(self) -> MobileButton:
        return MobileButton(MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="{}"]', 'Cancel',
                            'Download Offline Map Screen.cancel')

    def cancel(self):
        self.wait_for_is_opened()
        SpinnerScreen().wait_for_is_closed()
        self._btn_cancel.tap_via_coordinates()
