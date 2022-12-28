from d14_ui_framework.pages.base_page import BasePage
from d14_ui_framework.elements.button import Button
from d14_ui_framework.elements.label import Label
from d14_ui_framework.elements.text_box import TextBox


class SmartPassPage(BasePage):
    page_name = "SmartPass Page"
    page_element = Label("//a[contains(@id, 'SmartPassTitle')]", "Smart Pass Page")

    tbx_user_name_field = TextBox("//div[contains(@class, 'form-value')]//input[contains(@class, 'ng-pristine') and "
                                  "contains(@name, 'username')]",
                                  "User name field")
    tbx_user_password_field = TextBox("//div[contains(@class, 'form-value')]//input[contains(@class, 'ng-pristine') and"
                                      " contains(@name, 'password')]",
                                      "User password field")

    btn_login = Button("//input[contains(@type, 'submit')]", "Login button")

    def __init__(self):
        super(SmartPassPage, self).__init__(self.page_element)

    def send_username(self, data):
        self.tbx_user_name_field.scroll_by_script()
        self.tbx_user_name_field.send_keys(data)

    def send_password(self, data):
        self.tbx_user_password_field.send_keys(data)

    def click_login(self):
        self.btn_login.click_js()
