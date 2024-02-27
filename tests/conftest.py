import pytest
from appium.options.android import UiAutomator2Options
from selene import browser

@pytest.fixture
def mobile_manage():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": "azgallyamov_iJc0ZC",
            "accessKey": "pu39Kd7osyjnxcDXz9oZ"
        }
    })
    browser.config.driver_remote_url = "http://hub.browserstack.com/wd/hub"
    browser.config.driver_options = options

    yield

    browser.quit()
