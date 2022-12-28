from d14_ui_framework.browser.browser import Browser
from d14_ui_framework.elements.button import Button
from d14_ui_framework.elements.list import List
from d14_ui_framework.elements.base.element_state import ElementState
from d14_base.string_util import StringUtil
from d14_ui_framework.elements.label import Label
from d14_ui_service_tests_templates.ui_tests.pages.base_page_journey_methods.base_page_journey import BasePageJourney


class SearchCommonPage(BasePageJourney):
    page_name = "Search Home page"

    lst_of_results_quick_search = List("//div[contains(@class, 'row-flex')]//div[contains(@class, 'price number')]",
                                       "List of results price for homes Tiles view")
    btn_property_banner = Button(
        "//div[contains(@class, 'property-tile clickable')][.//div[contains(@class, 'price number') "
        "and (contains(., '{}'))]]//div[contains(@class, 'header-hero')]",
        "Button Select home according price {}")
    lbl_island_location = Label(
        "//div[contains(@class, 'summary')][.//div[contains(@class, 'price')][contains(., '{}')]]"
        "//span[contains(@class, '__title')]",
        "Island Location Text {}")
    lbl_area_location = Label(
        "//div[contains(@class, 'summary')][.//div[contains(@class, 'price')][contains(., '{}')]]"
        "//span[contains(@class, 'subtitle')]",
        "Area Location Text {}")
    lbl_area_size = Label(
        "//div[contains(@class, 'summary')][.//div[contains(@class, 'price')][contains(., '{}')]]"
        "//div[contains(@class, 'hoz')]//div",
        "Area size {}")

    def __init__(self):
        if Browser.is_mobile():
            self.page_element = Label("//div[contains(@class, 'search-home-phone')]", "Search Home Page")
        else:
            self.page_element = Label("//div[contains(text(), '{}')]", "Search Home Page",
                                      locale="Search Home Page.search_for_a_home")
        super(SearchCommonPage, self).__init__(self.page_element)

    def get_data_from_selected_home(self):
        """
        Get Island, Area, Price data from opened random home
        :return: list: list with parameters for selected home
        """
        random_home = self.get_random_data_about_home_from_locator(self.lst_of_results_quick_search, False)
        self.btn_property_banner.format(random_home[0]).scroll_by_script()
        self.btn_property_banner.format(random_home[0]).click()
        return random_home

    def get_random_data_about_home_from_locator(self, object_locator, is_star, page=None):
        """
        Get random data from list about home from locator
        :param is_star: bool: true if star is present
        :param page: page with locators
        :param object_locator: locator for data
        :return: list: list of search data
        """
        if is_star:
            while page.lbl_star_enabled_without_price.soft_wait_for_element_state(ElementState.ABSENT):
                page.click_btn_load_more()
        list_of_search = []
        price_of_home = object_locator.get_random_items_from_list(1)
        price_regular = StringUtil.get_text_without_letters(price_of_home)
        list_of_search.append(price_regular)
        list_of_search.append(self.get_island_location(price_regular))
        list_of_search.append(StringUtil.get_text_after_splitting_by_comma(self.get_area_location(price_regular))[0].
                              title())  # Get island
        list_of_search.append(StringUtil.get_text_after_splitting_by_comma(self.get_area_location(price_regular))[1].
                              title())  # Get city
        list_of_search.append(self.get_area_size(price_regular))
        return list_of_search

    def get_island_location(self, price):
        """
        Method connected with returning island text for selected home
        :return: str: island text
        """
        return self.lbl_island_location.format(price).get_text()

    def get_area_location(self, price):
        """
        Get area text for selected home
        :return: str: area text
        """
        return self.lbl_area_location.format(price).get_text()

    def get_area_size(self, price):
        """
        Method connected with returning area size text for selected home
        :return: str: area size text
        """
        return self.lbl_area_size.format(price).get_text()
