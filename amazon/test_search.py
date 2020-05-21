import pytest
from selenium import webdriver

expected_title = 'Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more'
base_url = 'https://www.amazon.com'
search_title = 'Amazon.com : nike air max'


@pytest.fixture()
def env_setup():
    global driver
    global baseUrl
    # we will use Google Chrome in this test. Specify the location of your chromedriver.exe
    driver = webdriver.Chrome("../chromedriver_81")
    # maximize browser window to full screen
    driver.maximize_window()
    # pull the DOM for 10 seconds when trying to find any element
    driver.implicitly_wait(10)
    yield
    # when test is done, close ALL windows of the browser which has been created
    driver.quit()


def test_search_airmax(env_setup):
    # navigate to Amazon.com home page
    driver.get(base_url)
    # verify that web page title is Amazon.com
    assert driver.title == expected_title
    # locate search field element
    search_field = driver.find_element_by_id("twotabsearchtextbox")
    # enter "nike air max" in the search field
    search_field.send_keys("nike air max")
    # locate search button
    search_button = driver.find_element_by_xpath("//input[@value='Go']")
    # click on 'Search' button
    search_button.click()
    # verify actual page title matches expected page title
    assert driver.title == search_title