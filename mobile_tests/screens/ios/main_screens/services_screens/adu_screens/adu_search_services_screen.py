from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.element_types import ElementType
from d14_mobile_framework.framework.elements.list_of_elements import MobileListOfElements
from mobile_tests.screens.base.main_screens.services_screens.adu_screens.adu_search_services_screen import \
    BaseAduSearchServicesScreen


class AduSearchServicesScreen(BaseAduSearchServicesScreen):

    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, 'subCategoryTableView')

    def _btn_service(self, key) -> MobileButton:
        return MobileButton(MobileBy.XPATH, '//XCUIElementTypeStaticText[@value="{}"]', key, key)

    def _lst_services(self) -> MobileListOfElements[ElementType.MOBILE_LABEL]:
        return MobileListOfElements(ElementType.MOBILE_LABEL, MobileBy.XPATH, '//XCUIElementTypeCell', "Services")
