from abc import ABC, abstractmethod

from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.checkbox import MobileCheckBox
from d14_mobile_framework.framework.screens.base_screen import BaseScreen


class BaseSummaryScreen(ABC, BaseScreen):

    def __init__(self, locator_type: MobileBy, locator: str, locale: str = None):
        super().__init__(locator_type, locator, locale)

    @property
    @abstractmethod
    def _chb_accept_term_and_conditions(self) -> MobileCheckBox:
        pass

    @property
    @abstractmethod
    def _btn_submit(self) -> MobileButton:
        pass

    def accept_terms_and_conditions(self):
        self._chb_accept_term_and_conditions.check()

    def submit(self):
        self._btn_submit.tap()
