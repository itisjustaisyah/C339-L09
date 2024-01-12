from imports import *

driver.get("https://the-internet.herokuapp.com/checkboxes")

checkboxes = driver.find_elements(By.XPATH, "/html/body/div[2]/div/div/form/input")

for checkbox in checkboxes:
    print(checkbox.get_attribute("checked") is not None)
sleep(2)

driver.get("https://the-internet.herokuapp.com/dropdown")

select_element = driver.find_element(By.XPATH, "//*[@id='dropdown']")
select = Select(select_element)

option_list = select.options
select.select_by_visible_text('Option 1')
sleep(2)

driver.get("https://thirstycoder.tech/c339/elements.html")
select_element = driver.find_element(By.XPATH, "//*[@id='cars']")
select = Select(select_element)

print("is multiple", select.is_multiple)

select.select_by_index(1)
select.select_by_index(3)

print(select.options)
print(select.all_selected_options)
print(select.all_selected_options[0])
sleep(1)

for i in range(0, len(select.options)):
    select.select_by_index(i)

select.deselect_by_index(3)

sleep(2)
for i in range(0, len(select.options)):
    select.select_by_index(i)

select.deselect_all()

sleep(3)

driver.quit()
