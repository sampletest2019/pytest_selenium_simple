import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # wait 10 seconds to pull the DOM
    browser.implicitly_wait(10)
    # maximize browser window to full screen
    browser.maximize_window()
    yield browser
    # make a screenshot before closing the browser
    allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    # when test is done, close ALL windows of the browser
    browser.quit()

