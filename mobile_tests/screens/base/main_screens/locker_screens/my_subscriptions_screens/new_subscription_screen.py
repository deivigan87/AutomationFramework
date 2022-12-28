from abc import ABC, abstractmethod

from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.screens.base_screen import BaseScreen


class BaseNewSubscriptionScreen(ABC, BaseScreen):

    def __init__(self, locator_type: MobileBy, locator: str, locale: str = None):
        super().__init__(locator_type, locator, locale)

    class Subscription:
        ETISALAT_ELIFE = "New Subscription Screen.etisalat_elife"
        MAWAQIF = "New Subscription Screen.mawaqif"

    @abstractmethod
    def _btn_subscription(self, key) -> MobileButton:
        pass

    def tap_subscription(self, subscription: Subscription):
        self._btn_subscription(subscription).tap()
