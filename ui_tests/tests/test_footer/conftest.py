import pytest

from d14_ui_framework.configuration import config


@pytest.fixture(scope="function")
def check_links():
    previous_value = config.CHECK_LINKS
    config.CHECK_LINKS = True
    yield
    config.CHECK_LINKS = previous_value
