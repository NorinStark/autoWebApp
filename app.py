import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

user_name = "0968981786"
password = "sousdey123456789"

browser = webdriver.Chrome("/Users/norinstark/PycharmProjects/autoWebApp/chromedriver")
browser.get("https://wwww.facebook.com")

element = browser.find_element_by_id("email")
element.send_keys(user_name)

element = browser.find_element_by_id("pass")
element.send_keys(password)

submit = browser.find_element_by_id("loginbutton")

submit.click()
wait = WebDriverWait(browser, 5)
page_title = browser.title
assert page_title == "FACEBOOK"
