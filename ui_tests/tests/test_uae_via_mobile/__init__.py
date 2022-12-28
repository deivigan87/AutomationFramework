from d14_ui_framework.configuration import config
from ui_tests.configuration import config as project_config

for key, value in project_config.__dict__.items():
    config.__dict__[key] = value
