from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.text_field import MobileTextbox
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.feedback_screen \
    import BaseFeedbackScreen
from mobile_tests.screens.ios.main_screens.locker_screens.my_subscriptions_screens.feedback_received_screen import \
    FeedbackReceivedScreen


class FeedbackScreen(BaseFeedbackScreen):

    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, '{}', "Feedback Screen.title")

    @property
    def _btn_happy(self) -> MobileButton:
        return MobileButton(MobileBy.XPATH, '//XCUIElementTypeOther[./XCUIElementTypeButton[2]/following-sibling::*[1]'
                                            '/self::XCUIElementTypeButton]/XCUIElementTypeButton[{}]',
                            'Happy', "Feedback Screen.happy_index")

    @property
    def _btn_sad(self) -> MobileButton:
        return MobileButton(MobileBy.XPATH, '//XCUIElementTypeOther[./XCUIElementTypeButton[2]/following-sibling::*[1]'
                                            '/self::XCUIElementTypeButton]/XCUIElementTypeButton[{}]',
                            'Sad', "Feedback Screen.sad_index")

    @property
    def _btn_normal(self) -> MobileButton:
        return MobileButton(MobileBy.XPATH, '//XCUIElementTypeOther[./XCUIElementTypeButton[2]/following-sibling::*[1]'
                                            '/self::XCUIElementTypeButton]/XCUIElementTypeButton[{}]',
                            'Normal', "Feedback Screen.normal_index")

    @property
    def _btn_submit(self) -> MobileButton:
        return MobileButton(MobileBy.ACCESSIBILITY_ID, '{}', 'Submit', "Feedback Screen.submit")

    @property
    def _txb_comment(self) -> MobileTextbox:
        return MobileTextbox(MobileBy.XPATH, '//XCUIElementTypeTextView', 'Comment')

    def leave_feedback(self, level: BaseFeedbackScreen.FeedbackLevel, comment: str = None):
        super().leave_feedback(level, comment)
        FeedbackReceivedScreen().click_ok()
