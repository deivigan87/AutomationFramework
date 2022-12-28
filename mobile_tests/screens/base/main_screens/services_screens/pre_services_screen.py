from abc import ABC, abstractmethod

from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.screens.base_screen import BaseScreen


class BasePreServicesScreen(ABC, BaseScreen):

    def __init__(self, locator_type: MobileBy, locator: str, locale: str = None):
        super().__init__(locator_type, locator, locale)

    @property
    @abstractmethod
    def _start_service(self) -> MobileButton:
        pass

    def click_start_service(self):
        self._start_service.tap()
