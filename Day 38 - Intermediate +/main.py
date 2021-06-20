import requests
import os
from requests.auth import HTTPBasicAuth
from datetime import datetime
from personal_data import personal_data

APP_ID = YOUR_API_INFO
API_KEY = YOUR_API_INFO

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

user_input = input("How much exercise have you done today?: ")

exercise_params = {
    "query": user_input,
    "gender": personal_data["gender"],
    "weight_kg": personal_data["weight_kg"],
    "height_cm": personal_data["height_cm"],
    "age": personal_data["age"],
}

response = requests.post(exercise_endpoint, json=exercise_params, headers=headers)
data = response.json()
print(data)
print("-" * 20)

current_time = datetime.now()

# Placing all this data into the Google Spreadsheet

bearer_headers = {
    "Authorization": YOUR_KEY

sheety_endpoint = YOUR_ENDPOINT

for exercise in data["exercises"]:
    sheety_params = {
        "workout": {
            "date": current_time.strftime("%d/%m/%Y"),
            "time": current_time.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(sheety_endpoint, json=sheety_params, headers=bearer_headers)
    print(sheety_response.text)
