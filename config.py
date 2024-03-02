import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


def load_env():
    load_dotenv()


class Settings(BaseSettings):
    user_name: str = os.getenv('user_name')
    access_key: str = os.getenv('access_key')
    cloud_url: str = os.getenv('cloud_url')
    remote_url: str = os.getenv('remote_url')
    sample_app_url: str = os.getenv('sample_app_url')
    android_capabilities: dict = {
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        'appWaitActivity': 'org.wikipedia.*',
        "app": "",

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": f"{user_name}",
            "accessKey": f"{access_key}"
        }
    }
    ios_capabilities: dict = {
        "app": f"{sample_app_url}",

        "deviceName": "iPhone 11 Pro",
        "platformName": "ios",
        "platformVersion": "13",

        "bstack:options": {
            "userName": f"{user_name}",
            "accessKey": f"{access_key}",
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test"
        }
    }


load_env()
