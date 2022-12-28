import re
import sys
from collections import OrderedDict

import allure
import pytest
from allure_commons.model2 import TestResult, Status
from allure_commons.types import AttachmentType

import d14_mobile_framework
from d14_mobile_framework.configuration import config
from d14_mobile_framework.framework.device.device import Device
from d14_base.screenshooter import Screenshooter
from d14_base.string_util import StringUtil
from d14_base.html_allure_report_listener import AllureListener
from d14_base.pytest_cache import PytestCache
from mobile_tests.screens.base.screen_factory import ScreenFactory
from mobile_tests.screens.screen_resolver import ScreenResolver


@pytest.fixture(scope='function')
def screen(request) -> ScreenFactory:
    params = {}
    try:
        params = OrderedDict(request.node.callspec.params.items())
        del params['__pytest_repeat_step_number']
    except (KeyError, AttributeError):
        pass
    test_id = str(params) + str(request.node.fspath) + re.sub(r'\[.*', '', request.node.name)
    Device(test_id)
    return ScreenResolver().factory


@pytest.fixture(scope='function', autouse=True)
def add_screenshot(request):
    tests_failed_before_function = request.session.testsfailed
    yield
    try:
        if AllureListener.get_allure_listener():
            test_result = AllureListener.get_allure_listener().get_last_item(TestResult)
            test_result.name = StringUtil.get_method_name_for_allure_report(test_result.name)
            test_result.description = config.DEVICE_ID
            if request.session.testsfailed != tests_failed_before_function:
                test_result.steps[-1].status = Status.FAILED
                test_result.status = Status.FAILED
                Screenshooter.set_session_screen_dir()
                Device().switch_to_native_app()
                allure.attach.file(Screenshooter.take_screenshot(Device().driver), 'screenshot', AttachmentType.JPG)
    finally:
        Device().quit_session()


def pytest_configure(config):
    if d14_mobile_framework.configuration.config.CAPTURE_LOG:
        sys.stdout = sys.stderr
    PytestCache.cache = config.cache
