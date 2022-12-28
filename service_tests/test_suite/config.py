import os

APPLICATION_NAME = os.getenv("APPLICATION_NAME", "api_journey")
SERVICE_ENV = os.getenv("SERVICE_ENV", "stg")
PROTOCOL = os.getenv("PROTOCOL", "protocol_https")
EXCEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", 'test_suite')
