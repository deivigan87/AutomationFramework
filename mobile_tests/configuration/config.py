import os

DEVICES = os.getenv('DEVICES', 'Nexus 5X Emulator')
RUN_TESTS_ON_EACH_DEVICE = os.getenv('RUN_TESTS_ON_EACH_DEVICE', False) in [True, "True"]

# Environment for running tests
UI_ENV = os.getenv('UI_ENV', 'qa_stg')

# Global timeout for operations with elements
ELEMENT_TIMEOUT_SECONDS = 60
SCREEN_LOAD_TIMEOUT_SECONDS = 120
ACTION_REPEAT_TIMEOUT_SECONDS = 60
MOBILE_CHROMEDRIVER_VERSION = "2.40"

# Appium settings
IMPLICITLY_WAIT_SEC = 0
NEW_COMMAND_TIMEOUT_SECONDS = 300
APP_FILE_PATH = os.getenv('APP_FILE_PATH', '/Users/dima/repo/Tamm_Stage.app')  # simulator IOS
APK_FILE_PATH = os.getenv('APK_FILE_PATH', '/Users/dzmitryananyev/Desktop/Python/3.2.1.53.56.apk')  # Android
IPA_FILE_PATH = os.getenv('IPA_FILE_PATH', None)  # real IOS
CAPTURE_LOG = os.getenv('CAPTURE_LOG', False) in [True, "True"]
IOS_CAPABILITIES = {
    'automationName': 'XCUITest',
    'wdaStartupRetries': 2,
    'wdaLaunchTimeout': 90000,
    'wdaEventloopIdleDelay': 5,
    'waitForQuiescence': False,
}
ANDROID_CAPABILITIES = {
    'automationName': 'UiAutomator2',
    'appWaitActivity': 'ae.government.tamm.components.*',
}
APPIUM_SERVER_HOST = '127.0.0.1'
APPIUM_SERVER_PORT = '4723'
DEVICES_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'devices.json')
# Localization
# Supported locale: "en", "ar"
LOCALE = os.getenv('LOCALE', 'en')
PATTERN_LOCALE_DICTIONARY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "locale", "{0}",
                                              "dictionary.json")
PATTERN_LOCALE_DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data", "{0}", "data.json")
PATTERN_ENV_DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data_user", "{0}",
                                     "data.json")
TEST_FILES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data/")
