from time import sleep
from selenium import webdriver

# --- Internet Speed Twitter Complaint Bot ---

chrome_driver_path = YOU_CHROME_DRIVER_LOCATION

PROMISED_DOWN = 100
PROMISED_UP = 100
TWITTER_LOGIN = (YOUR_EMAIL, YOUR_PASSWORD)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.DOWN = PROMISED_DOWN
        self.UP = PROMISED_UP
        self.driver = webdriver.Chrome(chrome_driver_path)

    def get_internet_speed(self):
        self.driver.get("https://speedtest.net")
        start = self.driver.find_element_by_class_name("js-start-test")
        start.click()
        sleep(50)
        DOWN = self.driver.find_element_by_css_selector(".download-speed").text
        UP = self.driver.find_element_by_css_selector(".upload-speed").text
        print(f"Download: {DOWN}\nUpload: {UP}")
        return float(DOWN), float(UP)

    def tweet_at_provider(self, info):
        self.driver.get("https://twitter.com/login")
        sleep(1)
        email_field = self.driver.find_element_by_name("session[username_or_email]")
        email_field.send_keys(TWITTER_LOGIN[0])
        password_field = self.driver.find_element_by_name("session[password]")
        password_field.send_keys(TWITTER_LOGIN[1])
        login_btn = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        login_btn.click()
        sleep(3)
        # Changing Twitters theme to "Dim" because I dislike 'light theme'
        menu = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/div')
        menu.click()
        sleep(1)
        display = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[9]/a')
        display.click()
        sleep(1)
        dim = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[8]/div/div/div[2]/input')
        dim.click()
        sleep(1)
        done = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[9]/div')
        done.click()
        sleep(2)
        # Now back to the actual program.
        text_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        text_box.send_keys(f"Hey Internet Provider, why is my internet speed {info[0]} Download/{info[1]} Upload when I pay for {PROMISED_DOWN} Download/{PROMISED_UP} Upload.")
        sleep(5)
        tweet_btn = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_btn.click()


bot = InternetSpeedTwitterBot()
speeds = bot.get_internet_speed()
if speeds[0] < PROMISED_DOWN or speeds[1] < PROMISED_UP:
    bot.tweet_at_provider(speeds)
else:
    print("All is good.")
