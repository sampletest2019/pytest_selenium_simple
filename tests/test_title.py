import pytest
from selenium import webdriver

expected_title = 'Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more'
base_url = 'https://www.amazon.com'
search_title = 'Amazon.com: nike air max'


def test_title(browser):
    # navigate to Amazon.com home page
    browser.get(base_url)
    # verify that website title is Amazon.com
    assert browser.title == expected_title
