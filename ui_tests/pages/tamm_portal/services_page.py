import allure

from d14_ui_framework.elements.button import Button
from d14_ui_framework.elements.label import Label
from d14_ui_framework.elements.base.element_state import ElementState
from d14_ui_service_tests_templates.ui_tests.pages.base_page_journey_methods.base_page_journey import BasePageJourney


class ServicesPage(BasePageJourney):
    page_name = "Search Home page"
    page_element = Label("//div[contains(@class, 'title')]", "Services Page")

    lbl_arabic = Label("//button[contains(@class, 'language-switcher') and contains(text(), 'عربي')]", "Arabic Lang")
    lbl_english = Label("//button[contains(@class, 'language-switcher') and contains(text(), 'English')]", "Eng Lang")

    btn_not_accept_cookies = Button("(//a[contains(@onclick, 'remove')])[1]", "Not Accept Cookies")
    lbl_table = Label("//div[contains(@class, 'table__pre-title')]", "Table")
    lbl_service_table = Label("//div[contains(@class, 'ui-lib-status')]", "Service Table")

    def __init__(self):
        self.page_element = Label("//div[contains(@class, 'title')]", "Services Page")
        super(ServicesPage, self).__init__(self.page_element)

    def is_cookies_message_displayed(self):
        return self.btn_not_accept_cookies.soft_wait_for_element_state(ElementState.EXISTS)

    def is_table_present(self):
        return self.lbl_table.soft_wait_for_element_state(ElementState.EXISTS)

    def is_arab_lang_btn_present(self):
        return self.lbl_arabic.soft_wait_for_element_state(ElementState.EXISTS)

    def is_service_table_present(self):
        return self.lbl_service_table.soft_wait_for_element_state(ElementState.VISIBLE)

    def is_eng_lang_btn_present(self):
        return self.lbl_english.soft_wait_for_element_state(ElementState.EXISTS)

    def change_language_to_ar(self):
        with allure.step("Change language to Arabic"):
            self.lbl_arabic.wait_for_element_state(ElementState.VISIBLE)
            self.close_cookies_message()
            self.lbl_arabic.click()

    def change_language_to_eng(self):
        with allure.step("Change language to English"):
            self.lbl_english.wait_for_element_state(ElementState.VISIBLE)
            self.close_cookies_message()
            self.lbl_english.click()

    def close_cookies_message(self):
        if self.is_cookies_message_displayed():
            self.btn_not_accept_cookies.click()
