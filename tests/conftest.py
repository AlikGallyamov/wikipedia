import pytest
from appium.options.android import UiAutomator2Options
from selene import browser

from wikipedia_tests.controls.utils import get_url_app


@pytest.fixture
def mobile_manage():
    url_app = get_url_app()
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": f"{url_app}",

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": "azgallyamov_0wTr3j",
            "accessKey": "mckBkK9h5XxxhVcXBnpq"
        }
    })
    browser.config.driver_remote_url = "http://hub.browserstack.com/wd/hub"
    browser.config.driver_options = options

    yield

    browser.quit()
