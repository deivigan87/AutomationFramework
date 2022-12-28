from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.checkbox import MobileCheckBox
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.summary_screen \
    import BaseSummaryScreen


class SummaryScreen(BaseSummaryScreen):

    def __init__(self):
        super().__init__(MobileBy.ID, 'tutorialItemDescription')

    @property
    def _chb_accept_term_and_conditions(self) -> MobileCheckBox:
        return MobileCheckBox(MobileBy.XPATH, '//android.widget.CheckBox', "Accept terms and conditions")

    @property
    def _btn_submit(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'submitSelectedPackages', 'Submit')
