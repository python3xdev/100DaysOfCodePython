#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

sheety_get_endpoint = YOUR_SHEETY_ENDPOINT
sheety_headers = {
    "Authorization": YOUR_BEARER_TOKEN
}

response = requests.get(sheety_get_endpoint, headers=sheety_headers)
sheet_data_old = response.json() # cant use this because I have reached my API request limit.

sheet_data = {  # I decided to recreate part of the sheet_data.
    "prices": [
        {"city": "Paris", "iataCode": "PAR", "lowest_price": 54},
        {"city": "Berlin", "iataCode": "BER", "lowest_price": 42},
        {"city": "Tokyo", "iataCode": "TYO", "lowest_price": 485},
    ],
}

all_filled = True
# THIS FILLS OUT THE IATA CODE COLUMN IN THE GOOGLE SHEET
for city_info in sheet_data["prices"]:
    if city_info["iataCode"] == '':
        iata_code = FlightSearch().find_iata_code(city_info["city"])
        city_info["iataCode"] = iata_code
    all_filled = True
# print(sheet_data)
if not all_filled:
    DataManager(sheet_data).put_iata_codes()

flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"  # London
destinations_data = sheet_data["prices"]
for destination in destinations_data:
    flight = flight_search.search(ORIGIN_CITY_IATA, destination["iataCode"])
    if flight.price <= destination["lowest_price"]:
        print(f"Flight Info: {flight.destination_city}, {flight.price}")
        notification_manager = NotificationManager()
        notification_manager.send_sms(flight)


