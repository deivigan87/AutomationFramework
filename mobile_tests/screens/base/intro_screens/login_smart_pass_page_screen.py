from abc import ABC, abstractmethod

from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.text_field import MobileTextbox
from d14_mobile_framework.framework.screens.base_screen import BaseScreen


class BaseLoginSmartPassPageScreen(ABC, BaseScreen):

    def __init__(self, locator_type: MobileBy, locator: str, locale: str = None):
        super().__init__(locator_type, locator, locale)

    @property
    @abstractmethod
    def _txb_username(self) -> MobileTextbox:
        pass

    @property
    @abstractmethod
    def _txb_password(self) -> MobileTextbox:
        pass

    @property
    @abstractmethod
    def _btn_sign_in(self) -> MobileButton:
        pass

    def authorize_smart_pass(self, login, password):
        self._txb_username.set_text(login)
        self._txb_password.set_text(password)
        self._btn_sign_in.tap()
