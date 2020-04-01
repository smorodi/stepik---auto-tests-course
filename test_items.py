from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_for_adding(browser):
    browser.get(link)
    is_button_clickable = browser.find_element_by_class_name("btn-add-to-basket")
    time.sleep(3)
    assert is_button_clickable, 'Button is not found'