import pytest
from selenium import webdriver
import time
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_element_by_class_name("btn-add-to-basket")
    assert button.is_displayed, "button is not  displayed"
    time.sleep(5)

