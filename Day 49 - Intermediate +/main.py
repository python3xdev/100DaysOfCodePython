import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = YOUR_CHROME_DRIVER_PATH
driver = webdriver.Chrome(chrome_driver_path)

LINKEDIN_LOGIN_INFO = (YOUR_EMAIL, YOUR_PASSWORD)  # I USED A FAKE ACCOUNT

# LOGIN
driver.get("https://www.linkedin.com/")
email_field = driver.find_element_by_name("session_key")
email_field.send_keys(LINKEDIN_LOGIN_INFO[0])
password_field = driver.find_element_by_name("session_password")
password_field.send_keys(LINKEDIN_LOGIN_INFO[1])
sign_in_btn = driver.find_element_by_class_name("sign-in-form__submit-button")
sign_in_btn.click()

# APPLYING FOR A JOB
# go to the LinkedIn Jobs page and search 'python developer', now turn on the Easy Apply filter. Now copy and paste that URL below in the 'URL' variable.
URL = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId={GEO_ID}&keywords=python%20developer&location={YOUR_CONTRY}" # This is an example.
driver.get(URL)

time.sleep(1)
jobs = driver.find_elements_by_css_selector("div ul li div .job-card-container.relative.job-card-list.job-card-container--clickable")
print(f"Applying for {len(jobs)} jobs...")


for job in jobs:
    job.click()
    time.sleep(2)
    try:
        apply_btn = driver.find_element_by_css_selector(".jobs-apply-button--top-card button")
        apply_btn.click()
        time.sleep(2)

        phone_number_field = driver.find_element_by_css_selector(".fb-single-line-text .display-flex input")
        if phone_number_field.text == "":
            phone_number_field.send_keys("667562499")  # I used a fake phone number

        submit_button = driver.find_element_by_css_selector("footer button")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

            # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipping...")
        pass


time.sleep(10)
driver.quit()
