import pytest


expected_title = 'Amazon.com. Spend less. Smile more.'
base_url = 'https://www.amazon.com'
search_title = 'Amazon.com: nike air max'


@pytest.mark.alina
def test_title(browser):
    # navigate to Amazon.com home page
    browser.get(base_url)
    # verify that website title is Amazon.com
    assert browser.title == expected_title

