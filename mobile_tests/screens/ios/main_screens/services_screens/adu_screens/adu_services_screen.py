from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.text_field import MobileTextbox

from mobile_tests.screens.base.main_screens.services_screens.adu_screens.adu_services_screen import \
    BaseAduServicesScreen


class AduServicesScreen(BaseAduServicesScreen):

    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, 'serviceListTableView')

    @property
    def _txb_search_field(self) -> MobileTextbox:
        return MobileTextbox(MobileBy.ACCESSIBILITY_ID, "searchTitle", "Search Service field")

    def click_search_field(self):
        self.wait_for_is_opened()
        self._txb_search_field.tap_via_coordinates()
