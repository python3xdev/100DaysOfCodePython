##################### Extra Hard Starting Project ######################
print("Sending Email...")
import pandas
import smtplib
import random
import datetime as dt

my_email = EMAIL
password = PASSWORD

# Reading the csv file.
csv_data = pandas.read_csv("birthdays.csv")
people_list = [list(row) for row in csv_data.values]

# Checking if today matches the dates in the csv file

now = dt.datetime.now()
month = now.month
day = now.day

for person in people_list:
    if person[3] == month and person[4] == day:
        random_file = random.choice(['letter_1.txt', 'letter_2.txt', 'letter_3.txt'])
        person_name = person[0]
        person_email = person[1]
        with open(f"letter_templates/{random_file}", "r") as file:
            file_data = file.read()
            email_text = file_data.replace("[NAME]", person_name)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=person_email,
                msg=f"Subject:Happy Birthday!\n\n{email_text}"
            )
print("- - - - - - - - - - - - - - -")
print("Email Sent Successfully.")
