from appium.webdriver.common.mobileby import MobileBy
from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.intro_screens.meet_home_pop_up_screen import BaseMeetHomePopUpScreen


class MeetHomePopUpScreen(BaseMeetHomePopUpScreen):

    def __init__(self):
        super().__init__(MobileBy.ID, 'abudhabi.tamm.stage:id/img_onboarding')

    @property
    def _btn_close(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'abudhabi.tamm.stage:id/img_cross', 'Close')
