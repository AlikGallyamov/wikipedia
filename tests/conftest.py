import os

import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver
from selene import browser

from config import Settings
from wikipedia_tests.controls.attach import get_video, get_screenshot, get_page_source
from wikipedia_tests.controls.utils import get_url_app


@pytest.fixture
def android_app_manage():
    config = Settings()
    config.android_capabilities['bstack:options']["userName"] = config.user_name
    config.android_capabilities['bstack:options']["accessKey"] = config.access_key
    config.android_capabilities["app"] = get_url_app(config.user_name, config.access_key, config.cloud_url)

    options = UiAutomator2Options().load_capabilities(config.android_capabilities)
    # browser.config.driver_remote_url = config.remote_url
    # browser.config.driver_options = options
    browser.config.driver = webdriver.Remote(
        config.remote_url,
        options=options
    )

    yield
    session_id = browser.driver.session_id
    get_video(session_id)
    get_screenshot()
    get_page_source()

    browser.quit()


@pytest.fixture
def ios_app_manage():
    config = Settings()
    config.ios_capabilities['bstack:options']["userName"] = config.user_name
    config.ios_capabilities['bstack:options']["accessKey"] = config.access_key
    config.ios_capabilities["app"] = config.sample_app_url
    options = XCUITestOptions().load_capabilities(config.ios_capabilities)
    browser.config.driver = webdriver.Remote(
        config.remote_url,
        options=options
    )
    yield
    session_id = browser.driver.session_id
    get_video(session_id)
    get_screenshot()
    get_page_source()

    browser.quit()
