import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver

zillow_link = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
headers = {
    "user-agent": YOUR_USER_AGENT,
    "accept-language": YOU_ACCEPT_LANGUAGE,
}

response = requests.get(zillow_link, headers=headers)
content = response.text
soup = BeautifulSoup(content, "html.parser")
properties = soup.select("li article.list-card")[:-1]

data_sets = []

for prop in properties:
    address = prop.select_one("address.list-card-addr").text
    price = prop.select_one("div.list-card-price").text.split("+")[0].split("/")[0]
    link = f'https://www.zillow.com{prop.select_one("a.list-card-link").get("href")}'
    data_sets.append([address, price, link])

google_form = "https://docs.google.com/forms/d/e/1FAIpQLSc_EKVrjyioqZXJYNMgqkl7sWsJdOAyHgUXaXJl7os7hk_ivQ/viewform?usp=sf_link"
chrome_driver_path = YOUR_CHROME_DRIVER_PATH
driver = webdriver.Chrome(chrome_driver_path)
for data_set in data_sets:
    driver.get(google_form)
    sleep(1)
    fields = driver.find_elements_by_css_selector("div.quantumWizTextinputPaperinputInputArea input")
    fields[0].send_keys(data_set[0])
    fields[1].send_keys(data_set[1])
    fields[2].send_keys(data_set[2])
    send_btn = driver.find_element_by_css_selector("div[role='button']")
    send_btn.click()
    sleep(1)

print("--- Complete ---")
driver.quit()
