import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser
import config


@pytest.fixture(scope='function')
def android_management():
    options = UiAutomator2Options().load_capabilities({
        "platformName": 'android',
        "platformVersion": '13.0',
        "deviceName": 'Google Pixel 7 Pro',
        "app": "bs://sample.app",
        'bstack:options': {
            "projectName": "Android tests",
            "buildName": "browserstack-build-1",
            "userName": config.user_name,
            "accessKey": config.access_key
        }
    })

    browser.config.driver = webdriver.Remote(
        config.remote_url,
        options=options
    )

    browser.config.timeout = 15.0
    browser.config.base_url = "app"

    yield browser

    browser.quit()

@pytest.fixture(scope='function')
def ios_management():
    options = XCUITestOptions().load_capabilities({
        "platformName": "ios",
        "platformVersion": "14",
        "deviceName": "iPhone 12",
        "app": "bs://sample.app",
        'bstack:options': {
            "projectName": "IOS tests",
            "buildName": "browserstack-build-1",
            "userName": config.user_name,
            "accessKey": config.access_key
        }
    })

    driver = webdriver.Remote(
        command_executor=config.remote_url,
        options=options
    )

    browser.config.driver = driver
    browser.config.timeout = 15.0
    browser.config.base_url = "app"

    yield browser

    browser.quit()