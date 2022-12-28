import random

import logging

import allure
import pytest
from hamcrest import assert_that, equal_to

from d14_service_framework.utils.api_library import Status
from d14_service_framework.utils.json_parser import JsonParser


@allure.feature('Buy_a_home')
@allure.story("ADM")
class TestAdmBuah(object):
    """Test cases related to test_ADM"""

    @pytest.mark.health_check
    def test_get_online_user_verification_status(self, api_helper):
        """Test getOnlineUserVerificationStatus: BUAH-1629"""

        national_id = random.randint(14 ** 15, 14 ** 16 - 1)
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper. \
            post_request("GetOnlineUserVerificationStatus", "TAMMOwnerProfile", "getOnlineUserVerificationStatus",
                         headers=headers, args=national_id)
        assert_that(resp_code, equal_to(Status.SUCCESS), "The response code isn't equal the expected code")

    @pytest.mark.health_check
    def test_verification_process(self, api_helper):
        """Test InitiateService, CommitService, GetServiceDetails, getOwnerIdByOwnerIDN: BUAH-1822"""

        logging.info('Send request to InitiateService')
        national_id = random.randint(14 ** 15, 14 ** 16 - 1)
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_request("InitiateService", "IntegratedServices",
                                                                               "getInitiateService",
                                                                               headers=headers, args=national_id)
        assert_that(resp_code, equal_to(Status.SUCCESS), "The response code isn't equal the expected code")
        application_id = JsonParser.get_value_from_dict(resp_body, ['data', 'applicationId'])

        logging.info('Send request to InitiateService - BuyAndSellUnitService')
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = \
            api_helper.post_request("InitiateService", "IntegratedServices", "getInitiateServiceBuyAndSellUnitService",
                                    headers=headers)
        assert_that(resp_code, equal_to(Status.SUCCESS), "The response code isn't equal the expected code")
        application_id_buy_and_sell = JsonParser.get_value_from_dict(resp_body, ['data', 'applicationId'])

        logging.info('Send request to CommitService')
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_request("CommitService", "IntegratedServices",
                                                                               "getCommitService",
                                                                               headers=headers,
                                                                               args=application_id)
        assert_that(resp_code, equal_to(Status.SUCCESS), "The response code isn't equal the expected code")

        logging.info('Send request to CommitService - Buy and Sell')
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_request("CommitService", "IntegratedServices",
                                                                               "getCommitServiceBuyAndSell",
                                                                               headers=headers,
                                                                               args=application_id_buy_and_sell)
        assert_that(resp_code, equal_to(Status.SUCCESS), "The response code isn't equal the expected code")

        logging.info('Send request to GetServiceDetails')
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_request("GetServiceDetails",
                                                                               "IntegratedServices",
                                                                               "getServiceDetails",
                                                                               headers=headers,
                                                                               args=application_id)
        assert_that(resp_code, equal_to(Status.SUCCESS), "The response code isn't equal the expected code")

        logging.info('Send request to GetOnlineUserVerificationStatus')
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper. \
            post_request("GetOnlineUserVerificationStatus", "TAMMOwnerProfile", "getOnlineUserVerificationStatus",
                         headers=headers, args=application_id)
        assert_that(resp_code, equal_to(Status.SUCCESS), "The response code isn't equal the expected code")
