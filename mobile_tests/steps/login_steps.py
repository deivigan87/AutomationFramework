import allure

from d14_mobile_framework.framework.utils.wait_for import wait_for
from mobile_tests.screens.base.intro_screens.login_screen import BaseLoginScreen
from mobile_tests.screens.base.main_screens.main_screen import BaseMainScreen
from mobile_tests.screens.screen_resolver import ScreenResolver


class LoginSteps:

    @staticmethod
    def smart_pass_authorize_with_info_skipping(login, password):
        screen = ScreenResolver().factory
        with allure.step("Select SmartPass authorization"):
            screen.login_screen.select_authorization_type(BaseLoginScreen.LoginType.SMART_PASS)

        with allure.step("Continue on the System pop up"):
            if screen.system_pop_up_screen.is_opened():
                screen.system_pop_up_screen.continue_action()

        wait_for(LoginSteps.__is_main_or_additional_screens_and_popups_present,
                 message="The main or additional screens/popups absent")

        LoginSteps.is_sop1_pop_up_present()

        if screen.download_offline_map_popup.is_opened() or screen.main_screen.is_opened() \
                or screen.quick_tip_popup.is_opened():
            if screen.download_offline_map_popup.is_opened():
                with allure.step("Cancel map downloading"):
                    screen.download_offline_map_popup.cancel()
            if screen.quick_tip_popup.is_opened():
                with allure.step("Click to Ok for Quick tip pop up"):
                    screen.quick_tip_popup.ok()
            with allure.step("Logout"):
                screen.main_screen.click_menu_item(BaseMainScreen.MenuItem.LOGOUT)
            with allure.step("Select SmartPass authorization"):
                screen.login_screen.select_authorization_type(BaseLoginScreen.LoginType.SMART_PASS)
            with allure.step("Authorization"):
                screen.login_smart_pass_page_screen.authorize_smart_pass(login, password)
                screen.login_smart_pass_page_screen.wait_for_is_closed()
            LoginSteps.is_sop1_pop_up_present()
        elif screen.login_smart_pass_page_screen.is_opened():
            with allure.step("Authorization"):
                screen.login_smart_pass_page_screen.authorize_smart_pass(login, password)
                screen.login_smart_pass_page_screen.wait_for_is_closed()
            LoginSteps.is_sop1_pop_up_present()
            if screen.download_offline_map_popup.is_opened():
                with allure.step("Cancel map downloading"):
                    screen.download_offline_map_popup.cancel()

    @staticmethod
    def uae_pass_authorize_with_info_skipping(emirates_id):
        screen = ScreenResolver().factory
        with allure.step("Select SmartPass authorization"):
            screen.login_screen.select_authorization_type(BaseLoginScreen.LoginType.UAE_PASS)

        wait_for(LoginSteps.__is_main_or_additional_screens_and_popups_present,
                 message="The main or additional screens/popups absent")

        if screen.download_offline_map_popup.is_opened() or screen.main_screen.is_opened() \
                or screen.quick_tip_popup.is_opened():
            if screen.download_offline_map_popup.is_opened():
                with allure.step("Cancel map downloading"):
                    screen.download_offline_map_popup.cancel()
            if screen.quick_tip_popup.is_opened():
                with allure.step("Click to Ok for Quick tip pop up"):
                    screen.quick_tip_popup.ok()
            with allure.step("Logout"):
                screen.main_screen.click_menu_item(BaseMainScreen.MenuItem.LOGOUT)
            with allure.step("Select SmartPass authorization"):
                screen.login_screen.select_authorization_type(BaseLoginScreen.LoginType.UAE_PASS)
            with allure.step("Authorization"):
                screen.login_smart_pass_page_screen.authorize_uae_pass(emirates_id)
                screen.login_smart_pass_page_screen.wait_for_is_closed()
            LoginSteps.is_sop1_pop_up_present()
        elif screen.login_uae_pass_page_screen.is_opened():
            with allure.step("Authorization"):
                screen.login_uae_pass_page_screen.authorize_uae_pass(emirates_id)
                screen.login_uae_pass_page_screen.wait_for_is_closed()
            LoginSteps.is_sop1_pop_up_present()
            if screen.download_offline_map_popup.is_opened():
                with allure.step("Cancel map downloading"):
                    screen.download_offline_map_popup.cancel()

    @staticmethod
    def is_sop1_pop_up_present():
        screen = ScreenResolver().factory
        wait_for(LoginSteps.__is_main_or_additional_screens_and_popups_present,
                 message="The main or additional screens/popups absent")
        if screen.sop1_screen.is_opened():
            with allure.step("Skip SOP1 Screen"):
                screen.sop1_screen.skip()
                if ScreenResolver().factory.quick_tip_popup.is_opened:
                    wait_for(ScreenResolver().factory.quick_tip_popup.is_opened,
                             message="Quick tip popup is not opened")

    @staticmethod
    def guest_user_login():
        screen = ScreenResolver().factory
        with allure.step("Select Login as Quest user"):
            screen.login_screen.select_authorization_type(BaseLoginScreen.LoginType.GUEST_USER)
        with allure.step("Cancel map downloading"):
            screen.download_offline_map_popup.cancel()

    @staticmethod
    def __is_main_or_additional_screens_and_popups_present():
        return ScreenResolver().factory.download_offline_map_popup.is_opened() or ScreenResolver().\
            factory.quick_tip_popup.is_opened() or ScreenResolver().factory.login_smart_pass_page_screen.\
            is_opened() or ScreenResolver().factory.login_uae_pass_page_screen.\
            is_opened() or ScreenResolver().factory.sop1_screen.is_opened() or ScreenResolver().factory.\
            main_screen.is_opened() or ScreenResolver().factory.meet_home_pop_up_screen.is_opened()
