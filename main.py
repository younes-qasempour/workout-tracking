import requests
from data import *


exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}
user_input = input('Tell me which exercise you did: ')
exercise_params = {
    "query": user_input,
    'weight_kg': 74,
    'height_cm': 174,
    'age': 26,
}

response = requests.post(exercise_endpoint, headers=exercise_headers, json=exercise_params)
response.raise_for_status()
data = response.json()
