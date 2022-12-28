from d14_ui_framework.elements.label import Label
from d14_ui_service_tests_templates.ui_tests.pages.base_page_journey_methods.base_page_header import BasePageHeader


class LoginRequiredPage(BasePageHeader):
    page_name = "Login Required Page"
    page_element = Label("//div[contains(text(), '{}')]", "Login Required page",
                         locale="Login Required Page.login_required")

    uae_pass_btn = Label("//div[contains(@class, 'login-required')]//a[contains(@aria-label, 'UAEPass Button')]",
                         "Uae pass button")

    def __init__(self):
        super(LoginRequiredPage, self).__init__(self.page_element)
