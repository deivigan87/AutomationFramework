from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.my_subscriptions_screen \
    import BaseMySubscriptionsScreen


class MySubscriptionsScreen(BaseMySubscriptionsScreen):

    def __init__(self):
        super().__init__(MobileBy.ID, "subscriptionsListScrollView")

    @property
    def _btn_add_subscription(self) -> MobileButton:
        return MobileButton(MobileBy.ID, "emptyLayoutAddSubscriptionBtn", "Add Subscriptions")
