import requests
from datetime import datetime
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, new_sheet_data):
        self.new_sheet_data = new_sheet_data
        # print(self.new_sheet_data)
        self.endpoint = YOUR_SHEETY_ENDPOINT

    def put_iata_codes(self):  # this weill only be used once when new cities are added.
        for city in self.new_sheet_data["prices"]:
            parameters = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            headers = {
                "Authorization": YOUR_BEARER_TOKEN
            }
            response = requests.put(f"{self.endpoint}/{city['id']}", json=parameters, headers=headers)
            print(response.text)

