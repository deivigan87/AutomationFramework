from abc import ABC, abstractmethod

from appium.webdriver.common.mobileby import MobileBy
from d14_mobile_framework.framework.device.device import Device
from d14_mobile_framework.framework.device.swipe_direction import SwipeDirection

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.element_state import ElementState
from d14_mobile_framework.framework.screens.base_screen import BaseScreen
from d14_mobile_framework.framework.utils.wait_for import wait_for


class BaseMainScreen(ABC, BaseScreen):

    def __init__(self, locator_type: MobileBy, locator: str):
        super().__init__(locator_type, locator)

    class MenuItem:
        ASPECTS_OF_LIFE = "Menu.aspects_of_life"
        CO_CREATE = "Menu.co_create"
        NEWS = "Menu.news"
        MY_EVENTS = "Menu.my_events"
        ABU_DHABI_GOVERNMENT_ENTITIES = "Menu.abu_dhabi_government_entities"
        ABOUT_ABU_DHABI = "Menu.about_abu_dhabi"
        TEST_API_TOKEN = "Menu.test_api_token"
        ABOUT_TAMM = "Menu.about_tamm"
        SETTINGS = "Menu.settings"
        HOW_TO_USE = "Menu.how_to_use"
        LOGOUT = "Menu.logout"
        ARABIC = "Menu.arabic"
        ENGLISH = "Menu.english"

    class Screen:
        UPDATES = "Updates Screen.title"
        LOCKER = "Locker Screen.title"
        SERVICES = "Services Screen.title"
        COMMUNITIES = "Communities Screen.title"

    @property
    @abstractmethod
    def _btn_menu(self) -> MobileButton:
        pass

    @abstractmethod
    def _btn_menu_item(self, key) -> MobileButton:
        pass

    @abstractmethod
    def _btn_screen(self, key) -> MobileButton:
        pass

    @property
    @abstractmethod
    def _btn_english(self) -> MobileButton:
        pass

    @property
    @abstractmethod
    def _btn_language(self) -> MobileButton:
        pass

    @property
    @abstractmethod
    def _btn_arabic(self) -> MobileButton:
        pass

    def click_menu_item(self, item: MenuItem):
        self._btn_menu.tap()

        def wait_for_item():
            if self._btn_menu_item(item).is_element_in_state(ElementState.EXISTS)\
                    and self._btn_menu_item(item).is_element_in_state(ElementState.VISIBLE):
                Device().swipe(SwipeDirection.DOWN)
                return True
            else:
                Device().swipe(SwipeDirection.DOWN)
            return False
        wait_for(wait_for_item, message="{} Logout is absent".format(item))
        self._btn_menu_item(item).tap()

    def select_language(self, language):
        self._btn_language.tap()
        if language == 'en':
            self._btn_english.tap()
        else:
            self._btn_arabic.tap()

    def open_screen(self, screen: Screen):
        self._btn_screen(screen).tap()
