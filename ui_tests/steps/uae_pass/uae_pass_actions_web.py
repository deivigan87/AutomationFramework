from d14_ui_framework.elements.base.element_state import ElementState
from d14_ui_framework.pages.base_page import BasePage
from d14_ui_framework.elements.button import Button
from d14_ui_framework.elements.label import Label


class UAEPassActionsWeb(BasePage):
    """Actions on UAE page in browser"""

    lbl_email_uae = Label("//input[contains(@id, 'userIdentifier')]", "Email field UAE page")

    btn_confirm_uae = Button("//span[contains(@class, 'mobileIdWaitForAuthnMessage2Text')]", "Confirm button UAE "
                                                                                             "login page")
    btn_login_uae = Button("//input[contains(@id, 'basicPasswordForm-submitButton')]", "Login button UAE page")

    @staticmethod
    def send_email(email):
        UAEPassActionsWeb.lbl_email_uae.send_keys(email)

    @staticmethod
    def click_login_uae():
        UAEPassActionsWeb.btn_login_uae.wait_for_element_state(ElementState.VISIBLE)
        UAEPassActionsWeb.btn_login_uae.click()

    @staticmethod
    def wait_confirm_page():
        UAEPassActionsWeb.btn_confirm_uae.wait_for_element_state(ElementState.VISIBLE)
