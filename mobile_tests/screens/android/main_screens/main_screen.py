from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.android.system_popup_screen import SystemPopUpScreen
from mobile_tests.screens.base.main_screens.main_screen import BaseMainScreen


class MainScreen(BaseMainScreen):

    def __init__(self):
        super().__init__(MobileBy.ID, 'buttonBurgerMenu')

    @property
    def _btn_menu(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'buttonBurgerMenu', "Menu")

    def _btn_menu_item(self, key) -> MobileButton:
        return MobileButton(MobileBy.XPATH, '//android.widget.TextView[@text="{}"]', key, key)

    def _btn_screen(self, key) -> MobileButton:
        return MobileButton(MobileBy.XPATH, '//*[contains(@resource-id, "smallLabel")][@text="{}"]', key, key)

    @property
    def _btn_english(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'englishRadioButton', 'English')

    @property
    def _btn_arabic(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'arabicRadioButton', 'Arabic')

    @property
    def _btn_language(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'rrl_language', "Language")

    def select_language(self, language):
        SystemPopUpScreen().decline()
        super().select_language(language)
