from d14_ui_framework.elements.button import Button
from d14_ui_framework.elements.label import Label
from d14_ui_framework.elements.base.element_state import ElementState
from d14_ui_framework.pages.base_page import BasePage


class BasePageHeader(BasePage):
    lbl_arabic = Label("//div[contains(@class, 'uil-header')]//button[contains(@class, 'language-switcher')]",
                       "Arabic label")
    lbl_profile = Label("//div[@class = 'uil-header-login__profile']|//div[@class='ui-lib-header-avatar']//img[not("
                        "contains(@class, 'avatar__default'))]|//div[@class='uil-header-avatar']//img[not("
                        "contains(@class, 'avatar__default'))]|//a[contains(@class, 'action-profile-btn') and not("
                        "contains(@class, 'loggedout'))]|"
                        "//button[contains(@aria-label, 'profile')]//img[contains(@class, 'avatar__image')]",
                        "Profile Label")

    lbl_tamm_icon = Label("//div[contains(@class, 'header__logo')]//a", "Tamm icon")

    btn_uae_pass = Button("//a[contains(@class, 'uaepass-button')]//img "
                          "| //button[contains(@type, 'submit')]//img[contains(@title, '{}')]", "UAE pass button",
                          locale="UAE pass Page.uae")
    btn_smart_pass = Button("//a[contains(@class, 'smart-pass-button')]//img|"
                            "(//div[contains(@class, 'smartpass')]//button//img)[2]", "Smart pass button")
    btn_logout = Button("//div[contains(@class, 'logout')]//a[contains(@class, 'secondary')]", "Logout button")
    btn_user_icon = Button("//i[contains(@class, 'person')] | //div[contains(@class, 'avatar')] "
                           "| //button[contains(@class, 'icon-start')] | //a[contains(@class, 'btn--loggedout')] "
                           "| //div[contains(@class, 'login_anonymous')]/button",
                           "User icon")
    btn_user_logged_icon = Button("//div[@class = 'uil-header-avatar']//img | //div[contains(@class, "
                                  "'avatar__sidebar')]//img", "Icon for logged user")

    def is_smart_pass_btn_present(self):
        return self.btn_smart_pass.soft_wait_for_element_state(ElementState.VISIBLE)

    def get_uae_pass_btn_url(self):
        return self.btn_user_logged_icon.get_attribute('href')

    def wait_for_not_logged_user_icon_present(self):
        self.btn_user_icon.wait_for_element_state(ElementState.VISIBLE)

    def is_profile_present(self):
        return self.lbl_profile.soft_wait_for_element_state(ElementState.EXISTS)

    def is_profile_present_fast(self):
        return self.lbl_profile.is_element_in_state(ElementState.EXISTS)

    def is_profile_absent(self):
        return self.lbl_profile.soft_wait_for_element_state(ElementState.ABSENT)

    def click_user_icon(self):
        self.btn_user_icon.click()

    def click_logged_user_icon(self):
        self.btn_user_logged_icon.click()

    def click_smart_pass(self):
        self.btn_smart_pass.click_js()

    def click_uae_pass(self):
        self.btn_uae_pass.click_js()

    def click_logout(self):
        self.btn_logout.click()

    def click_tamm_icon(self):
        self.lbl_tamm_icon.scroll_by_script()
        self.lbl_tamm_icon.wait_until_location_stable()
        self.lbl_tamm_icon.click()

    def click_switch_language(self):
        self.lbl_arabic.wait_until_location_stable()
        self.lbl_arabic.click()
