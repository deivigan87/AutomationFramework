# -*- coding: utf-8 -*-
from d14_mobile_framework.framework.utils.config_reader import ConfigReader

from d14_mobile_framework.framework.constants import ANDROID
from mobile_tests.screens.android.android_screen_factory import AndroidScreenFactory
from mobile_tests.screens.ios.ios_screen_factory import IosScreenFactory


class ScreenResolver:
    def __init__(self):
        platform_name = ConfigReader().get_platform_name()
        if platform_name == ANDROID:
            self._factory = AndroidScreenFactory()
        else:
            self._factory = IosScreenFactory()

    @property
    def factory(self):
        return self._factory
