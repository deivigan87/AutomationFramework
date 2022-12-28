from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.my_subscriptions_screen \
    import BaseMySubscriptionsScreen
from mobile_tests.screens.ios.spinner_screen import SpinnerScreen


class MySubscriptionsScreen(BaseMySubscriptionsScreen):

    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, "{}", "My Subscriptions Screen.add_subscription")

    @property
    def _btn_add_subscription(self) -> MobileButton:
        return MobileButton(MobileBy.ACCESSIBILITY_ID, "{}", "Add Subscription",
                            "My Subscriptions Screen.add_subscription")

    def tap_add_subscription(self):
        SpinnerScreen().wait_for_is_closed()
        self._btn_add_subscription.tap()
