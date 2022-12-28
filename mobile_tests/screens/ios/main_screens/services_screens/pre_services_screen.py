from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.main_screens.services_screens.pre_services_screen import BasePreServicesScreen


class PreServicesScreen(BasePreServicesScreen):

    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, 'Tamm_Stage.ServicesDetailView')

    @property
    def _start_service(self) -> MobileButton:
        return MobileButton(MobileBy.XPATH, '//XCUIElementTypeButton[@name="{}"]', "Start", "Pre services Screen.start")

    def click_start_service(self):
        self.wait_for_is_opened()
        self._start_service.tap_via_coordinates()
