from imports import *

driver.get("https://www.google.com")

# wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Sign In")))
eleSignIn = driver.find_element(By.LINK_TEXT, "Sign in")
print(eleSignIn.is_displayed())
print(eleSignIn.is_enabled())
print(eleSignIn.value_of_css_property('color'))
print(eleSignIn.text)
print(eleSignIn.rect)

sleep(1)

eleQ = driver.find_element(By.CSS_SELECTOR, '[name="q"]')
eleQ.send_keys("webElement")
sleep(1)
title_attribute = driver.switch_to.active_element.get_attribute("title")
print(title_attribute)

sleep(1)
eleQ.send_keys(Keys.CONTROL + "a")
eleQ.send_keys(Keys.DELETE)
sleep(3)
eleQ.send_keys("webElement")
eleQ.send_keys(Keys.ENTER)

sleep(3)
driver.quit()
