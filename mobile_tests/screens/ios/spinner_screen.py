from appium.webdriver.common.mobileby import MobileBy

from mobile_tests.screens.base.spinner_screen import BaseSpinnerScreen


class SpinnerScreen(BaseSpinnerScreen):

    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, 'activity.indicator.inprogress.label')
