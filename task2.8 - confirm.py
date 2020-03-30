from selenium.webdriver.support.ui import Select
from selenium import webdriver
import math
import os
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

if __name__ == "__main__":
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)
    button = browser.find_element_by_class_name("btn-primary")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()