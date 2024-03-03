import pytest
from selene import browser
from config import config_options
from wikipedia_tests.controls.attach import get_video, get_screenshot, get_page_source


@pytest.fixture
def android_app_manage(context):
    config_options(context=context)

    yield
    if context == 'bstack':
        session_id = browser.driver.session_id
        get_video(session_id)
    get_screenshot()
    get_page_source()

    browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="local_emulator"
    )


def pytest_configure(config):
    context = config.getoption("--context")


@pytest.fixture
def context(request):
    return request.config.getoption("--context")
