import requests
from datetime import date
from flight_data import FlightData
from dateutil.relativedelta import relativedelta


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.tequila_endpoint_v1 = "https://tequila-api.kiwi.com"
        self.tequila_endpoint_v2 = "https://tequila-api.kiwi.com/v2"
        self.tequila_api_key = YOUR_API_KEY

    def find_iata_code(self, city_name):
        location_endpoint = f"{self.tequila_endpoint_v1}/locations/query"
        headers = {"apikey": self.tequila_api_key}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        data = response.json()
        code = data["locations"][0]["code"]
        return code

    def search(self, fly_from, fly_to):
        today_date = date.today()
        today_formatted = today_date.strftime("%d/%m/%Y")  # dd/mm/yyyyy
        future_date = date(today_date.year, today_date.month,  today_date.day) + relativedelta(months=+6)
        future_formatted = f"{future_date.day}/{future_date.month}/{future_date.year}"
        headers = {
            "apikey": self.tequila_api_key,
        }
        parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": today_formatted,
            "date_to": future_formatted,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        search_endpoint = f"{self.tequila_endpoint_v2}/search"
        response = requests.get(search_endpoint, params=parameters, headers=headers)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {fly_to}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
