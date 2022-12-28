from appium.webdriver.common.mobileby import MobileBy
from d14_mobile_framework.framework.utils.wait_for import wait_for

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.android.system_popup_screen import SystemPopUpScreen
from mobile_tests.screens.android.warning_popup_screen import WarningPopupScreen

from mobile_tests.screens.base.main_screens.services_screens.pre_services_screen import BasePreServicesScreen


class PreServicesScreen(BasePreServicesScreen):

    def __init__(self):
        super().__init__(MobileBy.ID, 'epoxy_rv')

    @property
    def _start_service(self) -> MobileButton:
        return MobileButton(MobileBy.XPATH, '//button[contains(text(), "start")]|//*[contains(@resource-id, '
                                            '"txtProceed")]', 'Start button')

    def click_start_service_btn(self):
        self._start_service.tap()

    @staticmethod
    def click_accept_system_screen():
        system_pop_up_screen = SystemPopUpScreen()

        def wait_for_screen():
            if system_pop_up_screen.is_opened():
                return True
            else:
                return False

        wait_for(wait_for_screen, message="Screen is absent")
        system_pop_up_screen.accept()

    def click_start_service(self):
        system_pop_up_screen = SystemPopUpScreen()
        warning_pop_up_screen = WarningPopupScreen()

        def method():
            try:
                if warning_pop_up_screen.is_opened():
                    warning_pop_up_screen.ok()
                if system_pop_up_screen.is_opened():
                    self.click_accept_system_screen()
                self._start_service.tap()
                return True
            except:  # noqa.
                return False

        wait_for(method, message="Start Service Button is absent")

        for i in range(35):
            if warning_pop_up_screen.is_opened():
                warning_pop_up_screen.ok()
            if system_pop_up_screen.is_opened():
                self.click_accept_system_screen()
