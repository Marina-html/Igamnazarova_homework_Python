from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("http://uitestingplayground.com/dynamicid")
button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
button.click()

sleep(30)

