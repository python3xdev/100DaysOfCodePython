import requests
import smtplib

my_email = EMAIL
my_password = PASSWORD
recipient = EMAIL

""""
Website used:
https://www.latlong.net/       - To get you coordinates
http://jsonviewer.stack.hu/       - To easier read json text
https://openweathermap.org/api/one-call-api       - To get the weather for specific lat & lon
https://www.ventusky.com/?p=50.7;-1.3;5&l=rain-3h       - To see where its raining for testing purposes
https://www.twilio.com      - To send SMS's to your phone
https://www.pythonanywhere.com      - automatically run the file every day
"""

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = API_KEY

my_lat_lon = (YOUR_LAT, YOUR_LON)
test_lan_lon = (TEST_LAT, TEST_LON) # a place that its currently raining at.

parameters = {
    "lat": my_lat_lon[0],
    "lon": my_lat_lon[1],
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()

data = response.json()

weather_slice = data["hourly"][:12]


def umbrella():
    will_rain = False
    for hour_data in weather_slice:
        weather_id = hour_data["weather"][0]["id"]
        # print(hour_data["weather"])
        if weather_id < 700:
            will_rain = True
            return will_rain  # "Take an umbrella with you."
    return will_rain  # "You do not need an umbrella."


if umbrella():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg="Subject:Take an umbrella with you!\n\nTake an umbrella "
                "with you today, there is a chance for rain/show."
        )
    print("Email Sent.")
