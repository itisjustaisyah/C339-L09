from imports import *

driver.get("https://thirstycoder.tech/c339/window1.html")

original_window = driver.current_window_handle

driver.minimize_window()
sleep(1)
driver.maximize_window()
sleep(1)

driver.set_window_size(1025, 768)
sleep(1)
driver.set_window_position(100, 100)


print(driver.get_window_position(), driver.get_window_size())

sleep(1)

driver.find_element(By.CSS_SELECTOR, 'a').click()

driver.switch_to.new_window('tab')
driver.get("https://selenium.dev")
sleep(1)
driver.close()
driver.switch_to.window(original_window)

driver.switch_to.new_window('window')
driver.get("https://selenium.dev")
sleep(1)
driver.close()
driver.switch_to.window(original_window)


sleep(2)
driver.save_screenshot("screenshot.png")
driver.find_element(By.CSS_SELECTOR, 'a').screenshot("element_screenshot.png")

value = driver.execute_script('return arguments[0].innerText', driver.find_element(By.CSS_SELECTOR, 'a'))
sleep(3)

print("script:", value)
driver.quit()

