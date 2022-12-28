from abc import ABC, abstractmethod

from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.element_state import ElementState
from d14_mobile_framework.framework.elements.element_types import ElementType
from d14_mobile_framework.framework.elements.label import MobileLabel
from d14_mobile_framework.framework.elements.list_of_elements import MobileListOfElements
from d14_mobile_framework.framework.screens.base_screen import BaseScreen
from d14_mobile_framework.framework.utils.wait_for import wait_for


class BasePackagesScreen(ABC, BaseScreen):

    def __init__(self, locator_type: MobileBy, locator: str, locale: str = None):
        super().__init__(locator_type, locator, locale)

    @property
    @abstractmethod
    def _list_packages(self) -> MobileListOfElements[ElementType.MOBILE_BUTTON]:
        pass

    @property
    @abstractmethod
    def _btn_next(self) -> MobileButton:
        pass

    @abstractmethod
    def _selected_package(self, index: int) -> MobileLabel:
        pass

    def tap_package(self, index: int):
        wait_for(lambda: self._list_packages.size > 0, message="Packages list is empty")
        self._list_packages.get_elements()[index].tap()

    def is_package_selected(self, index: int) -> bool:
        return self._selected_package(index).is_element_in_state(ElementState.EXISTS)

    def tap_next(self):
        self._btn_next.tap()
