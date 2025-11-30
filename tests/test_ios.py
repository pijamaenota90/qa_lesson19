import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be
from utils.attach import attach_screenshot, attach_browser_stack_video


@allure.title('Проверка главного экрана')
def test_main_screen(ios_management):
    with allure.step("Проверить наличие элементов на главном экране"):
        browser.element((AppiumBy.XPATH, "//XCUIElementTypeTabBar//XCUIElementTypeButton[1]")).should(be.existing)
        browser.element((AppiumBy.XPATH, "//XCUIElementTypeTabBar//XCUIElementTypeButton[2]")).should(be.existing)
        browser.element((AppiumBy.XPATH, "//XCUIElementTypeTabBar//XCUIElementTypeButton[3]")).should(be.existing)
        attach_screenshot()

    with allure.step("Кликнуть на Local Testing"):
        browser.element((AppiumBy.XPATH, "//XCUIElementTypeTabBar//XCUIElementTypeButton[3]")).click()
        attach_screenshot()

    with allure.step('Прикрепить видео'):
        session_id = browser.driver.session_id
        attach_browser_stack_video(session_id, 'app-')
