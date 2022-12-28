from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.main_screens.locker_screens.locker_screen import BaseLockerScreen


class LockerScreen(BaseLockerScreen):

    def __init__(self):
        super().__init__(MobileBy.XPATH, "//*[contains(@resource-id, 'textViewTitle')][@text='{}']",
                         'Locker Screen.title')

    def _btn_item(self, key) -> MobileButton:
        return MobileButton(MobileBy.XPATH, '//*[contains(@resource-id, "textViewTitle")][@text="{}"]', key, key)
