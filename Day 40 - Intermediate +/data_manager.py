from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = YOUR_SHEETY_ENDPOINT


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        headers = {
            "Authorization": YOUR_BEARER_TOKEN
        }
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        print(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            headers = {
                "Authorization": YOUR_BEARER_TOKEN
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers,
            )
            # print(response.text)

    def get_customer_emails(self):
        customers_endpoint = YOUR_USERS_SHEETY_ENDPOINT
        headers = {
                "Authorization": YOUR_BEARER_TOKEN
            }
        response = requests.get(customers_endpoint, headers=headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
