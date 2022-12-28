import csv
import os

import allure
import numpy
from datetime import datetime
import pytest
from allure_commons.model2 import TestResult

from d14_base.excel.excel_util import ExcelUtil
from d14_base.excel.perf_actions import PerfExcelActions
from d14_service_framework.utils.api_library import ApiMethods

from d14_base.html_allure_report_listener import AllureListener

from service_tests.test_data_configuration.test_data_config_parser import ConfigParser
from service_tests.test_suite import config

from d14_base.string_util import StringUtil
from d14_service_framework.utils.api_helper import ApiHelper


@pytest.fixture(scope="session")
def api_helper():
    config_parser = ConfigParser(config.APPLICATION_NAME, config.SERVICE_ENV, config.PROTOCOL)
    yield ApiHelper(config_parser)


@pytest.fixture(scope='function', autouse=True)
def allure_naming():
    """Using name of method as name of test in allure-report"""
    yield
    if AllureListener.get_allure_listener():
        test_result = AllureListener.get_allure_listener().get_last_item(TestResult)
        test_result.name = StringUtil.get_method_name_for_allure_report(test_result.name)
        if test_result.status == 'passed':
            test_result.description = "Environment: {}<br/><br/>Test Name: {}<br/>Test Description: {}<br/><br/>" \
                                      "Status of test: {} (200 OK)<br/>".format(config.SERVICE_ENV, test_result.name,
                                                                                test_result.description,
                                                                                test_result.status)
        else:
            test_result.description = "Environment: {}<br/><br/>Test Name: {}<br/>Test Description: {}<br/><br/>" \
                                      "Status of test: {}<br/>Status Details: {}<br/>".format(config.SERVICE_ENV,
                                                                                              test_result.name,
                                                                                              test_result.description,
                                                                                              test_result.status,
                                                                                              test_result.statusDetails.
                                                                                              message)


@pytest.fixture(scope='session', autouse=True)
def parse_response_time():
    yield
    csv_data = [("timestamp", "url", "response_time")]
    responses = ApiMethods.get_responses_times()
    for method in responses:
        for url in responses[method]:
            for idx, times in enumerate(responses[method][url]):
                date = times[1].strftime("%Y-%m-%d %H:%M:%S.%f")
                csv_data.append((date, url.split("/")[-1], numpy.round(times[0], 2)))
                responses[method][url][idx] = times[0]
    with allure.step("Actions with CSV"):
        with open("./responses.csv", 'w', newline='') as csv_file:
            wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for row in csv_data:
                wr.writerow(row)

    with allure.step("Actions with Excel"):
        actions_with_excel_file(responses)


def actions_with_excel_file(responses_dict):
    with allure.step("Precondition for starting to work with Excel"):
        file_excel_path = os.path.join(config.EXCEL_PATH, "responses-{}.xlsx".format(datetime.date(datetime.now())))
        ExcelUtil.delete_files(config.EXCEL_PATH, 'xlsx')
        ExcelUtil.create_file(file_excel_path)
        name_of_excel_sheet = "Responses"
        ExcelUtil.add_sheet_to_file(file_excel_path, name_of_excel_sheet)

    with allure.step("Fill hat of Excel document"):
        precondition_data = ["Number",
                             "Endpoint",
                             "Avg {} run(s), sec".format(len(list(responses_dict['post'].values())[0])),
                             "Avg {} run(s), ms".format(len(list(responses_dict['post'].values())[0])),
                             "Min ms",
                             "Max ms"]
        column_names = ['A', 'B', 'C', 'D', 'E', 'F']
        ExcelUtil.add_data_to_columns_in_one_raw(file_path=file_excel_path, name_of_sheet=name_of_excel_sheet,
                                                 default_raw=1, data=precondition_data,
                                                 column_names=column_names)

    with allure.step("Bold text in the hat"):
        for column in column_names:
            ExcelUtil.bold_text(file_path=file_excel_path, name_of_sheet=name_of_excel_sheet,
                                column=column, raw=1)
            ExcelUtil.fill_color_cell(file_path=file_excel_path, column=column, raw=1,
                                      name_of_sheet=name_of_excel_sheet, color='88CCDD')

    with allure.step("Resize the width for columns"):
        ExcelUtil.auto_resize_column(file_excel_path, name_of_excel_sheet)
        ExcelUtil.resize_column(file_excel_path, name_of_excel_sheet, column_number=2, column_width=100)
        ExcelUtil.resize_column(file_excel_path, name_of_excel_sheet, column_number=3, column_width=20)
        ExcelUtil.resize_column(file_excel_path, name_of_excel_sheet, column_number=4, column_width=20)

    with allure.step("Fill info about microservices to Excel"):
        raw_number = 2
        service_number = 1
        for method in responses_dict:
            for url in responses_dict[method]:
                times = sorted(responses_dict[method][url])
                data_raw = [service_number, url, numpy.round(numpy.mean(times) / 1000, 2),
                            numpy.round(numpy.mean(times), 2), numpy.round(times[0], 2), numpy.round(times[-1], 2)]
                ExcelUtil.add_data_to_columns_in_one_raw(file_path=file_excel_path,
                                                         name_of_sheet=name_of_excel_sheet,
                                                         default_raw=raw_number,
                                                         data=data_raw, column_names=column_names,
                                                         additional_method=lambda:
                                                         PerfExcelActions.perf_microservices_actions_with_cells(
                                                             name_of_sheet=name_of_excel_sheet,
                                                             file_path=file_excel_path,
                                                             default_raw=raw_number, data=data_raw,
                                                             column_names=column_names)
                                                         )
                ExcelUtil.add_alignment_style(default_raw=raw_number, file_path=file_excel_path,
                                              name_of_sheet=name_of_excel_sheet, column="B", alignment_style="left")
                service_number += 1
                raw_number += 1
