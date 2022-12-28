from d14_ui_framework.configuration import config
from d14_bulk_actions.tamm.configuration import config as all_actions_config
from ui_tests.configuration import config as project_config

UI_PROPERTIES_TO_IGNORE = ['MOBILE_CHROMEDRIVER_VERSION', 'IMPLICIT_TIMEOUT_SECONDS', 'LOCALE']
ACTIONS_PROPERTIES_TO_IGNORE = ['PATTERN_LOCALE_DICTIONARY_PATH']

for key, value in project_config.__dict__.items():
    if key not in UI_PROPERTIES_TO_IGNORE:
        config.__dict__[key] = value

    if key not in ACTIONS_PROPERTIES_TO_IGNORE:
        all_actions_config.__dict__[key] = value
