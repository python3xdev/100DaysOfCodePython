from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

# AUTO TINDER SWIPING BOT

chrome_driver_path = YOUR_CHROME_DRIVER_PATH
driver = webdriver.Chrome(chrome_driver_path)

FACEBOOK_LOGIN = (YOUR_EMAIL, YOUR_PASSWORD)

driver.get("https://tinder.com/")
driver.maximize_window()

# ----------------- LOGIN WITH FACEBOOK -----------------
login_btn = driver.find_element_by_css_selector("div .button")
login_btn.click()

sleep(1)

more_options_btn = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/span/button")
try:
    if more_options_btn.text == "MORE OPTIONS":
        more_options_btn.click()
        sleep(3)
except NoSuchElementException:
    pass

login_fb_btn = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button")
login_fb_btn.click()

sleep(5)
driver.switch_to.window(driver.window_handles[1])  # switching to the facebook login window

email_field = driver.find_element_by_id("email")
email_field.send_keys(FACEBOOK_LOGIN[0])
password_field = driver.find_element_by_id("pass")
password_field.send_keys(FACEBOOK_LOGIN[1])
login_facebook = driver.find_element_by_name("login")
login_facebook.click()

# ----------------- AUTOMATING TINDER -----------------
sleep(10)
driver.switch_to.window(driver.window_handles[0])  # switching back to the tinder window

sleep(2)
allow_btn = driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div/div/div[3]/button[1]')
allow_btn.click()

sleep(2)
i_accept_tos_and_cookies_btn = driver.find_element_by_xpath('//*[@id="u2005023502"]/div/div[2]/div/div/div[1]/button')
i_accept_tos_and_cookies_btn.click()

sleep(2)
disable_notifications_btn = driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div/div/div[3]/button[2]')
disable_notifications_btn.click()

sleep(1)
like_xpath = '//*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button'
like_xpath_2nd = '//*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button'

for n in range(100):
    sleep(1)
    try:
        try:
            like_btn = driver.find_element_by_xpath(like_xpath)
            like_btn.click()
            print("Profile Liked.")
        except NoSuchElementException:
            like_btn = driver.find_element_by_xpath(like_xpath_2nd)
            like_btn.click()
            print("Profile Liked.")
    except NoSuchElementException:  # If page is not completely loaded yet this will run the loop again.
        print("Waiting for profile to load.")
        sleep(1)
    except ElementClickInterceptedException:
        try:
            # close the "Match" pop up here
            popup = driver.find_element_by_css_selector(".itsAMatch a")
            print(f"Match!")
            sleep(4)
            popup.click()
        except NoSuchElementException:
            print("Waiting for profile to load.")
            sleep(1)

print("You have reached your daily 100 Likes. Closing program in 10 seconds.")
sleep(10)
driver.quit()
