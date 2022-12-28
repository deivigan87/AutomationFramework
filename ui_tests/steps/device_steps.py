import allure

from d14_ui_framework.browser.browser import Browser
from d14_ui_framework.pages.base_page import BasePage


class DeviceSteps(BasePage):
    """Steps if browser was opened on mobile/tablet device"""

    @staticmethod
    def do_specific_action_mobile_device(device_action, desktop_action):
        """
        :param device_action:
        :param desktop_action:
        :return: value if sent method will return any data
        Examples for using:
         DeviceSteps. \
                do_specific_action_different_devices([[manage_base_page.click_specific_item_dropdown, [parameter]]],
                                                     [[manage_base_page.click_my_tab,
                                                       [EnvReader().get_from_locale(
                                                           "Manage My Property Page.my_services_tab")]]])

         where [[manage_base_page.click_specific_item_dropdown, ["SERVICES"]]] - method and 1 parameter for mobile
         device
         and [[manage_base_page.click_my_tab, [EnvReader().
                                    get_from_locale("Manage My Property Page.my_services_tab")]]] - method and argument
                                    for desktop and tablet.

         if need to send 1 method without argument: [[instance_of_page.name_of_method, []]],
         if need to send several methods for 1 device:
         [[instance_of_page.name_of_method_1, [parameter]], [instance_of_page.name_of_method_2, [parameter]]]
         if need to send 1 method with several parameters: [[instance_of_page.name_of_method, [parameter1, parameter2]]]

        """
        global value_data
        with allure.step("Check that Android or IOS device was used"):
            if Browser.is_mobile():
                Browser.wait_for_page_to_load()
                for function_and_args in device_action:
                    value_data = function_and_args[0](*function_and_args[1])
            else:
                Browser.wait_for_page_to_load()
                for function_and_args in desktop_action:
                    value_data = function_and_args[0](*function_and_args[1])
            return value_data

    @staticmethod
    def do_only_mobile_action_device(*actions):
        """
        :param actions: actions which need to do on mobile
        :return: value if sent method will return any data

        Example:
            DeviceSteps.do_only_mobile_action_device([request_callback_page.click_displaying_btn_device, []])

        Where [request_callback_page.click_displaying_btn_device, []]:
        request_callback_page.click_displaying_btn_device is 1 method
        [] - it's mean that without parameters
         if need to send several methods for 1 device:
         [[instance_of_page.name_of_method_1, [parameter]], [instance_of_page.name_of_method_2, [parameter]]]
         if need to send 1 method with several parameters: [[instance_of_page.name_of_method, [parameter1, parameter2]]]

        """
        global value_data
        with allure.step("Check that Android or IOS mobile device was used"):
            if Browser.is_mobile():
                Browser.wait_for_page_to_load()
                for function_and_args in actions:
                    value_data = function_and_args[0](*function_and_args[1])
                return value_data

    @staticmethod
    def do_only_tablet_action_device(*actions):
        global value_data
        with allure.step("Check that Android or IOS tablet device was used"):
            if Browser.is_tablet():
                Browser.wait_for_page_to_load()
                for function_and_args in actions:
                    value_data = function_and_args[0](*function_and_args[1])
                return value_data

    @staticmethod
    def do_mobile_or_tablet_action_device(*actions):
        global value_data
        with allure.step("Check that Android or IOS mobile/tablet device was used"):
            if Browser.is_mobile() or Browser.is_tablet():
                Browser.wait_for_page_to_load()
                for function_and_args in actions:
                    value_data = function_and_args[0](*function_and_args[1])
                return value_data
