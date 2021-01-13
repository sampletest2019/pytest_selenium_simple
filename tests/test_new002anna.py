import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

expected_title = "Nordstrom Rack Online & In Store: Shop Dresses, Shoes, Handbags, Jewelry & More"
base_url = "https://www.nordstromrack.com/"
expected_url_coach = "https://www.nordstromrack.com/shop/search?query=Coach"


@pytest.mark.anna2
def test_nordstrom(browser):
    browser.get(base_url)
    assert browser.title == expected_title

    browser.find_element_by_name("query").send_keys("Coach"+Keys.ENTER)
    assert browser.current_url == expected_url_coach
    dropdown = Select (browser.find_element_by_name("sort-by"))
    dropdown.select_by_index(4)
    print(dropdown.first_selected_option.text)
    assert dropdown.first_selected_option.text == "Price Low To High"



