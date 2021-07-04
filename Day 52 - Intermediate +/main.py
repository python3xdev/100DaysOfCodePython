from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = YOUR_CHROME_DRIVER_PATH
INSTAGRAM_LOGIN = (YOUR_EMAIL, YOUR_PASSWORD)
TARGET_ACCOUNT = 'YOUR_TARGET_ACCOUNT_GOES_HERE'
URL = "https://www.instagram.com/"
PROFILE_FOLLOW_LIMIT = 20

# --- Instagram Follower Bot ---

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_driver_path)

    def login(self):
        self.driver.get(f"{URL}accounts/login")
        sleep(1)
        email_field = self.driver.find_element_by_name("username")
        email_field.send_keys(INSTAGRAM_LOGIN[0])
        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys(INSTAGRAM_LOGIN[1])
        login_btn = self.driver.find_element_by_css_selector(".L3NKy")
        login_btn.click()

    def find_followers(self):
        self.driver.get(f"{URL}{TARGET_ACCOUNT}/")
        sleep(1)
        followers = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

    def follow(self):
        followed = 0
        index = 0
        followers_list = self.driver.find_elements_by_css_selector('ul div li')
        print(f"Length of the visible followers list: {len(followers_list)}")
        print(f"Amount of people about to follow: {PROFILE_FOLLOW_LIMIT}")
        print("- - - - - -")
        while followed < PROFILE_FOLLOW_LIMIT:
            if followed % 11 == 0:
                element_inside_popup = self.driver.find_element_by_xpath('//div[@class="isgrP"]//a')
                element_inside_popup.send_keys(Keys.END)
                sleep(5)
                followers_list = self.driver.find_elements_by_css_selector('ul div li')
                print(f"New Length of the visible followers list: {len(followers_list)}")
                print(f"Continuing from index {index}...")
                sleep(1)
            follower = followers_list[index]
            follow_btn = follower.find_element_by_css_selector('.L3NKy')
            username = follower.find_element_by_css_selector('.FPmhX').text
            text = follower.find_element_by_css_selector('.L3NKy').text
            # print(f"The text: {text}")
            if text == "Follow":
                print(f"Following: {username}")
                follow_btn.click()
                followed += 1
                index += 1
                sleep(1)
            else:
                print(f"Already Following: {username}")
                index += 1
        print(f"You followed {followed} accounts.")


bot = InstaFollower()
bot.login()
sleep(10)
bot.find_followers()
sleep(2)  # 10
bot.follow()
print("--- Done ---")
