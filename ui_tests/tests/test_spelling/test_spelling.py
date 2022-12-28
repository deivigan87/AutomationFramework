import allure
import pytest

from d14_ui_framework.browser.browser import Browser
from d14_ui_framework.utils.spelling_util import SpellingUtil

from ui_tests.pages.tamm_portal.services_page import ServicesPage

IGNORE_WORDS = ['عربي', 'smartpass']


class TestCancelElectricityGeneration:
    """Test Validate Summary page link for cancel Electricity generation:    SMDOE-T275"""

    @pytest.mark.TC("T5145")
    @pytest.mark.smoke
    def test_spelling(self):
        with allure.step("Check spelling on \"Service\" page"):
            Browser.set_url("https://stage.tamm.abudhabi/en/tamm-centers-services/department-of-energy")
            services_page = ServicesPage()
            services_page.wait_page_to_load()
            services_page.change_language_to_ar()
            SpellingUtil.steps_for_checking_of_spelling(services_page, services_page.lbl_letters, IGNORE_WORDS)
