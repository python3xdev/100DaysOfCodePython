import requests
from datetime import datetime
import smtplib
import time

my_email = EMAIL
my_password = PASSWORD
recipient = EMAIL
MY_LAT = Your latitude
MY_LONG = Your longitude


def within_five_deg():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    lng_bool = MY_LONG + 5 > iss_longitude > MY_LONG - 5
    lat_bool = MY_LAT + 5 > iss_latitude > MY_LAT - 5
    if lng_bool and lat_bool:
        return True
    return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_dark():
    response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()
    data_sun = response_sun.json()
    sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])

    current_hour = datetime.now().hour

    if current_hour >= sunset or current_hour <= sunrise:
        return True
    return False


while True:
    time.sleep(60)
    if within_five_deg() and is_dark():
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg="Subject:Look Up 👆\n\nThe ISS is above you in the sky.",
        )

# BONUS: run the code every 60 seconds.
