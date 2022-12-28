from abc import ABC, abstractmethod

from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.screens.base_screen import BaseScreen


class BaseLoginScreen(ABC, BaseScreen):

    def __init__(self, locator_type: MobileBy, locator: str, locale: str = None):
        super().__init__(locator_type, locator, locale)

    class LoginType:
        UAE_PASS = "UAE Pass"
        SMART_PASS = "Smart Pass"
        GUEST_USER = "Guest User"

    @property
    @abstractmethod
    def _btn_login_as_guest_user(self) -> MobileButton:
        pass

    @property
    @abstractmethod
    def _btn_smart_pass(self) -> MobileButton:
        pass

    @property
    @abstractmethod
    def _btn_uae_pass(self) -> MobileButton:
        pass

    def select_authorization_type(self, login_type: LoginType):
        if login_type == self.LoginType.SMART_PASS:
            self._btn_smart_pass.tap()
        elif login_type == self.LoginType.GUEST_USER:
            self._btn_login_as_guest_user.tap()
        else:
            self._btn_uae_pass.tap()
