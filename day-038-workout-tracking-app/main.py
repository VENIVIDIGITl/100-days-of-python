import requests
from datetime import datetime
import os

GENDER = "YOUR GENDER"
WEIGHT_KG = "YOUR WEIGHT"
HEIGHT_CM = "YOUR HEIGHT"
AGE = "YOUR AGE"
# Sheety API
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]
AUTH_TOKEN = f"Bearer {os.environ['SHEET_TOKEN']}"
# Nutritionix API
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ["NUTRITIONIX_APP_ID"]
APP_KEY = os.environ["NUTRITIONIX_APP_KEY"]


exercise_query = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

exercise_params = {
    "query": exercise_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# Get exercise data
exercise_response = requests.post(EXERCISE_ENDPOINT, json=exercise_params, headers=headers)
data = exercise_response.json()

# Generate rows of exercises and add them to your sheet
for exercise in data["exercises"]:
    # generate a row
    sheet_inputs = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime('%X'),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        },
    }
    # add the row to your sheet
    bearer_headers = {
        "Authorization": AUTH_TOKEN
    }
    response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, headers=bearer_headers)
    print(response)
    data = response.json()
    print(data)
