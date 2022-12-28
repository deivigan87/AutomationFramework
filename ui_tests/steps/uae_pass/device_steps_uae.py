from filelock import FileLock

from selenium.webdriver.common.by import By

from d14_base.data_reader import DataReader
from d14_ui_framework.utils.uae_password_device import UAEPasswordDevice


class DeviceStepsUAE:

    _lock = FileLock("DeviceStepsUAE")

    @staticmethod
    def confirm(fn):
        try:
            DeviceStepsUAE._lock.acquire()
            fn()
            device_name = DataReader().get_test_data("UAEPassword.device_name")
            udid = DataReader().get_test_data("UAEPassword.udid")
            value = UAEPasswordDevice.get_instance(device_name, udid)
            while not value.is_present(By.ID, "confirm"):
                value.refresh()
            value.click(By.ID, "confirm")
            if value.is_present(By.ID, "key_1"):
                pin = "1234"

                for x in pin:
                    value.click(By.ID, "key_" + x)
        finally:
            DeviceStepsUAE._lock.release()
