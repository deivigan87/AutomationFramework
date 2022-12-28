from pytest_bdd import scenario
from ui_tests.steps.home_page_steps import *
from ui_tests.steps.smartpass_steps import *


@scenario("../features/login-logout.feature", "Login and logout via SmartPass")
def test_login_logout_via_smartpass():
    pass
