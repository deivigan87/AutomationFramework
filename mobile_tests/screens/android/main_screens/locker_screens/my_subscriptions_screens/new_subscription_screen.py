from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.new_subscription_screen \
    import BaseNewSubscriptionScreen


class NewSubscriptionScreen(BaseNewSubscriptionScreen):

    def __init__(self):
        super().__init__(MobileBy.ID, "selectNewSubscriptionLayout")

    def _btn_subscription(self, key) -> MobileButton:
        return MobileButton(MobileBy.XPATH, '//*[contains(@resource-id, "packages_layout")]//*[contains(@text, "{}")]',
                            key, key)
