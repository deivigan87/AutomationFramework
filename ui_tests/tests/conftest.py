"""Conftest class with common fixtures before and after running test."""
import configparser
import logging
import os
import re
from collections import OrderedDict

import pytest
import allure
from adaptavist import Adaptavist
from allure_commons.model2 import TestResult, Status
from allure_commons.types import AttachmentType
from d14_ui_framework.configuration import config
from d14_base.excel.excel_util import ExcelUtil
from d14_base.api.rp_test_marks_updater import RpTestMarksUpdater
from d14_ui_framework.utils.accessibility_util import AccessibilityUtil
from d14_ui_framework.utils.js_checker_util import JSCheckerUtil
from filelock import FileLock

from selenium.webdriver.common.by import By

from d14_base.data_reader import DataReader
from d14_ui_framework.browser.browser import Browser
from d14_ui_framework.constants import browsers
from d14_ui_framework.constants import desktop_platforms
from d14_base.screenshooter import Screenshooter
from d14_base.soft_assert import SoftAssert
from d14_base.html_allure_report_listener import AllureListener
from d14_base.pytest_cache import PytestCache

from ui_tests.configuration import config as project_config
from d14_base.string_util import StringUtil
from d14_ui_framework.utils.uae_password_device import UAEPasswordDevice
from datetime import datetime

cycle_of_violation_title = 1
__lock = FileLock("Conftest")


@pytest.fixture(scope="function", autouse=True)
def browser(request, prepare_config):
    """
    Fixture for working with browser: open browser before test and close after test.

    Args:
        request: request.
        prepare_config: config: Using config file for each journey.
    """
    params = {}
    try:
        params = OrderedDict(request.node.callspec.params.items())
        del params['__pytest_repeat_step_number']
    except (KeyError, AttributeError):
        pass
    test_id = str(params) + str(request.node.fspath) + re.sub(r'\[.*', '', request.node.name)
    _cloud_session_id = Browser.set_up_driver(test_id=test_id)

    platform_name = Browser.get_platform_name()
    if platform_name in [browsers.BROWSER_CHROME,
                         browsers.BROWSER_FIREFOX, browsers.BROWSER_SAFARI,
                         browsers.BROWSER_IE, browsers.BROWSER_EDGE] or desktop_platforms.\
            WINDOWS in platform_name or desktop_platforms.MAC_OS in platform_name:
        Browser.maximize()
    Browser.set_url(DataReader()._get_env_config()['start_url'])
    tests_failed_before_function = request.session.testsfailed
    platform_info = Browser.get_platform_info()
    device_or_browser_name = \
        platform_info['browser_name'] if not Browser.get_platform_name() in [
            browsers.BROWSER_ANDROID, browsers.BROWSER_IOS] else Browser.device_name
    version_of_browser = \
        platform_info['browser_version'] if not Browser.get_platform_name() in [
            browsers.BROWSER_ANDROID, browsers.BROWSER_IOS] else platform_info['browser_version']
    yield {"tests_failed_before_function": tests_failed_before_function,
           "device_or_browser_name": device_or_browser_name,
           "version_of_browser": version_of_browser,
           "platform_info": platform_info,
           "cloud_session_id": _cloud_session_id}
    Browser.quit()


