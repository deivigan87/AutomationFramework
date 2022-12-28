from abc import ABC, abstractmethod

from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.device.device import Device
from d14_mobile_framework.framework.device.swipe_direction import SwipeDirection
from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.element_state import ElementState
from d14_mobile_framework.framework.elements.element_types import ElementType
from d14_mobile_framework.framework.elements.list_of_elements import MobileListOfElements
from d14_mobile_framework.framework.elements.text_field import MobileTextbox
from d14_mobile_framework.framework.screens.base_screen import BaseScreen
from d14_mobile_framework.framework.utils.wait_for import wait_for


class BaseServicesScreen(ABC, BaseScreen):

    def __init__(self, locator_type: MobileBy, locator: str, locale: str = None):
        super().__init__(locator_type, locator, locale)

    class Journey:
        BUY_A_HOME = "Services Screen.buy_a_home"

    class Service:
        BILL_PAYMENT = "Services Screen.bill_payment"

    class Tab:
        JOURNEYS = "Services Screen.journeys_tab"
        SERVICES = "Services Screen.services_tab"

    class ADU:
        HOUSING_AND_PROPERTY = "ADU.housing_and_property"

    @property
    @abstractmethod
    def _btn_more(self) -> MobileButton:
        pass

    @property
    @abstractmethod
    def _btn_filter_services_tab(self) -> MobileButton:
        pass

    @abstractmethod
    def _btn_adu(self, key) -> MobileButton:
        pass

    @abstractmethod
    def _btn_journey(self, key) -> MobileButton:
        pass

    @abstractmethod
    def _btn_service(self, key) -> MobileButton:
        pass

    @abstractmethod
    def _btn_tab(self, key) -> MobileButton:
        pass

    @property
    @abstractmethod
    def _txb_search_field(self) -> MobileTextbox:
        pass

    @property
    @abstractmethod
    def _txb_search_field_input(self) -> MobileTextbox:
        pass

    @abstractmethod
    def _lst_adu(self) -> MobileListOfElements[ElementType.MOBILE_LABEL]:
        pass

    @abstractmethod
    def _lst_journeys(self) -> MobileListOfElements[ElementType.MOBILE_LABEL]:
        pass

    @abstractmethod
    def _lst_services(self) -> MobileListOfElements[ElementType.MOBILE_LABEL]:
        pass

    def select_adu(self, adu):

        def wait_for_adu():
            if self._btn_adu(adu).is_element_in_state(ElementState.EXISTS) \
                    and self._btn_adu(adu).is_element_in_state(ElementState.VISIBLE):
                Device().swipe(SwipeDirection.DOWN)
                return True
            else:
                Device().swipe(SwipeDirection.DOWN)
            return False

        wait_for(lambda: self._lst_adu().size > 0, message="Adu list is empty")
        wait_for(wait_for_adu, message="{} adu is absent".format(adu))
        self._btn_adu(adu).tap()

    def select_journey(self, journey: Journey):

        def wait_for_journey():
            if self._btn_journey(journey).is_element_in_state(ElementState.EXISTS) \
                    and self._btn_journey(journey).is_element_in_state(ElementState.VISIBLE):
                Device().swipe(SwipeDirection.DOWN)
                return True
            else:
                Device().swipe(SwipeDirection.DOWN)
            return False

        wait_for(lambda: self._lst_journeys().size > 0, message="Journeys list is empty")
        wait_for(wait_for_journey, message="{} journey is absent".format(journey))
        self._btn_journey(journey).tap()

    def select_service(self, service):

        def wait_for_service():
            if self._btn_service(service[1:]).is_element_in_state(ElementState.EXISTS) \
                    and self._btn_service(service[1:]).is_element_in_state(ElementState.VISIBLE):
                Device().swipe(SwipeDirection.DOWN)
                return True
            else:
                Device().swipe(SwipeDirection.DOWN)
            return False

        wait_for(lambda: self._lst_services().size > 0, message="Service list is empty")
        wait_for(wait_for_service, message="{} service is absent".format(service))
        self._btn_service(service[1:]).tap()

    def click_search_field(self):
        self._txb_search_field.tap()

    def search_service(self, service):
        self._txb_search_field_input.set_text(service)
        self._txb_search_field_input.tap()
        Device().driver.execute_script("mobile:performEditorAction", {"action": "search"})

    def select_tab(self, tab: Tab):
        self._btn_tab(tab).tap()

    def is_filter_services_tab_present(self):
        return self._btn_filter_services_tab.is_element_in_state(ElementState.EXISTS)
