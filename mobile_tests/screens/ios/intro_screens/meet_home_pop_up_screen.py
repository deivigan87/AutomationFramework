from appium.webdriver.common.mobileby import MobileBy
from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.intro_screens.meet_home_pop_up_screen import BaseMeetHomePopUpScreen


class MeetHomePopUpScreen(BaseMeetHomePopUpScreen):

    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, 'headLbl')

    @property
    def _btn_close(self) -> MobileButton:
        return MobileButton(MobileBy.ACCESSIBILITY_ID, 'dismissBtn_unselected', 'Cancel')
