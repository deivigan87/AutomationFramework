from d14_mobile_framework.framework.elements.element_state import ElementState
from d14_ui_framework.elements.button import Button
from d14_ui_framework.elements.label import Label
from d14_ui_framework.pages.base_page import BasePage


class Footer(BasePage):
    __page_element = Label("//section[contains(@class,'footer')]", "Landing page footer")

    __footer_item_xpath = "//li//a[contains(text(),'{}')]"

    __btn_follow = Button("//i[contains(@class,'{}')]", "{} social icon")

    def __init__(self):
        super(Footer, self).__init__(self.__page_element)

    def click_footer_lbl(self, name):
        lbl_footer_item = Label(self.__footer_item_xpath, "{} footer label", locale="Footer.{}".format(name))
        lbl_footer_item.wait_for_element_state(ElementState.VISIBLE)
        lbl_footer_item.click()

    def click_follow_us_btn(self, name):
        self.__btn_follow.format(name).wait_for_element_state(ElementState.VISIBLE)
        self.__btn_follow.format(name).click()
