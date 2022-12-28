from d14_ui_framework.configuration import config
from ui_tests.configuration import config as project_config
from d14_mobile_framework.configuration import config as mobile_config
from d14_ui_framework.configuration import config as ui_config
from mobile_tests.configuration import config as mobile_project_config

UI_PROPERTIES_TO_OVERRIDE = ['MOBILE_CHROMEDRIVER_VERSION', 'IMPLICIT_TIMEOUT_SECONDS', 'LOCALE']

for key, value in project_config.__dict__.items():
    config.__dict__[key] = value


for key, value in mobile_project_config.__dict__.items():
    mobile_config.__dict__[key] = value
    if key in UI_PROPERTIES_TO_OVERRIDE:
        ui_config.__dict__[key] = value
