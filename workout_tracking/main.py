import requests
from datetime import datetime

APP_ID = "42dcbf81"
API_KEY = "cdd1f8ee1560ef42366f507a23872156"

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_parameters = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 55,
    "height_cm": 14.47,
    "age": 18
}

response = requests.post(exercise_endpoint, json=exercise_parameters, headers=headers)
result = response.json()
print(result)

add_text_endpoint = "https://api.sheety.co/e7b6e23181315cf9ee92d6462b9e1e62/myWorkouts/workouts"
today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
 add_parameters = {
    "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": exercise['name'].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
        }
    }
 sheet_response = requests.post(add_text_endpoint, json=add_parameters)

 print(sheet_response.text)

