import pytest
from selenium.webdriver.common.by import By

base_url = 'https://homepro.herokuapp.com/index.php'
expected_url = 'https://homepro.herokuapp.com/order.php'


@pytest.mark.smoketest
def test_schedule_page_navigation(browser):
    browser.get(base_url)
    browser.find_element(By.LINK_TEXT, "Schedule an Appointment").click()
    assert expected_url == browser.current_url
