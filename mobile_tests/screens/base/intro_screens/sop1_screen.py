from abc import ABC, abstractmethod

from appium.webdriver.common.mobileby import MobileBy
from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.screens.base_screen import BaseScreen


class BaseSOP1Screen(ABC, BaseScreen):

    def __init__(self, locator_type: MobileBy, locator: str, locale: str = None):
        super().__init__(locator_type, locator, locale)

    @property
    @abstractmethod
    def _btn_cancel(self) -> MobileButton:
        pass

    def skip(self):
        self._btn_cancel.tap()
