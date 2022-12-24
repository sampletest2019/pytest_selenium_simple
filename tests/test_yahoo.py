@pytest.mark.smoketest
def test_title(browser_firefox):

    browser_firefox.get('https://www.yahoo.com')
    assert browser_firefox.title == "Amazon.com"




