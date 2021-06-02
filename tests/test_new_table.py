import pytest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select

expected_title = "The Internet"
base_url = "http://the-internet.herokuapp.com/tables"


@pytest.mark.anna4
def test_table(browser):
    browser.get(base_url)
    assert browser.title == expected_title
    # table = browser.find_element_by_id("table1")
    table = browser.find_element_by_xpath("//div[@id='content']/div/table[1]")
    rows = table.find_elements_by_tag_name("tr")
    # for row in rows:
    #     print(row.text)
    print(rows[0].text)
    print(rows[1].text)
    print(rows[2].text)
    print(rows[3].text)
    print(rows[4].text)
    # data_row_3 = rows[3].find_elements_by_tag_name("td")
    # assert data_row_3[1].text == "Jason"

