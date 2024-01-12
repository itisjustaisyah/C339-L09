from imports import *


def test_no_wait():
    driver.get("https://thirstycoder.tech/c339/delay.html")
    elementP = driver.find_element(By.TAG_NAME, "p")
    value = driver.execute_script('return arguments[0].innerText', elementP)
    assert value == "Hello from JavaScript!"


def test_implicit_wait():
    driver.get("https://thirstycoder.tech/c339/delay.html")
    driver.implicitly_wait(2)
    elementP = driver.find_element(By.CSS_SELECTOR, 'p')
    value = driver.execute_script('return arguments[0].innerText', elementP)
    assert value == "Hello from JavaScript!"


def text_explicitly_wait():
    driver.get("https://thirstycoder.tech/c339/delay.html")
    elementP = wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "p")))
    value = driver.execute_script('return arguments[0].innerText', elementP)
    assert value == "Hello from JavaScript!"


test_implicit_wait()
sleep(1)
driver.quit()
