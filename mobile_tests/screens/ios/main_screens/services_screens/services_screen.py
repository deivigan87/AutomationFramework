from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.element_types import ElementType
from d14_mobile_framework.framework.elements.list_of_elements import MobileListOfElements
from d14_mobile_framework.framework.elements.text_field import MobileTextbox

from mobile_tests.screens.base.main_screens.services_screens.services_screen import BaseServicesScreen


class ServicesScreen(BaseServicesScreen):

    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, 'abudhabi.tamm.stage:id/ll_app_bar')

    @property
    def _btn_more(self) -> MobileButton:
        return MobileButton(MobileBy.ACCESSIBILITY_ID, '{}', 'More', "Services Screen.show_more")

    def _btn_adu(self, key) -> MobileButton:
        return MobileButton(MobileBy.XPATH, f'//XCUIElementTypeStaticText[@label="{key}"]', key)

    def _btn_journey(self, key) -> MobileButton:
        return MobileButton(MobileBy.NAME, '{}', key, key)

    def _btn_service(self, key) -> MobileButton:
        return MobileButton(MobileBy.XPATH, f'//XCUIElementTypeStaticText[@value="{key}"]', key)

    def _btn_tab(self, key) -> MobileButton:
        return MobileButton(MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="{}"])[2]', key, key)

    @property
    def _txb_search_field(self) -> MobileTextbox:
        return MobileTextbox(MobileBy.ACCESSIBILITY_ID, "searchTitle", "Search Service field")

    @property
    def _txb_search_field_input(self) -> MobileTextbox:
        return MobileTextbox(MobileBy.XPATH,
                             "//XCUIElementTypeImage[@name='{}']/following-sibling::XCUIElementTypeTextField",
                             "Search Service field where need to input text", "Services Screen.search")

    @property
    def _btn_filter_services_tab(self) -> MobileButton:
        return MobileButton(MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="\'"]',
                            'Filter button on Services Tab')

    def _lst_adu(self) -> MobileListOfElements[ElementType.MOBILE_LABEL]:
        return MobileListOfElements(ElementType.MOBILE_LABEL, MobileBy.XPATH, '//XCUIElementTypeCell', "Journeys")

    def _lst_journeys(self) -> MobileListOfElements[ElementType.MOBILE_LABEL]:
        return MobileListOfElements(ElementType.MOBILE_LABEL, MobileBy.XPATH, '//XCUIElementTypeCell', "Journeys")

    def _lst_services(self) -> MobileListOfElements[ElementType.MOBILE_LABEL]:
        return MobileListOfElements(ElementType.MOBILE_LABEL, MobileBy.XPATH, '//XCUIElementTypeCell', "Services")

    def click_search_field(self):
        self._txb_search_field.tap_via_coordinates()

    def search_service(self, service):
        self._txb_search_field_input.set_text(service + "\n")
