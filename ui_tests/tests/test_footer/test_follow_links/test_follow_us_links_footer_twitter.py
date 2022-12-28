import allure
import pytest
import requests
from hamcrest import assert_that

from d14_base.data_reader import DataReader
from d14_ui_framework.browser.browser import Browser
from d14_ui_service_tests_templates.ui_tests.pages.footer.footer import Footer


class TestFollowUsLinks:
    """Buy: Footer links under section follow us works correct: BUAH-6801"""

    data = [("twitter", "twitter_mob")]

    @pytest.mark.TC("T5145")
    @pytest.mark.parametrize("page, mobile", data)
    @pytest.mark.smoke
    @pytest.mark.prod_health_check
    def test_follow_us_footer_twitter(self, page, mobile):
        with allure.step("Click {} link on footer".format(page)):
            Footer().click_follow_us_btn(page)

        with allure.step("Verify {} url is opened".format(page)):
            actual_url = Browser.get_url()
            link_key = page
            if Browser.is_mobile() and mobile:
                link_key = mobile
            assert_that(DataReader().get_test_data("Footer links.{}".format(link_key)) in actual_url,
                        "Opened page with another url: {}".format(actual_url))
            assert_that(requests.get(actual_url).status_code == 200, "Status Code answer is bad")
