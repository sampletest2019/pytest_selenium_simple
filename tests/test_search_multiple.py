import pytest
from selenium import webdriver

expected_title = 'Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more'
base_url = 'https://www.amazon.com'


@pytest.mark.parametrize("item", [
    "nike air max",
    "reebok crossfit shoes men",
    "puma sneakers",
    "adidas classic shoes"])
@pytest.mark.regressiontest
def test_search(browser, item):
    # navigate to Amazon.com home page
    browser.get(base_url)
    # verify that website title is Amazon.com
    assert browser.title == expected_title
    # locate search field element and enter search item from the list in the search field
    browser.find_element_by_id("twotabsearchtextbox").send_keys(item)
    # locate and click on search button
    browser.find_element_by_xpath("//input[@value='Go']").click()
    # verify the page title
    assert browser.title == 'Amazon.com : ' + item