@pytest.fixture(scope="function", autouse=True)
def screenshot_after_fail(request, browser, rp_logger, create_test_plan_and_cycle_tm4j):
    """
    Fixture for screenshot creation after failed test.

    Args:
        request: request.
        browser: created browser information.
        rp_logger: reportportal logger.
        create_test_plan_and_cycle_tm4j: function for creating test plan and test cycle in TM4J.
    """
    yield
    Screenshooter.set_session_screen_dir()
    if request.session.testsfailed != browser["tests_failed_before_function"] and \
            '--reportportal' in request.config.invocation_params.args and request.config._reportportal_configured:
        try:
            with open(Screenshooter.take_screenshot(Browser.get_driver(),
                                                    custom_name=f"{browser['device_or_browser_name']}_"
                                                                f"{browser['version_of_browser']}"),
                      "rb") as image_file:
                rp_logger.info("Screenshot", attachment={"name": "screenshot.jpg",
                                                         "data": image_file.read(),
                                                         "mime": "image/jpeg"})

        except Exception:
            pass
    if AllureListener.get_allure_listener():
        test_result = AllureListener.get_allure_listener().get_last_item(TestResult)
        test_result.name = StringUtil.get_method_name_for_allure_report(test_result.name)
        if test_result.description is None:
            test_result.description = get_platform_info_allure(browser["platform_info"])
        else:
            test_result.description += "<br/><br/>" + get_platform_info_allure(browser["platform_info"])
        tm4j_tc_id = update_tc_in_tm4j(request, create_test_plan_and_cycle_tm4j, browser["platform_info"],
                                       test_result.statusDetails.message if test_result.status in [
                                           "failed", "broken"] else None)
        if request.session.testsfailed != browser["tests_failed_before_function"]:
            test_result.steps[-1].status = Status.FAILED
            test_result.status = Status.FAILED
            allure.attach.file(Screenshooter.
                               take_screenshot(Browser.get_driver(),
                                               custom_name=f"{browser['device_or_browser_name']}_"
                                                           f"{browser['version_of_browser']}"),
                               'screenshot', AttachmentType.JPG)

            send_screenshot_to_tm4j(tm4j_tc_id, create_test_plan_and_cycle_tm4j, browser["device_or_browser_name"],
                                    browser["version_of_browser"])

            if bool(config.USE_SAUCE_LABS) is True and config.RP_ENDPOINT != '' and config.RP_PROJECT != '' and config.\
                    RP_TOKEN != '':
                # Update markers and connect SauceLabs on the ReportPortal if USE_SAUCE_LABS is True
                __lock.acquire()
                if browser["cloud_session_id"]:
                    try:
                        request.node.add_marker(pytest.mark.SLID(browser["cloud_session_id"][0]))
                        RpTestMarksUpdater.rp_update_test_marks(request,
                                                                config.RP_ENDPOINT.split('=')[1].split('/api')[0],
                                                                config.RP_PROJECT.split('=')[1],
                                                                config.RP_TOKEN.split('=')[1])

                    finally:
                        __lock.release()


def get_platform_info_allure(platform_info):
    environment = "Desktop" if Browser.get_platform_name() not in [browsers.BROWSER_ANDROID, browsers.BROWSER_IOS] \
        else "Physical" if "udid" in Browser.device else "Simulator"
    device_or_browser_name = \
        "Browser: {}".format(platform_info['browser_name']) if not Browser.get_platform_name() in [
            browsers.BROWSER_ANDROID, browsers.BROWSER_IOS] else "Mobile device: {}".format(Browser.device_name)
    version_of_browser = \
        "Version of browser: {}".format(platform_info['browser_version']) if not Browser.get_platform_name() in [
            browsers.BROWSER_ANDROID, browsers.BROWSER_IOS] else "Version of {} browser: {}".format(
            platform_info['browser_name'], platform_info['browser_version'])
    return f"Environment: {environment}<br/>Platform name: {platform_info['os_name']}<br/>" \
           f"Platform version: {platform_info['os_version']}<br/>{device_or_browser_name}<br/>{version_of_browser}<br/>"


@pytest.fixture(scope="session", autouse=True)
def create_accessibility_excel_file():
    if config.CHECK_ACCESSIBILITY:
        file_path = os.path.join(config.EXCEL_PATH, "Accessibility_report.xlsx")
        ExcelUtil.delete_file(file_path)
        ExcelUtil.create_file(file_path)
        name_of_sheet = "Accessibility_tests"
        ExcelUtil.add_sheet_to_file(file_path, name_of_sheet)


