import requests
import smtplib
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Corsair-Nightsword-Performance-Tunable-Backlit/dp/B07QX9C9WH/ref=sr_1_2_sspa?dchild=1&keywords=gaming+mouse&pd_rd_r=5495ff69-13cb-429f-aee1-781afeef7586&pd_rd_w=IoI5q&pd_rd_wg=iAsys&pf_rd_p=5811f97a-f703-4231-aa5f-c344167bfe13&pf_rd_r=FV9666049QBT1YD54TA7&qid=1624632236&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFRVEdQOEJYWklFOEcmZW5jcnlwdGVkSWQ9QTA0MDIzODMyVllMVTVGVzlXNlVHJmVuY3J5cHRlZEFkSWQ9QTA4MDY1MjUxSFlINlZQMTlQQ0FGJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
EMAIL = YOUR_EMAIL
PASSWORD = YOUR_PASSWORD
RECIPIENT = RECIPIENT

# Get the following info from here: http://myhttpheader.com/
headers = {
    "User-Agent": YOUR_USER_AGENT,
    "Accept-Language": YOUR_LANGUAGE,
}

response = requests.get(URL, headers=headers)
data = response.text
# print(data)
soup = BeautifulSoup(data, "html.parser")

price = float(soup.find(
    name="span",
    id="priceblock_ourprice",
    class_="a-size-medium a-color-price priceBlockBuyingPriceString"
).getText()[1:])
# print(price)

title = soup.find(
    name="span",
    id="productTitle",
    class_="a-size-large product-title-word-break",
).getText().strip()
# print(title)

if price <= 80: # If price for the pruduct is less than $80, send an email.
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=RECIPIENT,
            msg=f"Subject:Amazon Price Alert!\n\nThe product '{title}' is now ${price}!\nHere is a link:\n{URL}"
        )
    print("Email Sent")
