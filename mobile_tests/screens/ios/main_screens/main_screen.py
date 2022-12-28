from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.main_screens.main_screen import BaseMainScreen
from mobile_tests.screens.ios.system_popup_screen import SystemPopUpScreen


class MainScreen(BaseMainScreen):

    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, 'burgerMenu')

    @property
    def _btn_menu(self) -> MobileButton:
        return MobileButton(MobileBy.ACCESSIBILITY_ID, 'burgerMenu', "Burger menu")

    def _btn_menu_item(self, key) -> MobileButton:
        return MobileButton(MobileBy.ACCESSIBILITY_ID, '{}', key, key)

    def _btn_screen(self, key) -> MobileButton:
        return MobileButton(MobileBy.NAME, '{}', key, key)

    @property
    def _btn_english(self) -> MobileButton:
        return MobileButton(MobileBy.ACCESSIBILITY_ID, '//XCUIElementTypeStaticText[@name="{}"]', "English",
                            "Main screen.english")

    @property
    def _btn_arabic(self) -> MobileButton:
        return MobileButton(MobileBy.ACCESSIBILITY_ID, '//XCUIElementTypeStaticText[@name="{}"]', "Arabic",
                            "Main screen.arabic")

    @property
    def _btn_language(self) -> MobileButton:
        return MobileButton(MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="{}"]', "Language",
                            "Main screen.language")

    def select_language(self, language):
        SystemPopUpScreen().decline()
        super().select_language(language)
