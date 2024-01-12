from imports import *

driver.get("https://www.example.com")

driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

print("1.", driver.get_cookie("test1"))
print("2.", driver.get_cookies())

driver.delete_cookie("test2")
print("3.", driver.get_cookies())

driver.delete_all_cookies()
print("4.", driver.get_cookies())

driver.quit()




