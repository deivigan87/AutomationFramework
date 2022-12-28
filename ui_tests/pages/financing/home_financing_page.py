from d14_ui_framework.elements.label import Label
from d14_ui_framework.pages.base_page import BasePage


class HomeFinancingPage(BasePage):
    page_name = "Home Financing page"
    page_element = Label("//div[contains(@class, 'qa-hero')][contains(text(), '{}')]", "Home Financing Page",
                         locale="Home Financing Page.home_financing")

    lbl_property_price = Label("//input[contains(@aria-label, 'price')]", "Property price on Home Financing page")

    def __init__(self):
        super(HomeFinancingPage, self).__init__(self.page_element)

    def get_property_price(self):
        return self.lbl_property_price.get_value()
