from abc import ABC, abstractmethod

from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.device.device import Device
from d14_mobile_framework.framework.device.swipe_direction import SwipeDirection
from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.element_state import ElementState
from d14_mobile_framework.framework.elements.element_types import ElementType
from d14_mobile_framework.framework.elements.list_of_elements import MobileListOfElements
from d14_mobile_framework.framework.screens.base_screen import BaseScreen
from d14_mobile_framework.framework.utils.wait_for import wait_for


class BaseAduSearchServicesScreen(ABC, BaseScreen):

    def __init__(self, locator_type: MobileBy, locator: str, locale: str = None):
        super().__init__(locator_type, locator, locale)

    class GroupOfServices:
        BUILDING_AND_CONSTRUCTION = "ADU Search Services Screen.building_and_construction"
        UTILITIES_AND_MAINTENANCE = "ADU Search Services Screen.utilities_and_maintenance"

    @abstractmethod
    def _btn_service(self, key) -> MobileButton:
        pass

    @abstractmethod
    def _lst_services(self) -> MobileListOfElements[ElementType.MOBILE_LABEL]:
        pass

    def select_service(self, group_of_services):

        def wait_for_service():
            if self._btn_service(group_of_services).is_element_in_state(ElementState.EXISTS) \
                    and self._btn_service(group_of_services).is_element_in_state(ElementState.VISIBLE):
                Device().swipe(SwipeDirection.DOWN)
                return True
            else:
                Device().swipe(SwipeDirection.DOWN)
            return False

        wait_for(lambda: self._lst_services().size > 0, message="Service list is empty")
        wait_for(wait_for_service, message="{} service is absent".format(group_of_services))
        self._btn_service(group_of_services).tap()
        self.wait_for_is_closed()
