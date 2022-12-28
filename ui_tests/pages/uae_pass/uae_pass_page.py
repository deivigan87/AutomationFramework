from selenium.webdriver.common.keys import Keys

from d14_ui_framework.elements.base.element_state import ElementState
from d14_ui_framework.pages.base_page import BasePage
from d14_ui_framework.elements.button import Button
from d14_ui_framework.elements.label import Label
from d14_ui_framework.elements.text_box import TextBox


class UaePassPage(BasePage):
    page_name = "UAE Page"
    page_element = Label("//div[contains(@class, 'login-to-uaepass')]", "UAE Pass Page")

    tbx_user_input_field = TextBox('//input[@id="username"]', "User input field")
    btn_login = Button('//input[@id="basicPasswordForm-submitButton"]', "Login button")
    uae_pass_submit_button = Label("//input[@value='Submit']", "Submit button")

    def __init__(self):
        super(UaePassPage, self).__init__(self.page_element)

    def send_user_info(self, data):
        self.tbx_user_input_field.scroll_by_script()
        len_txt_value = len(self.tbx_user_input_field.get_value())
        self.tbx_user_input_field.send_keys(len_txt_value * Keys.BACKSPACE)
        self.tbx_user_input_field.send_keys(data)

    def click_login(self):
        self.btn_login.click_js()

    def click_submit(self):
        self.uae_pass_submit_button.wait_for_element_state(ElementState.VISIBLE)
        self.uae_pass_submit_button.click()
