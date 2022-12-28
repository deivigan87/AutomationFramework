from abc import ABC, abstractmethod

from mobile_tests.screens.base.intro_screens.download_offline_map_popup import BaseDownloadOfflineMapPopup
from mobile_tests.screens.base.intro_screens.login_uae_pass_page_screen import BaseLoginUAEPassPageScreen
from mobile_tests.screens.base.intro_screens.meet_home_pop_up_screen import BaseMeetHomePopUpScreen
from mobile_tests.screens.base.intro_screens.quick_tip_popup import BaseQuickTipPopup
from mobile_tests.screens.base.intro_screens.sop1_screen import BaseSOP1Screen
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.feedback_screen \
    import BaseFeedbackScreen
from mobile_tests.screens.base.intro_screens.first_launch_screen import BaseFirstLaunchScreen
from mobile_tests.screens.base.intro_screens.intro_screen import BaseIntroScreen
from mobile_tests.screens.base.main_screens.locker_screens.locker_screen import BaseLockerScreen
from mobile_tests.screens.base.intro_screens.login_smart_pass_page_screen import BaseLoginSmartPassPageScreen
from mobile_tests.screens.base.intro_screens.login_screen import BaseLoginScreen
from mobile_tests.screens.base.main_screens.main_screen import BaseMainScreen
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.my_subscriptions_screen \
    import BaseMySubscriptionsScreen
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.new_subscription_screen \
    import BaseNewSubscriptionScreen
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.package_details_screen \
    import BasePackageDetailsScreen
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.packages_screen \
    import BasePackagesScreen
from mobile_tests.screens.base.main_screens.services_screens.adu_screens.adu_search_services_screen import \
    BaseAduSearchServicesScreen
from mobile_tests.screens.base.main_screens.services_screens.adu_screens.adu_services_screen import \
    BaseAduServicesScreen
from mobile_tests.screens.base.main_screens.services_screens.pre_services_screen import BasePreServicesScreen
from mobile_tests.screens.base.main_screens.services_screens.services_screen import BaseServicesScreen
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.subscription_successful_screen \
    import BaseSubscriptionSuccessfulScreen
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.summary_screen \
    import BaseSummaryScreen
from mobile_tests.screens.base.intro_screens.tutorial_screen import BaseTutorialScreen
from mobile_tests.screens.base.main_screens.updates_screens.updates_screen import BaseUpdatesScreen
from mobile_tests.screens.base.system_popup_screen import BaseSystemPopupScreen
from mobile_tests.screens.base.warning_popup_screen import BaseWarningPopupScreen


class ScreenFactory(ABC):

    @property
    @abstractmethod
    def first_launch_screen(self) -> BaseFirstLaunchScreen:
        pass

    @property
    @abstractmethod
    def intro_screen(self) -> BaseIntroScreen:
        pass

    @property
    @abstractmethod
    def login_screen(self) -> BaseLoginScreen:
        pass

    @property
    @abstractmethod
    def main_screen(self) -> BaseMainScreen:
        pass

    @property
    @abstractmethod
    def download_offline_map_popup(self) -> BaseDownloadOfflineMapPopup:
        pass

    @property
    @abstractmethod
    def quick_tip_popup(self) -> BaseQuickTipPopup:
        pass

    @property
    @abstractmethod
    def sop1_screen(self) -> BaseSOP1Screen:
        pass

    @property
    @abstractmethod
    def login_smart_pass_page_screen(self) -> BaseLoginSmartPassPageScreen:
        pass

    @property
    @abstractmethod
    def login_uae_pass_page_screen(self) -> BaseLoginUAEPassPageScreen:
        pass

    @property
    @abstractmethod
    def tutorial_screen(self) -> BaseTutorialScreen:
        pass

    @property
    @abstractmethod
    def updates_screen(self) -> BaseUpdatesScreen:
        pass

    @property
    @abstractmethod
    def locker_screen(self) -> BaseLockerScreen:
        pass

    @property
    @abstractmethod
    def my_subscriptions_screen(self) -> BaseMySubscriptionsScreen:
        pass

    @property
    @abstractmethod
    def new_subscription_screen(self) -> BaseNewSubscriptionScreen:
        pass

    @property
    @abstractmethod
    def packages_screen(self) -> BasePackagesScreen:
        pass

    @property
    @abstractmethod
    def package_details_screen(self) -> BasePackageDetailsScreen:
        pass

    @property
    @abstractmethod
    def summary_screen(self) -> BaseSummaryScreen:
        pass

    @property
    @abstractmethod
    def subscription_successful_screen(self) -> BaseSubscriptionSuccessfulScreen:
        pass

    @property
    @abstractmethod
    def feedback_screen(self) -> BaseFeedbackScreen:
        pass

    @property
    @abstractmethod
    def services_screen(self) -> BaseServicesScreen:
        pass

    @property
    @abstractmethod
    def adu_services_screen(self) -> BaseAduServicesScreen:
        pass

    @property
    @abstractmethod
    def adu_search_services_screen(self) -> BaseAduSearchServicesScreen:
        pass

    @property
    @abstractmethod
    def pre_services_screen(self) -> BasePreServicesScreen:
        pass

    @property
    @abstractmethod
    def system_pop_up_screen(self) -> BaseSystemPopupScreen:
        pass

    @property
    @abstractmethod
    def warning_pop_up_screen(self) -> BaseWarningPopupScreen:
        pass

    @property
    @abstractmethod
    def meet_home_pop_up_screen(self) -> BaseMeetHomePopUpScreen:
        pass
