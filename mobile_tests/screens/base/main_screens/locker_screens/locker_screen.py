from abc import ABC, abstractmethod

from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.screens.base_screen import BaseScreen


class BaseLockerScreen(ABC, BaseScreen):

    def __init__(self, locator_type: MobileBy, locator: str, locale: str = None):
        super().__init__(locator_type, locator, locale)

    class Item:
        MY_PAYMENTS = "Locker Screen.my_payments"
        MY_SUBSCRIPTIONS = "Locker Screen.my_subscriptions"
        MY_DOCUMENTS = "Locker Screen.my_documents"
        MY_EVENTS = "Locker Screen.my_events"
        MY_SUPPORT = "Locker Screen.my_support"

    @abstractmethod
    def _btn_item(self, key) -> MobileButton:
        pass

    def tap_item(self, item: Item):
        self._btn_item(item).tap()
