import allure

from d14_base.data_reader import DataReader
from d14_ui_service_tests_templates.ui_tests.pages.base_page_journey_methods.base_page_journey import BasePageJourney
from d14_ui_service_tests_templates.ui_tests.pages.common_page import CommonPage
from d14_ui_service_tests_templates.ui_tests.pages.navigation_home_items import NavigationHomeItems


class NavigateSteps(BasePageJourney):
    """Navigate methods"""

    @staticmethod
    def go_to_specific_tab(name_of_tab):
        with allure.step("Click to specific tab"):
            home_page = CommonPage()
            home_page.click_tab_lbl(name_of_tab)

    @staticmethod
    def go_to_search_page():
        with allure.step("Click to Buy tab"):
            home_page = CommonPage()
            home_page.wait_page_to_load()
            NavigateSteps.go_to_specific_tab(DataReader().get_from_locale("Home Page.buy_tab"))

        with allure.step("Select Start Button"):
            home_page.click_start_on_buy_tab()

        with allure.step("Select 'Home Search' item"):
            home_page.click_navigation_panel_lbl(NavigationHomeItems.HOME_SEARCH.value)
            BasePageJourney.wait_until_spinner_disappear()
