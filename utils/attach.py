import allure
import requests
import dotenv
import os
from selene import browser


def attach_screenshot(name='screenshot'):
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )

def attach_browser_stack_video(session_id, version_driver):
    dotenv.load_dotenv()
    user_name = os.getenv('USER_NAME')
    access_key = os.getenv('ACCESS_KEY')
    b_stack_session = requests.get(
        f'https://api.browserstack.com/{version_driver}automate/sessions/{session_id}.json',
        auth=(user_name, access_key),
    ).json()
    video_url = b_stack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )