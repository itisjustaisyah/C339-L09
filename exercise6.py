from imports import *

driver.get("https://thirstycoder.tech/c339/elements.html")

print("1. ", driver.find_element(By.CLASS_NAME, "tomatoes"))
sleep(1)

fruits = driver.find_element(By.ID, "fruits")
fruits = fruits.find_element(By.CLASS_NAME, "tomatoes")
print("2. ", fruits)
sleep(1)

print("3. ", driver.find_elements(By.CSS_SELECTOR, "li"))

driver.quit()
