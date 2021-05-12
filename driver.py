from appium import webdriver
from testdata import TestConfig


class Driver:
    """
    Class contains of a driver settings
    """

    def __init__(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.google.android.keep",
            "appActivity": "com.google.android.apps.keep.ui.activities.BrowseActivity",
            "noReset": True,
            "automationName": "UiAutomator2",
            "autoDismissAlerts": True
        }

        self.instance = webdriver.Remote(TestConfig.local_host, desired_cap)
        self.instance.implicitly_wait(15)
