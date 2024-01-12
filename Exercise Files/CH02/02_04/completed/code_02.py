from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://c339.herokuapp.com/lesson08/html_code_02.html")

login_form_absolute = driver.find_element(By.XPATH, "/html/body/form[1]")
login_form_relative = driver.find_element(By.XPATH, "//form[1]")
login_form_id = driver.find_element(By.XPATH, "//form[@id='loginForm']")
print("My login form is:")
print(login_form_absolute)
print(login_form_relative)
print(login_form_id)

driver.close()