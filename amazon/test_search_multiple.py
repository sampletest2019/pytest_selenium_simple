import pytest
from selenium import webdriver

expected_title = 'Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more'
base_url = 'https://www.amazon.com'
search_items = ['nike air max', 'reebok crossfit shoes men', 'puma sneakers', 'adidas classic shoes']

@pytest.fixture()
def env_setup():
    global driver
    global baseUrl
    # we will use Google Chrome in this test. Specify the location of your chromedriver.exe
    driver = webdriver.Chrome("../chromedriver_81.exe")
    # wait 10 seconds till the website will open
    driver.implicitly_wait(10)
    # maximize browser window to full screen
    driver.maximize_window()
    yield
    # when test is done, close ALL windows of the browser
    driver.quit()

def test_search(env_setup):
    # navigate to Amazon.com home page
    driver.get(base_url)
    # verify that website title is Amazon.com
    assert driver.title == expected_title
    for item in search_items:
        # locate search field element
        search_field = driver.find_element_by_id("twotabsearchtextbox")
        # enter search item from the list in the search field
        search_field.send_keys(item)
        # locate and click on search button
        driver.find_element_by_xpath("//input[@value='Go']").click()
        # verify the page title
        assert driver.title == 'Amazon.com : ' + item
        # navigate to the previous page
        driver.back()

