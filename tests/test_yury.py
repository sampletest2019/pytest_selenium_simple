import pytest

@pytest.mark.smoketest
def test_verify_page_url(browser):
  browser.get('https://www.ebay.com)
  assert browser.title == "Ebay"            
