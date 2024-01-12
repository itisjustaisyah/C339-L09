from imports import *

driver.get("https://www.selenium.dev/documentation/webdriver/browser/alerts/")
sleep(3)

driver.find_element(By.LINK_TEXT, "See an example alert")
element = wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "See an example alert")))
driver.execute_script("arguments[0].click();", element)
sleep(3)
alert = wait.until(expected_conditions.alert_is_present())
text = alert.text
alert.accept()
print(text, "OK")
sleep(3)


driver.find_element(By.LINK_TEXT, "See a sample confirm")
element = wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "See a sample confirm")))
driver.execute_script("arguments[0].click();", element)
sleep(3)
alert = wait.until(expected_conditions.alert_is_present())
text = alert.text
alert.dismiss()
print(text, "Cancel")
sleep(3)


driver.find_element(By.LINK_TEXT, "See a sample prompt")
element = wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "See a sample prompt")))
driver.execute_script("arguments[0].click();", element)
sleep(3)
wait.until(expected_conditions.alert_is_present())
alert = Alert(driver)
alert.send_keys("Selenium")
alert.accept()
print(text, "OK")

driver.quit()
