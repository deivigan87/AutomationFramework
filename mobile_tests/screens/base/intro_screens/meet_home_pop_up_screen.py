from abc import ABC, abstractmethod

from appium.webdriver.common.mobileby import MobileBy
from d14_mobile_framework.framework.elements.button import MobileButton

from d14_mobile_framework.framework.screens.base_screen import BaseScreen


class BaseMeetHomePopUpScreen(ABC, BaseScreen):
    def __init__(self, locator_type: MobileBy, locator: str):
        super().__init__(locator_type, locator)

    @property
    @abstractmethod
    def _btn_close(self) -> MobileButton:
        pass

    def close(self):
        self._btn_close.tap()
