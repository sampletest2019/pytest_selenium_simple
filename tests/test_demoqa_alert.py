import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

expected_title = "ToolsQA"
base_url = "https://demoqa.com/alerts"


@pytest.mark.anna3
def test_demoqa(browser):
    browser.get(base_url)
    assert browser.title == expected_title

    browser.find_element_by_id("alertButton").click()
    alert_window = browser.switch_to.alert
    print(alert_window.text)