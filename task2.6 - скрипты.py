from selenium.webdriver.support.ui import Select
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

if __name__ == "__main__":
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    checkbox = browser.find_element_by_id("robotsRule")
    checkbox.click()
    radiobutton = browser.find_element_by_id("robotCheckbox")
    radiobutton.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()