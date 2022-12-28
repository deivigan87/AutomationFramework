from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.element_types import ElementType
from d14_mobile_framework.framework.elements.label import MobileLabel
from d14_mobile_framework.framework.elements.list_of_elements import MobileListOfElements
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.packages_screen \
    import BasePackagesScreen


class PackagesScreen(BasePackagesScreen):

    def __init__(self):
        super().__init__(MobileBy.ID, 'subscriptionsItemsLayout')

    @property
    def _list_packages(self) -> MobileListOfElements[ElementType.MOBILE_BUTTON]:
        return MobileListOfElements(ElementType.MOBILE_BUTTON, MobileBy.XPATH, "//android.widget.RelativeLayout"
                                    "/android.widget.ImageView[not(contains(@resource-id, 'selectImageView'))]",
                                    "Packages")

    def _selected_package(self, index: int) -> MobileLabel:
        return MobileLabel(MobileBy.XPATH, "//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[{}]"
                                           "//*[contains(@resource-id, 'selectImageView')]".format(index + 1),
                           "Selected package")

    @property
    def _btn_next(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'nextButton', "Next")
