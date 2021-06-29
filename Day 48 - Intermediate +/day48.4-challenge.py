from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = YOUR_CHROME_WEBDRIVER_PATH
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Dan")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("TheMan")
email = driver.find_element_by_name("email")
email.send_keys("dantheman@email.com")

sign_up_btn = driver.find_element_by_css_selector(".btn")
sign_up_btn.click()

# driver.quit()