from d14_ui_framework.elements.label import Label
from d14_ui_framework.pages.base_page import BasePage


class DigitalSecondServicesPage(BasePage):
    page_name = "Second Services page"
    page_element = Label("//div", "Second services Page")

    def __init__(self):
        super(DigitalSecondServicesPage, self).__init__(self.page_element)
