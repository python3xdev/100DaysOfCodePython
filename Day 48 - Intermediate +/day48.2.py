from selenium import webdriver

chrome_driver_path = YOUR_CHROME_WEBDRIVER_PATH
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")

items = driver.find_element_by_css_selector(".event-widget .shrubbery ul")
items_list = items.text.split("\n")
items_dict = {items_list[i]: items_list[i + 1] for i in range(0, 10, 2)}
print(items_dict)

driver.quit()
