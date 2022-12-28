from d14_ui_framework.elements.label import Label
from d14_ui_framework.pages.base_page import BasePage


class DigitalServicesPage(BasePage):
    page_name = "Services page"
    page_element = Label("//div", "Services Page")

    def __init__(self):
        super(DigitalServicesPage, self).__init__(self.page_element)
