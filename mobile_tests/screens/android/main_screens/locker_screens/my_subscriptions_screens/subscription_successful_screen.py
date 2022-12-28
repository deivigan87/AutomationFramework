from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.subscription_successful_screen \
    import BaseSubscriptionSuccessfulScreen


class SubscriptionSuccessfulScreen(BaseSubscriptionSuccessfulScreen):

    def __init__(self):
        super().__init__(MobileBy.ID, 'successfulStatusIcon')

    @property
    def _btn_ok(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'subscriptionStatusOkButton', 'OK')
