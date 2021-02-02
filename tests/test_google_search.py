import pytest
from selenium.webdriver.common.keys import Keys


@pytest.mark.smoketest
def test_google_search(browser):
    browser.get("https://www.google.com/")
    assert browser.title == "Google"
    browser.find_element_by_name("q").send_keys("Macbook Pro" + Keys.ENTER)
    assert browser.title == "Macbook Pro - Google Search"

