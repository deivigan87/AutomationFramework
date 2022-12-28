import random

import pytest
from hamcrest import assert_that, equal_to

from d14_service_framework.utils.api_library import Status
from d14_service_framework.utils.json_parser import JsonParser
from d14_service_framework.utils.validation_util import ValidationUtil
from service_tests.test_data_configuration.test_data_config_parser import ConfigParser
from service_tests.test_suite import config


class TestValidationBuah(object):
    """Test cases related to ADDC"""
    validation_util = ValidationUtil(ConfigParser, config)

    def test_get_application_response(self, api_helper):
        """Test GetApplicationResponse: BUAH-3290"""

        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_request("GetApplicationResponse",
                                                                               "ADDCNotificationService",
                                                                               "getApplicationResponse",
                                                                               headers=headers)
        assert JsonParser.validate_response('ADDCNotificationService', 'GetApplicationResponse', resp_body), \
            "The response code isn't equal the expected code"
        self.validation_util.get_validation_data("getApplicationResponse", resp_body, "buah_validation")

    def test_to_chk_get_owner_id_by_owner_idn(self, api_helper):
        """Test getOwnerIdByOwnerIDN: BUAH-1630"""
        national_id = random.randint(14 ** 15, 14 ** 16 - 1)
        resp_code, resp_body, resp_time, resp_header = api_helper.post_request("GetOwnerIdByOwnerIDN",
                                                                               "TAMMOwnerProfile",
                                                                               "getOwnerIdByOwnerIDN",
                                                                               args=national_id)
        assert_that(resp_code, equal_to(Status.SUCCESS), "The response code isn't equal the expected code")
        self.validation_util.get_validation_data("getOwnerIdByOwnerIDN", resp_body, "buah_validation")

    @pytest.mark.parametrize("plot_id", [
        446942])
    def test_get_commit_service_buy_and_sell(self, plot_id, api_helper):

        resp_code, resp_body, resp_time, resp_header = api_helper.post_request("GetUnitOwnershipDeed",
                                                                               "TAMMPropertyProfileService",
                                                                               "getUnitOwnershipDeedBAv03",
                                                                               args=plot_id)
        assert_that(resp_code, equal_to(Status.SUCCESS), "The response code isn't equal the expected code")
        owner_id = JsonParser.get_value_from_dict(resp_body, ['GetUnitOwnershipDeedResponse',
                                                              'GetUnitOwnershipDeedResult',
                                                              'UnitOwnershipDeed', 'OwnershipDeedShareDetailsList',
                                                              'OwnershipDeedShareDetails',
                                                              'OwnerId'])
        requester_id = owner_id

        plot_owner_share_id = JsonParser.get_value_from_dict(resp_body, ['GetUnitOwnershipDeedResponse',
                                                                         'GetUnitOwnershipDeedResult',
                                                                         'UnitOwnershipDeed',
                                                                         'OwnershipDeedShareDetailsList',
                                                                         'OwnershipDeedShareDetails',
                                                                         'PlotOwnerShareId'])

        transaction_amount = 3477600
        is_with_mortgage = "true"
        mortgage_details_issue_date_initiate = "2019-02-20"
        mortgage_details_mortgage_amount_initiate = "5000"
        mortgage_details_athorized_bank_employee_id_initiate = "2"
        mortgage_details_mortgage_type_initiate = "1"
        mortgage_details_degree_initiate = "1"
        resp_code, resp_body, resp_time, resp_header = \
            api_helper.post_request("InitiateService", "IntegratedServices",
                                    "getInitiateServiceBuyAndSellUnitServiceMortgage",
                                    args=(plot_id, transaction_amount, owner_id, plot_owner_share_id, is_with_mortgage,
                                          mortgage_details_issue_date_initiate,
                                          mortgage_details_mortgage_amount_initiate,
                                          mortgage_details_athorized_bank_employee_id_initiate,
                                          mortgage_details_mortgage_type_initiate, mortgage_details_degree_initiate,
                                          requester_id))
        assert_that(resp_code, equal_to(Status.SUCCESS), "The response code isn't equal the expected code")
        application_id_buy_and_sell = JsonParser.get_value_from_dict(resp_body, ['InitiateServiceResponse',
                                                                                 'InitiateServiceResult',
                                                                                 'ApplicationId'])

        resp_code, resp_body, resp_time, resp_header = api_helper.post_request("CommitService",
                                                                               "IntegratedServices",
                                                                               "getCommitServiceBuyAndSell",
                                                                               args=application_id_buy_and_sell)

        assert_that(resp_code, equal_to(Status.SUCCESS), "The response code isn't equal the expected code")
        self.validation_util.get_validation_data("getCommitServiceBuyAndSell", resp_body, "buah_validation", 0, 1)
