from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

chrome_driver_path = "YOUR_DRIVER_PATH\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)

driver.get("https://www.saucedemo.com/")

# Login  # https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.by.html

user_field = driver.find_element(By.CSS_SELECTOR, "#user-name")
user_field.send_keys("standard_user")

pass_field = driver.find_element(By.CSS_SELECTOR, "#password")
pass_field.send_keys("secret_sauce")

login_btn = driver.find_element(By.CSS_SELECTOR, "#login-button")
login_btn.send_keys(Keys.RETURN)

# Add item to cart

add_to_cart_buttons = driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")
for button in add_to_cart_buttons:
    button.click()

# Go to cart

cart_btn = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
cart_btn.click()

# Purchase

checkout_btn = driver.find_element(By.CSS_SELECTOR, ".checkout_button")
checkout_btn.click()

first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
first_name.send_keys("Python")

last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
last_name.send_keys("WebBot")

postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
postal_code.send_keys("0100100")

continue_btn = driver.find_element(By.CSS_SELECTOR, "#continue")
continue_btn.click()

finish_btn = driver.find_element(By.CSS_SELECTOR, "#finish")
finish_btn.click()

back_btn = driver.find_element(By.CSS_SELECTOR, "#back-to-products")
back_btn.click()
