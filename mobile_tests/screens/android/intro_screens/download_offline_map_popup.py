from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.intro_screens.download_offline_map_popup import BaseDownloadOfflineMapPopup


class DownloadOfflineMapPopup(BaseDownloadOfflineMapPopup):

    def __init__(self):
        super().__init__(MobileBy.ID, 'textViewDialogTitle')

    @property
    def _btn_cancel(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'buttonCancel', 'Cancel')
