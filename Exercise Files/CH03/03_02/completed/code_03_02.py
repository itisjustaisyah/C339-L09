from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
driver.get("https://c339.herokuapp.com/lesson08/html_code_03_02.html")

select= Select(driver.find_element(By.NAME, 'numReturnSelect'))
select.select_by_index(4)
time.sleep(2)
select.select_by_visible_text("200")
time.sleep(2)
select.select_by_value("250")
time.sleep(2)

options = select.options
print(options)

submit_button = driver.find_element(By.NAME, 'continue')
submit_button.click();
time.sleep(2)

driver.close()
