from appium.webdriver.common.mobileby import MobileBy

from mobile_tests.screens.base.main_screens.updates_screens.updates_screen import BaseUpdatesScreen


class UpdatesScreen(BaseUpdatesScreen):

    def __init__(self):
        super().__init__(MobileBy.XPATH, '//XCUIElementTypeNavigationBar[@name="{}"]', 'Updates Screen.title')
