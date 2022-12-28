from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.element_types import ElementType
from d14_mobile_framework.framework.elements.list_of_elements import MobileListOfElements
from d14_mobile_framework.framework.elements.text_field import MobileTextbox

from mobile_tests.screens.base.main_screens.services_screens.services_screen import BaseServicesScreen


class ServicesScreen(BaseServicesScreen):

    def __init__(self):
        super().__init__(MobileBy.ID, 'rv')

    @property
    def _btn_more(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'buttonLoadMoreNews', 'More')

    def _btn_adu(self, key) -> MobileButton:
        return MobileButton(MobileBy.XPATH, f'//*[contains(@resource-id, "abudhabi.tamm.stage:id/tv_title")'
                                            f'and (@text="{key}")]', key)

    def _btn_journey(self, key) -> MobileButton:
        return MobileButton(MobileBy.XPATH, '//*[contains(@resource-id, "rv")]'
                                            '/android.widget.LinearLayout//*[@text="{}"]', key, key)

    def _btn_service(self, key) -> MobileButton:
        return MobileButton(MobileBy.XPATH, f'//*[contains(@resource-id, "tv_title") and '
                                            f'contains(normalize-space(@text),"{key}")]', key)

    def _btn_tab(self, key) -> MobileButton:
        return MobileButton(MobileBy.XPATH, "//android.support.v7.app.ActionBar.Tab"
                                            "//android.widget.TextView[@text='{}']", key, key)

    @property
    def _txb_search_field(self) -> MobileTextbox:
        return MobileTextbox(MobileBy.ID, "tammEditTextSearch", "Search Service field")

    @property
    def _txb_search_field_input(self) -> MobileTextbox:
        return MobileTextbox(MobileBy.ID, "edt_search", "Search Service field where need to input text")

    @property
    def _btn_filter_services_tab(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'serviceFilterBtn', 'Filter button on Services Tab')

    def _lst_adu(self) -> MobileListOfElements[ElementType.MOBILE_LABEL]:
        return MobileListOfElements(ElementType.MOBILE_LABEL, MobileBy.XPATH,
                                    '//*[contains(@resource-id, "abudhabi.tamm.stage:id/tv_title")]',
                                    "Adu(s)")

    def _lst_journeys(self) -> MobileListOfElements[ElementType.MOBILE_LABEL]:
        return MobileListOfElements(ElementType.MOBILE_LABEL, MobileBy.XPATH,
                                    '//*[contains(@resource-id, "rv")]/android.widget.LinearLayout',
                                    "Journeys")

    def _lst_services(self) -> MobileListOfElements[ElementType.MOBILE_LABEL]:
        return MobileListOfElements(ElementType.MOBILE_LABEL, MobileBy.XPATH,
                                    '//*[contains(@resource-id, "rv")]//android.widget.LinearLayout',
                                    "Services")
