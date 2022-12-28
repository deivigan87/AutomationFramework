from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.package_details_screen \
    import BasePackageDetailsScreen


class PackageDetailsScreen(BasePackageDetailsScreen):

    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, '{}', "Package Details Screen.select_package")

    @property
    def _btn_select_package(self) -> MobileButton:
        return MobileButton(MobileBy.ACCESSIBILITY_ID, '{}', 'Select package', "Package Details Screen.select_package")
