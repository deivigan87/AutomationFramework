from abc import ABC, abstractmethod

from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.text_field import MobileTextbox
from d14_mobile_framework.framework.screens.base_screen import BaseScreen


class BaseLoginUAEPassPageScreen(ABC, BaseScreen):

    def __init__(self, locator_type: MobileBy, locator: str, locale: str = None):
        super().__init__(locator_type, locator, locale)

    @property
    @abstractmethod
    def _btn_uae_pass_test_user(self) -> MobileButton:
        pass

    @property
    @abstractmethod
    def _txb_emirates_id(self) -> MobileTextbox:
        pass

    @property
    @abstractmethod
    def _btn_sign_in(self) -> MobileButton:
        pass

    def authorize_uae_pass(self, emirates_id):
        self._btn_uae_pass_test_user.tap()
        self._txb_emirates_id.set_text(emirates_id)
        self._btn_sign_in.tap()
