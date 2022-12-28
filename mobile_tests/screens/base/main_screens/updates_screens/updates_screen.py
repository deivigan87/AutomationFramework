from abc import ABC

from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.screens.base_screen import BaseScreen


class BaseUpdatesScreen(ABC, BaseScreen):

    def __init__(self, locator_type: MobileBy, locator: str, locale: str = None):
        super().__init__(locator_type, locator, locale)
