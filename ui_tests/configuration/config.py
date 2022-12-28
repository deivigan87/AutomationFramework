# Test environment
import os

# Environment for running tests
UI_ENV = os.getenv('UI_ENV', 'qa_stg')

# Send results to TM4J:
TM4J = os.getenv('TM4J', False) in [True, "True"]
JIRA_USERNAME = os.getenv('JIRA_QA_USERNAME', '')
JIRA_PASSWORD = os.getenv('JIRA_QA_PASSWORD', '')

# ReportPortal project info:
RP_ENDPOINT = os.getenv("RP_ENDPOINT", "")
RP_PROJECT = os.getenv("RP_PROJECT", "")
RP_TOKEN = os.getenv("RP_TOKEN", "")

# Browser Settings
# Supported browsers: "chrome", "firefox", "ie", "edge", "safari". Name of devices you can take in devices.json
# "Android: name of device from devices.json", "iOS: name of device from devices.json"
# DEVICES = os.getenv('DEVICES', 'windows chrome Cloud,iPad Pro 4th gen Cloud')
DEVICES = os.getenv('DEVICES', 'chrome')

# Headless Settings
# Supported values: "y", "n"
HEADLESS = os.getenv('HEADLESS', 'n')

# Localization
# Supported locale: "ar", "en"
LOCALE = os.getenv('LOCALE', 'en')

# Accessibility
CHECK_ACCESSIBILITY = os.getenv('CHECK_ACCESSIBILITY', False) in [True, "True"]

# JS validation
CHECK_JS = os.getenv('CHECK_JS', False) in [True, "True"]

# Client side coverage calculation
CALCULATE_COVERAGE = os.getenv('CALCULATE_COVERAGE', False) in [True, "True"]

# Styles validation
CHECK_STYLES = os.getenv('CHECK_STYLES', False) in [True, "True"]

# W3C validation
CHECK_W3C = os.getenv('CHECK_W3C', False) in [True, "True"]

# Cookies validation
CHECK_COOKIES = os.getenv('CHECK_COOKIES', False) in [True, "True"]
ALLOWED_COOKIES_SIZE = os.getenv('ALLOWED_COOKIES_SIZE', 8 * 1024)

# Links validation
CHECK_LINKS = os.getenv('CHECK_LINKS', False) in [True, "True"]

# Run test on each devices
RUN_TESTS_ON_EACH_DEVICE = os.getenv('RUN_TESTS_ON_EACH_DEVICE', False) in [True, "True"]

# Selenoid Settings (remote browser)
SELENOID_HOST = "localhost"
SELENOID_PORT = "4445"
SELENOID_URL = "http://test:test-password@{host}:{port}/wd/hub".format(host=SELENOID_HOST, port=SELENOID_PORT)

# Sauce labs Settings (remote browser)
SAUCE_USERNAME = os.getenv('SAUCE_USERNAME', '')
SAUCE_ACCESS_KEY = os.getenv('SAUCE_ACCESS_KEY', '')
SAUCE_LAB_WD_HUB = os.getenv('SAUCE_LAB_WD_HUB', '')
SAUCE_LABS_URL = "https://" + SAUCE_USERNAME + ":" + SAUCE_ACCESS_KEY + SAUCE_LAB_WD_HUB
IS_VNC_ENABLED = True
IS_VIDEO_ENABLED = False

# USE_SELENOID - True if you want to run tests on chrome/firefox
USE_SELENOID = os.getenv('USE_SELENOID', False)
# USE_SAUCE_LABS - True if you want to run tests on IE/Edge/Mobile emulators (Android/iOS)
USE_SAUCE_LABS = os.getenv('USE_SAUCE_LABS', False)
USE_SAUCE_TUNNEL_ID = os.getenv('USE_SAUCE_TUNNEL_ID', '')

# SELENOID desktop browsers versions
CHROME_VERSION = os.getenv('CHROME_VERSION', None)
FIREFOX_VERSION = os.getenv('FIREFOX_VERSION', None)
SAFARI_VERSION = os.getenv('SAFARI_VERSION', None)
EDGE_VERSION = os.getenv('EDGE_VERSION', None)

# Sauce Labs platforms/browsers versions
WINDOWS_VERSION_SAUCE_LABS = os.getenv('WINDOWS_VERSION_SAUCE_LABS', '10')
MAC_OS_VERSION_SAUCE_LABS = os.getenv('MAC_OS_VERSION_SAUCE_LABS', '11.00')

CHROME_VERSION_SAUCE_LABS = os.getenv('CHROME_VERSION_SAUCE_LABS', 'latest')
FIREFOX_VERSION_SAUCE_LABS = os.getenv('FIREFOX_VERSION_SAUCE_LABS', 'latest')
IE_VERSION_SAUCE_LABS = os.getenv('IE_VERSION_SAUCE_LABS', '11')
EDGE_VERSION_SAUCE_LABS = os.getenv('EDGE_VERSION_SAUCE_LABS', 'latest')
SAFARI_VERSION_SAUCE_LABS = os.getenv('SAFARI_VERSION_SAUCE_LABS', '14')

# ANDROID_PLATFORM_VERSION_SAUCE_LABS = os.getenv('ANDROID_PLATFORM_VERSION_SAUCE_LABS', '11.0') NOT USE FOR NOW
IOS_PLATFORM_VERSION_SAUCE_LABS = os.getenv('IOS_PLATFORM_VERSION_SAUCE_LABS', '15.0')


# Mobile
# Android, iOS
# MOBILE_PLATFORM_VERSION = os.getenv('MOBILE_PLATFORM_VERSION', "12.0")

# Waiting settings
EXPLICITLY_WAIT_SEC = 150
PAGE_LOAD_TIMEOUT_SEC = 250
IMPLICITLY_WAIT_SEC = 0
CYCLE_WAIT_TIMEOUT = 150
WAIT_ELEMENT = 10

MOBILE_CHROMEDRIVER_VERSION = "2.40"

# Selenoid Appium
APPIUM_HOST = "localhost"
APPIUM_PORT = "4723"
# APPIUM_PORT = "4445"
# APPIUM_URL = "http://test:test-password@{host}:{port}/wd/hub".format(host=APPIUM_HOST, port=APPIUM_PORT)
APPIUM_URL = "http://{host}:{port}/wd/hub".format(host=APPIUM_HOST, port=APPIUM_PORT)

# Sauce labs Appium
SAUCE_LABS_APPIUM_URL = "https://" + SAUCE_USERNAME + ":" + SAUCE_ACCESS_KEY + SAUCE_LAB_WD_HUB

# Common Paths
DEVICES_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'devices.json')
INITIAL_WDA_LOCAL_PORT = 8101

ELEMENTS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'pages', 'elements.json')
PATTERN_ENV_BASE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "environments", "{0}", "")
PATTERN_LOCALE_DICTIONARY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "locale", "{0}",
                                              "dictionary.json")
PATTERN_LOCALE_DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data", "{0}", "data.json")
PATTERN_LOCALE_USER_DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_user_data", "{0}",
                                             "data.json")
PATTERN_ENV_DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data_user", "{0}",
                                     "data.json")
TEST_FILES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data/")
EXCEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", 'tests')
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", 'tests')
W3C_URL = "http://localhost:8688/?showsource=yes&doc="

# Hosts (Format: ["uploadstg.dmt.gov.ae:10.253.221.40", "uploadstg.dmt.gov.ae:10.7.221.22", etc] )
HOSTS = []
