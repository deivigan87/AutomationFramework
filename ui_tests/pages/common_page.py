from d14_ui_framework.elements.button import Button
from d14_ui_framework.elements.label import Label
from d14_ui_service_tests_templates.ui_tests.pages.base_page_journey_methods.base_page_header import BasePageHeader


class CommonPage(BasePageHeader):
    page_name = "Home Page"
    page_element = Label("//div[contains(@class, 'header')]", "Home page")
    btn_start = Label("//div[contains(text(), 'START')]", "Start service button")
    lbl_buy_tab = Label("//div[contains(@role, 'tab') and contains(text(), '{}')]", "Buy tab {}")
    btn_buy_start = Button("//button[contains(@aria-label, 'show')]", "Start button in snack")
    lbl_navigation_panel = Label("//span[contains(@class, 'uil-card')][contains(text(), '{}')]",
                                 "Navigation panels buttons {}")

    def __init__(self):
        super(CommonPage, self).__init__(self.page_element)

    def click_start_service_btn(self):
        self.btn_start.wait_until_location_stable()
        self.btn_start.scroll_by_script()
        self.btn_start.click()

    def click_tab_lbl(self, name_of_tab):
        self.lbl_buy_tab.format(name_of_tab).click_js()  # confirmed by customer

    def click_start_on_buy_tab(self):
        self.scroll_to_element(self.btn_buy_start)
        self.btn_buy_start.click_js()  # confirmed by customer

    def click_navigation_panel_lbl(self, panel_item):
        self.scroll_to_element(self.lbl_navigation_panel.format(panel_item))
        self.lbl_navigation_panel.format(panel_item).click_js()  # confirmed by customer
