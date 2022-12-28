from abc import ABC, abstractmethod

from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.text_field import MobileTextbox
from d14_mobile_framework.framework.screens.base_screen import BaseScreen


class BaseFeedbackScreen(ABC, BaseScreen):

    def __init__(self, locator_type: MobileBy, locator: str, locale: str = None):
        super().__init__(locator_type, locator, locale)

    @property
    @abstractmethod
    def _btn_happy(self) -> MobileButton:
        pass

    @property
    @abstractmethod
    def _btn_sad(self) -> MobileButton:
        pass

    @property
    @abstractmethod
    def _btn_normal(self) -> MobileButton:
        pass

    @property
    @abstractmethod
    def _btn_submit(self) -> MobileButton:
        pass

    @property
    @abstractmethod
    def _txb_comment(self) -> MobileTextbox:
        pass

    class FeedbackLevel:
        HAPPY = "Happy"
        NORMAL = "Normal"
        SAD = "Sad"

    def leave_feedback(self, level: FeedbackLevel, comment: str = None):
        if level == self.FeedbackLevel.HAPPY:
            self._btn_happy.tap()
        elif level == self.FeedbackLevel.NORMAL:
            self._btn_normal.tap()
        else:
            self._btn_sad.tap()
        if comment:
            self._txb_comment.set_text(comment)
        self._btn_submit.tap()
