from appium.webdriver.common.mobileby import MobileBy

from mobile_tests.screens.base.intro_screens.first_launch_screen import BaseFirstLaunchScreen


class FirstLaunchScreen(BaseFirstLaunchScreen):

    def __init__(self):
        super().__init__(MobileBy.ID, 'languageLayout')
