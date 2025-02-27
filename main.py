import requests
from data import *
from datetime import datetime


today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M:%S")

user_input = input('Tell me which exercise you did: ')

nutri_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
nutri_headers = {
    'x-app-id': NUTRI_APP_ID,
    'x-app-key': NUTRI_API_KEY
}
nutri_params = {
    "query": user_input,
    'weight_kg': 74,
    'height_cm': 174,
    'age': 26,
}

nutri_response = requests.post(nutri_endpoint, headers=nutri_headers, json=nutri_params)
nutri_response.raise_for_status()
data = nutri_response.json()["exercises"]

sheety_endpoint = 'https://api.sheety.co/e6ed77249101a376e125685dc5e4bfcd/myWorkouts/workouts'
sheety_headers = {
    'Authorization': SHEETY_API_KEY,
    'Content-Type': 'application/json',
}

for exercise in data:

    sheety_inputs = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise['name'],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json=sheety_inputs, headers=sheety_headers)
    sheet_response.raise_for_status()