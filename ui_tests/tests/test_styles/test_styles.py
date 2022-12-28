import pytest
import allure
from hamcrest import assert_that

from d14_ui_framework.browser.browser import Browser
from d14_ui_service_tests_templates.ui_tests.pages.digital_services_page.digital_second_services_page import \
    DigitalSecondServicesPage
from d14_ui_service_tests_templates.ui_tests.pages.digital_services_page.digital_services_page import \
    DigitalServicesPage


class TestStyles:
    """Test Styles: font, font_size, color: """

    @pytest.mark.regression
    @pytest.mark.guest_user
    def test_styles(self):
        with allure.step("Set URL"):
            Browser.set_url(
                "https://stage.tamm.abudhabi/en/tamm-centers-services/department-of-municipalities-and-transport")

        with allure.step("Check that page for example is opened"):
            digital_services_page = DigitalServicesPage()
            assert_that(digital_services_page.is_opened(), "Page is not opened")

        with allure.step("Check that page for example is opened"):
            digital_second_services_page = DigitalSecondServicesPage()
            assert_that(digital_second_services_page.is_opened(), "Page is not opened")
