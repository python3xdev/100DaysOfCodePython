import datetime as dt
import smtplib
import random

email = EMAIL
password = PASSWORD
recipient = EMAIL

now = dt.datetime.now()
day_of_the_week = now.weekday()
if day_of_the_week == 1:  # 1 == Tuesday. 0 == Monday. etc.
    with open("Auto Email Birthday Wisher/Birthday Wisher (Day 32) start/quotes.txt", "r") as file:
        data = file.readlines()
        random_quote = random.choice(data)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=recipient,
            msg=f"Subject:Tuesday's Quotes\n\n{random_quote}"
        )
        print("Email Sent.")