@pytest.fixture(scope="function", autouse=True)
def pre_and_post_condition_accessibility_for_excel_file():
    file_path = os.path.join(config.EXCEL_PATH, "Accessibility_report.xlsx")
    name_of_sheet = "Accessibility_tests"
    if config.CHECK_ACCESSIBILITY:
        precondition_data = ['№:', 'Violation issues:']
        if AllureListener.get_allure_listener():
            test_result = AllureListener.get_allure_listener().get_last_item(TestResult)
            ExcelUtil.pre_write_to_accessibility_file(1, file_path, name_of_sheet, precondition_data,
                                                      test_name=test_result.name, wrap_text=True)
    yield
    if config.CHECK_ACCESSIBILITY:
        ExcelUtil.post_write_to_accessibility_file(1, file_path, name_of_sheet)
        ExcelUtil.resize_column(file_path, name_of_sheet, column_number=1, column_width=80)
        ExcelUtil.resize_column(file_path, name_of_sheet, column_number=3, column_width=80)


@pytest.fixture(scope="session", autouse=True)
def create_test_plan_and_cycle_tm4j(request):
    if config.TM4J:
        __lock.acquire()
        jira_server = 'https://jira.tamm.abudhabi'

        try:
            if len(config.JIRA_USERNAME) == 0 or len(config.JIRA_PASSWORD) == 0:
                assert config.JIRA_USERNAME != "", "Input error, JIRA_USERNAME is empty in the config.py file"
                assert config.JIRA_PASSWORD != "", "Input error, JIRA_PASSWORD is empty in the config.py file"
            atm = Adaptavist(jira_server, config.JIRA_USERNAME, config.JIRA_PASSWORD)

            if not PytestCache.test_run_key:

                config_parser = configparser.ConfigParser()
                config_parser.read(str(request.config.inifile))
                project_key = config_parser['tm4j']['tm4j_project_prefix']
                project_id = atm.get_project_id(project_key)

                tc_key_list = []
                for items in request.node.items:
                    for item in items.own_markers:
                        if item.name == "TC":
                            tc_key_list.append(project_key + '-' + item.args[0])

                # create plan
                test_plan = atm.create_test_plan(project_key=project_key, project_id=project_id,
                                                 test_plan_name="Plan: " + project_key + "-" + datetime.now().
                                                 strftime("%d/%m/%Y %H:%M:%S"))
                test_plan_key = test_plan[0]

                # create a test cycle (formerly test run) with a set of test cases and add it to test plan
                PytestCache.test_run_key = atm.create_test_run(project_key=project_key,
                                                               test_run_name="Cycle: " + project_key + "-" + datetime.
                                                               now().
                                                               strftime("%d/%m/%Y %H:%M:%S"),
                                                               test_cases=set(tc_key_list),
                                                               test_plan_key=test_plan_key,
                                                               time=datetime.now().strftime('%Y-%m-%dT%H:%M:%S%Z.915Z'))
                PytestCache.project_key = project_key

        finally:
            __lock.release()

        return atm, PytestCache.test_run_key, PytestCache.project_key


def update_tc_in_tm4j(request, create_test_plan_and_cycle_tm4j, platform_info, result_tc_trace):
    if config.TM4J:
        try:
            test_case_id = None
            for item in request.node.own_markers:
                if item.name == "TC":
                    test_case_id = item.args[0]

            if test_case_id:
                mapping_auto_tests_statuses_and_tm4j = {
                    "passed": "Pass",
                    "failed": "Fail",
                    "broken": "Fail",
                    "skipped": "Not Executed"
                }
                test_result = AllureListener.get_allure_listener().get_last_item(TestResult)
                test_result.name = StringUtil.get_method_name_for_allure_report(test_result.name)

                test_case_id = create_test_plan_and_cycle_tm4j[0].edit_test_result_status(
                    test_run_key=create_test_plan_and_cycle_tm4j[1],
                    test_case_key=create_test_plan_and_cycle_tm4j[2] + '-' + test_case_id,
                    status=mapping_auto_tests_statuses_and_tm4j.get(test_result.status,
                                                                    "Autotest status is missed in mapping_"
                                                                    "mapping_auto_tests_statuses_and_tm4j"),
                    comment="The result with status ({}) was sent from the Auto test: path: {}<br/><br/>Platform info: "
                            "{}<br/>Autotest result message:<br/>{}.".format(test_result.status, request.node.nodeid,
                                                                             get_platform_info_allure(platform_info),
                                                                             result_tc_trace) if test_result.status in [
                        "failed",
                        "broken"] else "The result with status ({}) was sent from the Auto test: path: {}"
                                       "<br/><br/>Platform info: {}.".format(test_result.status,
                                                                             request.node.nodeid,
                                                                             get_platform_info_allure(
                                                                                 platform_info)))
                return test_case_id
        except IndexError:
            pass


