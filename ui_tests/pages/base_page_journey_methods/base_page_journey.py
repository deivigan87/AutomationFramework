from d14_ui_framework.elements.label import Label
from d14_ui_framework.elements.base.element_state import ElementState
from d14_ui_framework.pages.base_page import BasePage


class BasePageJourney(BasePage):
    lbl_spinner = Label("//div[contains(@class, 'page-spinner_visible')]", "Spinner Label")
    lbl_letters = Label("//body", "Get text data from page")

    @staticmethod
    def wait_until_spinner_disappear():
        BasePageJourney.lbl_spinner.wait_for_element_state(ElementState.ABSENT)
