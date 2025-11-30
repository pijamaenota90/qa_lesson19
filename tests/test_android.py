import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from utils.attach import attach_screenshot, attach_browser_stack_video


@allure.title('Проверка поиска статьи в Википедии')
def test_android_search(android_management):

    with allure.step('Поиск'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Moscow')
        attach_screenshot()

    with allure.step('Проверка найденного контента'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Moscow'))
        attach_screenshot()

    with allure.step('Прикрепить видео'):
        session_id = browser.driver.session_id
        attach_browser_stack_video(session_id, 'app-')