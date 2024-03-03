import os

from typing import Optional

from appium.options.android import UiAutomator2Options
from appium import webdriver
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from selene import browser

from wikipedia_tests.controls.utils import get_local_path_app


def load_env(context):
    load_dotenv(dotenv_path=f'.env.{context}')


def load_env_credential():
    load_dotenv(dotenv_path=f'.env')


class Settings(BaseSettings):
    user_name: Optional[str] = os.getenv('user_name')
    access_key: Optional[str] = os.getenv('access_key')
    remote_url: str = os.getenv('remote_url')
    device_name: str = os.getenv('device_name')
    app_url: str = os.getenv('app_url', get_local_path_app())


def config_options(context):
    if context == 'bstack':
        load_env_credential()
    load_env(context)
    config = Settings()
    if context == 'bstack':
        device_capabilities = {
            "platformName": "android",
            "platformVersion": "9.0",
            "deviceName": config.device_name,
            "app": config.app_url,

            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                "userName": f"{config.user_name}",
                "accessKey": f"{config.access_key}"
            }
        }
    if context == 'local_real':
        device_capabilities = {
            "platformName": "android",
            "appium:automationName": "UiAutomator2",
            "appium:ignoreHiddenApiPolicyError": "true",
            "appium:app": config.app_url,
            "appium:deviceName": config.device_name,
            "appium:appWaitActivity": "org.wikipedia.*",
            "appium:noReset": "true"
        }
    if context == 'local_emulator':
        device_capabilities = {
            "platformName": "android",
            "appium:automationName": "UiAutomator2",
            "appium:ignoreHiddenApiPolicyError": "true",
            "appium:app": config.app_url,
            "appium:deviceName": config.device_name,
            "appium:appWaitActivity": "org.wikipedia.*",
            "appium:noReset": "false"
        }

    options = UiAutomator2Options().load_capabilities(device_capabilities)
    browser.config.driver = webdriver.Remote(
        config.remote_url,
        options=options
    )
    return context
