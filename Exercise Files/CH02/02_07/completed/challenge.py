from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.seleniumhq.org')

element_id = driver.find_element(By.ID,'docsearch')
print(element_id)

element_name = driver.find_element(By.NAME,'submit')
print(element_name)

element_xpath1 = driver.find_element(By.XPATH,"/html/body/div/main/div[2]/h2")
print(element_xpath1)

element_xpath2 = driver.find_element(By.XPATH,"//*/main/div[2]/h2")
print(element_xpath2)

element_classname = driver.find_element(By.CLASS_NAME,'display-1')
print(element_classname)

driver.close()