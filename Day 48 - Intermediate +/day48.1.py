from selenium import webdriver

chrome_driver_path = YOUR_CHROME_WEBDRIVER_PATH
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# URL = "https://www.amazon.com/Corsair-Nightsword-Performance-Tunable-Backlit/dp/B07QX9C9WH/ref=sr_1_2_sspa?dchild=1&keywords=gaming+mouse&pd_rd_r=5495ff69-13cb-429f-aee1-781afeef7586&pd_rd_w=IoI5q&pd_rd_wg=iAsys&pf_rd_p=5811f97a-f703-4231-aa5f-c344167bfe13&pf_rd_r=FV9666049QBT1YD54TA7&qid=1624632236&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFRVEdQOEJYWklFOEcmZW5jcnlwdGVkSWQ9QTA0MDIzODMyVllMVTVGVzlXNlVHJmVuY3J5cHRlZEFkSWQ9QTA4MDY1MjUxSFlINlZQMTlQQ0FGJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
# driver.get(URL)
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)


URL = "https://www.python.org"
driver.get(URL)
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# docs_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(docs_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

driver.quit()

# driver.close() -> closes the current tab
# driver.quit() -> quits the browser
