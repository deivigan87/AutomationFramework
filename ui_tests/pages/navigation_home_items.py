from enum import Enum

from d14_base.data_reader import DataReader


class NavigationHomeItems(Enum):
    HOME_SEARCH = DataReader().get_test_data("Navigation Items.home search")
    DEED_TRANSFER = DataReader().get_test_data("Navigation Items.deed transfer")
    FINANCING = DataReader().get_test_data("Navigation Items.get home financing")
    MANAGE_MY_PROPERTY = DataReader().get_test_data("Navigation Items.manage my property")
    VIEW_READY_MADE_DESIGNS = DataReader().get_test_data("Navigation Items.view ready made design")
    CHECK_ELIGIBILITY = DataReader().get_test_data("Navigation Items.check eligibility")
    CALCULATE_LOAN_AMOUNT = DataReader().get_test_data("Navigation Items.calculate loan amount")
    ESTIMATE_HOME_SIZE = DataReader().get_test_data("Navigation Items.estimate home size")
    QASEMATI = DataReader().get_test_data("Navigation Items.qasemati")
    PROTECT_MY_PROPERTY = DataReader().get_test_data("Navigation Items.protect my property")
