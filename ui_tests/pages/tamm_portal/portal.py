from d14_mobile_framework.framework.elements.element_state import ElementState
from d14_ui_framework.elements.button import Button
from d14_ui_framework.elements.label import Label
from d14_ui_framework.pages.base_page import BasePage


class Portal(BasePage):
    __page_element = Label("//div[contains(@class,'component container')]", "Portal page")

    __btn_1st_apply = Button("(//div[contains(@class, 'wo-btn')])[1]", "Apply button")

    def __init__(self):
        super(Portal, self).__init__(self.__page_element)

    def click_1st_apply_btn(self):
        self.__btn_1st_apply.wait_for_element_state(ElementState.VISIBLE)
        self.__btn_1st_apply.click()
