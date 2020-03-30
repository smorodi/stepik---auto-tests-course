from selenium.webdriver.support.ui import Select
from selenium import webdriver


if __name__ == "__main__":
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    sum = str(int(x) + int(y))
    select = Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_value(sum)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()