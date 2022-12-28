import allure

from d14_base.data_reader import DataReader

from d14_mobile_framework.framework.device.device import Device

from mobile_tests.screens.base.main_screens.main_screen import BaseMainScreen
from mobile_tests.screens.screen_resolver import ScreenResolver
from mobile_tests.steps.login_steps import LoginSteps
from mobile_tests.steps.service_steps import ServiceSteps


class ServiceNavigationSteps:

    UTILITIES_AND_MAINTENANCE = "Water and Electricity Bill Payment"

    @staticmethod
    def go_to_service(send_service, tap_service,
                      login=DataReader().get_env_data("SmartPassCredentials.username_sop1"),
                      password=DataReader().get_env_data("SmartPassCredentials.password_sop1"),
                      emirates_id=DataReader().get_env_data("UaePassCredentials.emirates_id"),
                      uae_pass=False,
                      adu_name=None, group_of_services=None, go_via_adu_items=False, switch_to_web_view=True):
        screen = ScreenResolver().factory

        with allure.step("Accept System pop up"):
            if screen.system_pop_up_screen.is_opened():
                screen.system_pop_up_screen.accept()

        with allure.step("Skip intro"):
            screen.intro_screen.skip()

        with allure.step("Login via SmartPass or via UAE pass"):
            if uae_pass:
                LoginSteps.uae_pass_authorize_with_info_skipping(emirates_id)
            else:
                LoginSteps.smart_pass_authorize_with_info_skipping(login, password)

        with allure.step("Close Meet home popup"):
            if screen.meet_home_pop_up_screen.is_opened():
                screen.meet_home_pop_up_screen.close()

        with allure.step("Close Quick tip popup"):
            if screen.quick_tip_popup.is_opened():
                screen.quick_tip_popup.ok()

        with allure.step("Open service tab"):
            screen.main_screen.open_screen(BaseMainScreen.Screen.SERVICES)
        if go_via_adu_items:
            with allure.step("Open ADU"):
                screen.services_screen.select_adu(adu_name)

            with allure.step("Click to Service Group in ADU"):
                screen.adu_search_services_screen.select_service(group_of_services)

            with allure.step("Close Quick tip popup"):
                screen.quick_tip_popup.wait_for_is_opened()
                screen.quick_tip_popup.ok()

            with allure.step("Click to search input field from ADU services screen"):
                screen.adu_services_screen.click_search_field()

            with allure.step("Find the service"):
                screen.services_screen.search_service(send_service)

            with allure.step("Close Quick tip popup"):
                if screen.quick_tip_popup.is_opened():
                    screen.quick_tip_popup.ok()

            with allure.step("Open the service"):
                if switch_to_web_view:
                    Device().switch_to_webview_after_action(lambda: ServiceSteps.select_service(tap_service))
                else:
                    ServiceSteps.select_service(tap_service)
        else:
            with allure.step("Click to search input field"):
                screen.services_screen.click_search_field()

            with allure.step("Close Quick tip popup"):
                if screen.quick_tip_popup.is_opened():
                    screen.quick_tip_popup.ok()

            with allure.step("Find the service"):
                screen.services_screen.search_service(send_service)

            with allure.step("Open the service"):
                if switch_to_web_view:
                    Device().switch_to_webview_after_action(lambda: ServiceSteps.select_service(tap_service))
                else:
                    ServiceSteps.select_service(tap_service)
