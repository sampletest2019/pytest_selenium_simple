import pytest
from selenium import webdriver

expected_title = "Wikipedia"
base_url = "https://www.wikipedia.org/"


@pytest.mark.anna
def test_wiki(browser):
    browser.get(base_url)
    assert browser.title == expected_title

    browser.find_element_by_id("searchInput").send_keys("pycharm")
    browser.find_element_by_xpath("//button[@class='pure-button pure-button-primary-progressive']").click()