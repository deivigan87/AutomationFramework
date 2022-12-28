from abc import ABC, abstractmethod

from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.text_field import MobileTextbox
from d14_mobile_framework.framework.screens.base_screen import BaseScreen


class BaseAduServicesScreen(ABC, BaseScreen):

    def __init__(self, locator_type: MobileBy, locator: str, locale: str = None):
        super().__init__(locator_type, locator, locale)

    @property
    @abstractmethod
    def _txb_search_field(self) -> MobileTextbox:
        pass

    def click_search_field(self):
        self._txb_search_field.tap()
