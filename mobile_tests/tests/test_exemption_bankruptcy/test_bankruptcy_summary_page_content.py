import pytest
from d14_base.data_reader import DataReader
from mobile_tests.steps.service_navigation_steps import ServiceNavigationSteps


class TestBankruptcySummaryPageContent:
    """Test Validate Summary Page for Bankruptcy:   SMA-77"""

    @pytest.mark.smoke
    def test_bankruptcy_summary_page_content(self, screen):
        ServiceNavigationSteps.go_to_service(send_service=DataReader().get_from_locale("Services Screen.bill_payment"),
                                             tap_service=DataReader().get_from_locale("Services Screen.bill_payment"),
                                             login=DataReader().get_env_data("bill_payment.eligible_user2"),
                                             password=DataReader().get_env_data("bill_payment.eligible_pass2"),
                                             emirates_id=DataReader().get_env_data("UaePassCredentials.emirates_id"),
                                             uae_pass=True,
                                             adu_name=DataReader().get_from_locale("ADU.housing_and_property"),
                                             group_of_services=DataReader().
                                             get_from_locale("ADU Search Services Screen.utilities_and_maintenance"),
                                             go_via_adu_items=True,
                                             switch_to_web_view=False)

        """
        After this precondition need to past code with steps from UI tests.

        Examples:

        with allure.step("Verify Login Description"):
            bankruptcy_summary_page = BankruptcySummaryPage()
            SoftAssert.soft_assert(bankruptcy_summary_page.is_login_description_displayed(), "Login Description is "
                                                                                             "not displayed")

        with allure.step("Verify Service Description"):
            SoftAssert.soft_assert(bankruptcy_summary_page.is_service_description_displayed(), "Service Description "
                                                                                               "is not displayed")
        with allure.step("Verify Required Document 1"):
            SoftAssert.soft_assert(bankruptcy_summary_page.is_required_document1_displayed(), "Required Document 1 is "
                                                                                              "not displayed")
        with allure.step("Verify Required Document 2"):
            SoftAssert.soft_assert(bankruptcy_summary_page.is_required_document2_displayed(), "Required Document 2 is "
                                                                                              "not displayed")
        with allure.step("Verify Fees Description"):
            SoftAssert.soft_assert(bankruptcy_summary_page.is_fees_description_displayed(), "Fees Description is not  "
                                                                                            "displayed")
        with allure.step("Verify Fees Price"):
            SoftAssert.soft_assert(bankruptcy_summary_page.is_fees_price_displayed(), "Fees Description is not  "
                                                                                      "displayed")
        """
