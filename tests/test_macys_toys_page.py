import pytest


@pytest.mark.smoketest
def test_verify_macys_toys_title(browser):
    browser.get("https://www.macys.com")
    browser.find_element(By.LINK_TEXT, "Toys").click()
    assert browser.title == "All Toys - Macy's"
