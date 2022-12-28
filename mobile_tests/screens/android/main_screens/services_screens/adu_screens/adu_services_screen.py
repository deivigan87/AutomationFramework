from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.text_field import MobileTextbox

from mobile_tests.screens.base.main_screens.services_screens.adu_screens.adu_services_screen import \
    BaseAduServicesScreen


class AduServicesScreen(BaseAduServicesScreen):

    def __init__(self):
        super().__init__(MobileBy.ID, 'abudhabi.tamm.stage:id/ll_app_bar')

    @property
    def _txb_search_field(self) -> MobileTextbox:
        return MobileTextbox(MobileBy.ID, "tv_search", "Search Service field")
