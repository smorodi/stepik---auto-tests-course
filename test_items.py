from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_for_adding(browser):
    browser.get(link)
    WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-add-to-basket")))