def send_screenshot_to_tm4j(test_case_id, create_test_plan_and_cycle_tm4j, device_or_browser_name, version_of_browser):
    if config.TM4J:
        create_test_plan_and_cycle_tm4j[0]. \
            add_test_result_attachment(test_result_id=test_case_id, attachment=Screenshooter.
                                       take_screenshot(Browser.get_driver(),
                                                       custom_name=device_or_browser_name + "_" + version_of_browser))


@pytest.fixture(scope="function")
def rp_logger(request):
    """
    Fixture for sending results of test to Reporting Portal.

    Args:
        request: request.
    """
    import logging
    logger = logging.getLogger(__name__)
    logger_class = logging.getLoggerClass()
    if '--reportportal' in request.config.invocation_params.args and request.config._reportportal_configured:
        from pytest_reportportal import RPLogger, RPLogHandler
        logging.setLoggerClass(RPLogger)
        rp_handler = RPLogHandler(request.node.config.py_test_service)
        rp_handler.setLevel(logging.INFO)
    yield logger
    logging.setLoggerClass(logger_class)
    if hasattr(logger_class, "_patched"):
        del logger_class._patched


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    """Run test call hook."""
    outcome = yield
    if outcome.excinfo is not None or len(SoftAssert.verification_errors) != 0:
        if Browser.get_platform_name() in [browsers.BROWSER_CHROME, browsers.BROWSER_ANDROID]:
            result, data = JSCheckerUtil.get_network_js_issues()
            url_of_page = Browser.get_url()
            SoftAssert.soft_assert(result,
                                   "\nJS errors from the page where test was failed: "
                                   "\nURL of page: {}\nJS errors:\n{}".format(url_of_page, data))
        else:
            logging.warning("Network JS validation works only on Chrome")
    try:
        with allure.step("Soft Assert validation"):
            SoftAssert.final_assert()
    except AssertionError as e:
        if outcome.excinfo:
            data = list(outcome.excinfo)
            error_message = data[1].args[0] + "\n" + e.args[0]
            data[1].args = (error_message,)
        else:
            raise e


def pytest_configure(config):
    """Pytest Cache initialization."""
    PytestCache.cache = config.cache


@pytest.fixture(scope="function", autouse=True)
def prepare_config():
    """Prepare config file for each journey."""
    for key, value in project_config.__dict__.items():
        config.__dict__[key] = value


@pytest.fixture(scope="session")
def prepare_device_uae_password():
    """Fixture for preparing device (precondition steps) for checking UAE pass."""
    device_name = DataReader().get_test_data("UAEPassword.device_name")
    udid = DataReader().get_test_data("UAEPassword.udid")
    device = UAEPasswordDevice.get_instance(device_name, udid)
    device.restart_app()

    pin = DataReader().get_test_data("UAEPassword.pin")

    for x in pin:
        device.click(By.ID, "key_" + x)
    yield
    device.get_driver().quit()


@pytest.fixture(scope="function", autouse=True)
def configuring_accessibility_issues_to_ignore(request):
    skip_issues = request.node.get_closest_marker('accessibility').kwargs.get("skip_issues") \
        if request.node.get_closest_marker('accessibility') else None
    if skip_issues is not None and not isinstance(skip_issues, list):
        skip_issues = [skip_issues]
    AccessibilityUtil.skip_issues = skip_issues


def pytest_generate_tests(metafunc):
    metafunc.fixturenames.insert(len(metafunc.fixturenames),
                                 metafunc.fixturenames.pop(metafunc.fixturenames.index("screenshot_after_fail")))
