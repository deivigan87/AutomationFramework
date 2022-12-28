from mobile_tests.screens.android.intro_screens.download_offline_map_popup import DownloadOfflineMapPopup
from mobile_tests.screens.android.intro_screens.login_uae_pass_page_screen import LoginUAEPassPageScreen
from mobile_tests.screens.android.intro_screens.meet_home_pop_up_screen import MeetHomePopUpScreen
from mobile_tests.screens.android.intro_screens.quick_tip_popup import QuickTipPopup
from mobile_tests.screens.android.intro_screens.sop1_screen import Sop1Screen
from mobile_tests.screens.android.main_screens.locker_screens.my_subscriptions_screens.feedback_screen \
    import FeedbackScreen
from mobile_tests.screens.android.intro_screens.first_launch_screen import FirstLaunchScreen
from mobile_tests.screens.android.intro_screens.intro_screen import IntroScreen
from mobile_tests.screens.android.main_screens.locker_screens.locker_screen import LockerScreen
from mobile_tests.screens.android.intro_screens.login_smart_pass_page_screen import LoginSmartPassPageScreen
from mobile_tests.screens.android.intro_screens.login_screen import LoginScreen
from mobile_tests.screens.android.main_screens.main_screen import MainScreen
from mobile_tests.screens.android.main_screens.locker_screens.my_subscriptions_screens.my_subscriptions_screen \
    import MySubscriptionsScreen
from mobile_tests.screens.android.main_screens.locker_screens.my_subscriptions_screens.new_subscription_screen \
    import NewSubscriptionScreen
from mobile_tests.screens.android.main_screens.locker_screens.my_subscriptions_screens.package_details_screen \
    import PackageDetailsScreen
from mobile_tests.screens.android.main_screens.locker_screens.my_subscriptions_screens.packages_screen \
    import PackagesScreen
from mobile_tests.screens.android.main_screens.services_screens.adu_screens.adu_search_services_screen import \
    AduSearchServicesScreen
from mobile_tests.screens.android.main_screens.services_screens.adu_screens.adu_services_screen import AduServicesScreen
from mobile_tests.screens.android.main_screens.services_screens.pre_services_screen import PreServicesScreen
from mobile_tests.screens.android.main_screens.services_screens.services_screen import ServicesScreen
from mobile_tests.screens.android.main_screens.locker_screens.my_subscriptions_screens.subscription_successful_screen \
    import SubscriptionSuccessfulScreen
from mobile_tests.screens.android.main_screens.locker_screens.my_subscriptions_screens.summary_screen \
    import SummaryScreen
from mobile_tests.screens.android.intro_screens.tutorial_screen import TutorialScreen
from mobile_tests.screens.android.main_screens.updates_screens.updates_screen import UpdatesScreen
from mobile_tests.screens.android.system_popup_screen import SystemPopUpScreen
from mobile_tests.screens.android.warning_popup_screen import WarningPopupScreen
from mobile_tests.screens.base.intro_screens.download_offline_map_popup import BaseDownloadOfflineMapPopup
from mobile_tests.screens.base.intro_screens.first_launch_screen import BaseFirstLaunchScreen
from mobile_tests.screens.base.intro_screens.intro_screen import BaseIntroScreen
from mobile_tests.screens.base.intro_screens.login_smart_pass_page_screen import BaseLoginSmartPassPageScreen
from mobile_tests.screens.base.intro_screens.login_screen import BaseLoginScreen
from mobile_tests.screens.base.intro_screens.login_uae_pass_page_screen import BaseLoginUAEPassPageScreen
from mobile_tests.screens.base.intro_screens.meet_home_pop_up_screen import BaseMeetHomePopUpScreen
from mobile_tests.screens.base.intro_screens.quick_tip_popup import BaseQuickTipPopup
from mobile_tests.screens.base.intro_screens.sop1_screen import BaseSOP1Screen
from mobile_tests.screens.base.intro_screens.tutorial_screen import BaseTutorialScreen
from mobile_tests.screens.base.main_screens.locker_screens.locker_screen import BaseLockerScreen
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.feedback_screen import \
    BaseFeedbackScreen
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.my_subscriptions_screen import \
    BaseMySubscriptionsScreen
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.new_subscription_screen import \
    BaseNewSubscriptionScreen
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.package_details_screen import \
    BasePackageDetailsScreen
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.packages_screen import \
    BasePackagesScreen
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.subscription_successful_screen \
    import BaseSubscriptionSuccessfulScreen
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.summary_screen import \
    BaseSummaryScreen
