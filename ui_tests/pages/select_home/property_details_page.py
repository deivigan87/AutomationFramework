from d14_ui_framework.elements.button import Button
from d14_ui_framework.elements.label import Label
from d14_ui_service_tests_templates.ui_tests.pages.base_page_journey_methods.base_page_header import BasePageHeader
from d14_ui_service_tests_templates.ui_tests.pages.base_page_journey_methods.base_page_journey import BasePageJourney


class PropertyDetailsPage(BasePageJourney, BasePageHeader):
    page_name = "Property details page"
    page_element = Label("//div[contains(text(), '{}')]", "Property Details Page",
                         locale="Property Details Page.property")

    btn_get_financing = Button("//div[contains(@class, 'financing')]//button[contains(@class, 'goto-finance')]",
                               "Get home financing Button")

    def __init__(self):
        super(PropertyDetailsPage, self).__init__(self.page_element)

    def click_get_financing_btn(self):
        self.scroll_to_element(self.btn_get_financing)
        self.btn_get_financing.click()
