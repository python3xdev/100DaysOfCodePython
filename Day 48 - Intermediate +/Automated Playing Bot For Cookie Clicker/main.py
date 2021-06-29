from selenium import webdriver
import time
import threading

chrome_driver_path = YOUR_CHROME_WEBDRIVER_PATH
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element_by_id("cookie")

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

short_timer = time.time() + 5
long_timer = time.time() + 60 * 5

run_all = True


def click():
    while run_all:
        cookie.click()


def run():
    global short_timer, run_all
    while True:
        cookie.click()

        if time.time() > short_timer:
            prices = driver.find_elements_by_css_selector("#store div")
            cost_list = []
            for price in prices:
                price = price.text
                if price != '':
                    try:
                        cost = int(price.split("\n")[0].split("-")[1].strip().replace(",", ""))
                        cost_list.append(cost)
                    except IndexError:
                        pass

            money = int(driver.find_element_by_id("money").text.replace(",", ""))

            max_number = 0
            for cost in cost_list:
                if cost <= money:
                    if cost >= max_number:
                        max_number = cost

            try:
                max_number_index = cost_list.index(max_number)
            except ValueError:
                pass

            else:
                buy_item = driver.find_element_by_id(item_ids[max_number_index])
                buy_item.click()

            short_timer = time.time() + 5

        if time.time() > long_timer:
            cps = driver.find_element_by_id("cps").text
            run_all = False
            print("-"*20 + " Program Finished " + "-"*20)
            print(f"The results are: {cps} CPS (CookiesPerSecond)")
            break


threading.Thread(target=run).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
threading.Thread(target=click).start()