from mobile_tests.screens.base.main_screens.main_screen import BaseMainScreen
from mobile_tests.screens.base.main_screens.services_screens.adu_screens.adu_search_services_screen import \
    BaseAduSearchServicesScreen
from mobile_tests.screens.base.main_screens.services_screens.adu_screens.adu_services_screen import \
    BaseAduServicesScreen
from mobile_tests.screens.base.main_screens.services_screens.pre_services_screen import BasePreServicesScreen
from mobile_tests.screens.base.main_screens.services_screens.services_screen import BaseServicesScreen
from mobile_tests.screens.base.main_screens.updates_screens.updates_screen import BaseUpdatesScreen
from mobile_tests.screens.base.screen_factory import ScreenFactory
from mobile_tests.screens.base.system_popup_screen import BaseSystemPopupScreen
from mobile_tests.screens.base.warning_popup_screen import BaseWarningPopupScreen


class AndroidScreenFactory(ScreenFactory):

    @property
    def first_launch_screen(self) -> BaseFirstLaunchScreen:
        return FirstLaunchScreen()

    @property
    def intro_screen(self) -> BaseIntroScreen:
        return IntroScreen()

    @property
    def login_screen(self) -> BaseLoginScreen:
        return LoginScreen()

    @property
    def main_screen(self) -> BaseMainScreen:
        return MainScreen()

    @property
    def download_offline_map_popup(self) -> BaseDownloadOfflineMapPopup:
        return DownloadOfflineMapPopup()

    @property
    def quick_tip_popup(self) -> BaseQuickTipPopup:
        return QuickTipPopup()

    @property
    def sop1_screen(self) -> BaseSOP1Screen:
        return Sop1Screen()

    @property
    def login_smart_pass_page_screen(self) -> BaseLoginSmartPassPageScreen:
        return LoginSmartPassPageScreen()

    @property
    def login_uae_pass_page_screen(self) -> BaseLoginUAEPassPageScreen:
        return LoginUAEPassPageScreen()

    @property
    def tutorial_screen(self) -> BaseTutorialScreen:
        return TutorialScreen()

    @property
    def updates_screen(self) -> BaseUpdatesScreen:
        return UpdatesScreen()

    @property
    def locker_screen(self) -> BaseLockerScreen:
        return LockerScreen()

    @property
    def my_subscriptions_screen(self) -> BaseMySubscriptionsScreen:
        return MySubscriptionsScreen()

    @property
    def new_subscription_screen(self) -> BaseNewSubscriptionScreen:
        return NewSubscriptionScreen()

    @property
    def packages_screen(self) -> BasePackagesScreen:
        return PackagesScreen()

    @property
    def package_details_screen(self) -> BasePackageDetailsScreen:
        return PackageDetailsScreen()

    @property
    def summary_screen(self) -> BaseSummaryScreen:
        return SummaryScreen()

    @property
    def subscription_successful_screen(self) -> BaseSubscriptionSuccessfulScreen:
        return SubscriptionSuccessfulScreen()

    @property
    def feedback_screen(self) -> BaseFeedbackScreen:
        return FeedbackScreen()

    @property
    def services_screen(self) -> BaseServicesScreen:
        return ServicesScreen()

    @property
    def pre_services_screen(self) -> BasePreServicesScreen:
        return PreServicesScreen()

    @property
    def adu_services_screen(self) -> BaseAduServicesScreen:
        return AduServicesScreen()

    @property
    def adu_search_services_screen(self) -> BaseAduSearchServicesScreen:
        return AduSearchServicesScreen()

    @property
    def system_pop_up_screen(self) -> BaseSystemPopupScreen:
        return SystemPopUpScreen()

    @property
    def warning_pop_up_screen(self) -> BaseWarningPopupScreen:
        return WarningPopupScreen()

    @property
    def meet_home_pop_up_screen(self) -> BaseMeetHomePopUpScreen:
        return MeetHomePopUpScreen()
