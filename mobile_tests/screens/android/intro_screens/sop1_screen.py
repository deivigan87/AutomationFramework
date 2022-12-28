from appium.webdriver.common.mobileby import MobileBy
from d14_mobile_framework.framework.elements.button import MobileButton

from mobile_tests.screens.base.intro_screens.sop1_screen import BaseSOP1Screen


class Sop1Screen(BaseSOP1Screen):

    def __init__(self):
        super().__init__(MobileBy.ID, 'abudhabi.tamm.stage:id/btnFindKiosk')

    @property
    def _btn_cancel(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'abudhabi.tamm.stage:id/cancelButton', 'Cancel')
