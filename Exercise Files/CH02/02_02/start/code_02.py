from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://c339.herokuapp.com/lesson08/html_code_02.html")



driver.close()