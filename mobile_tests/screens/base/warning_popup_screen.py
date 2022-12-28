from abc import ABC, abstractmethod

from appium.webdriver.common.mobileby import MobileBy
from d14_mobile_framework.framework.elements.element_state import ElementState

from d14_mobile_framework.framework.screens.base_screen import BaseScreen


class BaseWarningPopupScreen(ABC, BaseScreen):

    def __init__(self, locator_type: MobileBy, locator: str):
        super().__init__(locator_type, locator)

    @abstractmethod
    def ok(self):
        pass

    @abstractmethod
    def cancel(self):
        pass

    @abstractmethod
    def _btn_system_button(self, value):
        pass

    def _click_button(self, values):
        self.wait_for_is_opened()
        for value in values:
            button = self._btn_system_button(value)
            if button.is_element_in_state(ElementState.VISIBLE):
                button.tap()
                break
