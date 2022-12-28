from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.intro_screens.intro_screen import BaseIntroScreen


class IntroScreen(BaseIntroScreen):

    def __init__(self):
        super().__init__(MobileBy.ID, 'skipButton')

    @property
    def _btn_skip(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'skipButton', 'Skip')
