from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.intro_screens.quick_tip_popup import BaseQuickTipPopup


class QuickTipPopup(BaseQuickTipPopup):

    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, "okButton_unselected", "Quick tip pop up.quick_tip")

    @property
    def _btn_ok(self) -> MobileButton:
        return MobileButton(MobileBy.ACCESSIBILITY_ID, "okButton_unselected", 'Ok', "Quick tip pop up.ok")
