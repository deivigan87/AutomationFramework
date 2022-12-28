from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.intro_screens.tutorial_screen import BaseTutorialScreen


class TutorialScreen(BaseTutorialScreen):

    def __init__(self):
        super().__init__(MobileBy.ID, 'tutorialItemDescription')

    @property
    def _btn_skip(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'skipTutorialButton', 'Skip')
