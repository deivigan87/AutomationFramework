from mobile_tests.screens.screen_resolver import ScreenResolver


class ServiceSteps:

    @staticmethod
    def select_service(service):
        screen = ScreenResolver().factory
        screen.services_screen.select_service(service)
        screen.pre_services_screen.click_start_service()
