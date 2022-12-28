import allure
import pytest

from d14_service_framework.utils.json_parser import JsonParser
from hamcrest import assert_that, equal_to

from d14_service_framework.utils.api_library import Status


@allure.feature('Buy_a_home')
@allure.story("BUILD")
class TestBuildRegression(object):
    """Test cases related to Build features"""

    @pytest.mark.regression
    @pytest.mark.TC('T1')
    def test_content_disclaimer(self, api_helper):

        headers = api_helper.config_parser().build_headers("build_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_request("ContentDisclaimer",
                                                                               "ADHA",
                                                                               "getContentDisclaimer",
                                                                               headers=headers)
        assert_that(resp_code, equal_to(Status.SUCCESS), "The response code isn't equal the expected code")
        assert JsonParser.validate_response('ADHA', 'getContentDisclaimer', resp_body), \
            "The response code isn't equal the expected code"

    @pytest.mark.regression
    @pytest.mark.TC('T2')
    def test_calculate(self, api_helper):

        headers = api_helper.config_parser().build_headers("build_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_request("Calculate",
                                                                               "ADHA",
                                                                               "getCalculate",
                                                                               headers=headers)
        assert_that(resp_code, equal_to(Status.SUCCESS), "The response code isn't equal the expected code")
        assert JsonParser.validate_response('ADHA', 'getCalculate', resp_body), \
            "The response code isn't equal the expected code"

    @pytest.mark.regression
    @pytest.mark.TC('T3')
    def test_loan_calculator(self, api_helper):

        headers = api_helper.config_parser().build_headers("build_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_request("LoanCalculator",
                                                                               "ADHA",
                                                                               "loanCalculator",
                                                                               headers=headers)
        assert_that(resp_code, equal_to(Status.SUCCESS), "The response code isn't equal the expected code")
        assert JsonParser.validate_response('ADHA', 'loanCalculator', resp_body), \
            "The response code isn't equal the expected code"

    @pytest.mark.regression
    @pytest.mark.TC('T4')
    def test_mustasharak_general_text(self, api_helper):

        headers = api_helper.config_parser().build_headers("build_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_request("GeneralText",
                                                                               "ADHA",
                                                                               "generalText",
                                                                               headers=headers)
        assert_that(resp_code, equal_to(Status.SUCCESS), "The response code isn't equal the expected code")
        assert JsonParser.validate_response('ADHA', 'generalText', resp_body), \
            "The response code isn't equal the expected code"

    @pytest.mark.regression
    @pytest.mark.TC('T5')
    def test_questionnaire(self, api_helper):

        headers = api_helper.config_parser().build_headers("build_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_request("Questionnaire",
                                                                               "ADHA",
                                                                               "questionnaire",
                                                                               headers=headers)
        assert_that(resp_code, equal_to(Status.SUCCESS), "The response code isn't equal the expected code")
        assert JsonParser.validate_response('ADHA', 'questionnaire', resp_body), \
            "The response code isn't equal the expected code"

    @pytest.mark.regression
    @pytest.mark.TC('T6')
    def test_bayti_designs(self, api_helper):

        headers = api_helper.config_parser().build_headers("build_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_request("Bayti",
                                                                               "ADHA",
                                                                               "baytiDesigns",
                                                                               headers=headers)
        assert_that(resp_code, equal_to(Status.SUCCESS), "The response code isn't equal the expected code")
        assert JsonParser.validate_response('ADHA', 'baytiDesigns', resp_body), \
            "The response code isn't equal the expected code"
