from imports import *


driver.get('https://www.selenium.dev/')
print(driver.title)
print(driver.current_url)
sleep(1)

driver.get('https://www.google.com')
driver.back()
driver.forward()
sleep(1)
driver.refresh()
driver.quit()

