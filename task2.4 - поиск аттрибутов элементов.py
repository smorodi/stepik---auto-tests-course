from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

if __name__ == "__main__":
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    treasure = browser.find_element_by_id("treasure")
    x = treasure.get_attribute("valuex")

    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    checkbox = browser.find_element_by_id("robotsRule")
    checkbox.click()
    radiobutton = browser.find_element_by_id("robotCheckbox")
    radiobutton.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

