from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

if __name__ == "__main__":
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    radiobutton = browser.find_element_by_id("robotCheckbox")
    radiobutton.click()
    checkbox = browser.find_element_by_css_selector("[for='robotsRule']")
    checkbox.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
