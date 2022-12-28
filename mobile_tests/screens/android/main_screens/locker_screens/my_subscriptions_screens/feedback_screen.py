from appium.webdriver.common.mobileby import MobileBy

from d14_mobile_framework.framework.elements.button import MobileButton
from d14_mobile_framework.framework.elements.text_field import MobileTextbox
from mobile_tests.screens.base.main_screens.locker_screens.my_subscriptions_screens.feedback_screen \
    import BaseFeedbackScreen


class FeedbackScreen(BaseFeedbackScreen):

    def __init__(self):
        super().__init__(MobileBy.ID, 'happinessMeterHeaderTextView')

    @property
    def _btn_happy(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'iconHappy', 'Happy')

    @property
    def _btn_sad(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'iconSad', 'Sad')

    @property
    def _btn_normal(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'iconNormal', 'Normal')

    @property
    def _btn_submit(self) -> MobileButton:
        return MobileButton(MobileBy.ID, 'buttonSubmit', 'Submit')

    @property
    def _txb_comment(self) -> MobileTextbox:
        return MobileTextbox(MobileBy.ID, 'feedbackEditText', 'Comment')
