import time

import self as self
from d14_mobile_framework.framework.elements.element_state import ElementState
# from d14_ui_framework.elements.button import Button
from d14_ui_framework.elements.label import Label
from d14_ui_framework.pages.base_page import BasePage


class Homepage(BasePage):
    __page_element = Label("//div[@class='ui-lib-home-page']", "Landing homepage")
    lbl_icon_search = Label("//div[@class='TPN-header__action-search']/a", "Search Icon")

    def __int__(self):
        super(Homepage, self).__int__(self.__page_element)

    def click_search_icon(self):
        self.lbl_icon_search.wait_for_element_state(ElementState.VISIBLE)
        self.lbl_icon_search.click()

    def click_searchbox(self):
        print("-click search box-")
        self.__searchBox_iteam.wait_for_element_state(ElementState.VISIBLE).click()

    def send_text(name):
        print("-send text function-")
        self.__searchBox_iteam.wait_for_element_state(ElementState.VISIBLE).send_keys(name)
        self.__searchBox_iteam.click_enter_button()

