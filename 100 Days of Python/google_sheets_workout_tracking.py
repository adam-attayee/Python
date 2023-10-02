from datetime import datetime
import requests
import os
import random

GENDER = f"{random.choice(['MALE', 'FEMALE'])}"
WEIGHT_KG = f"{random.randint(50, 150)}"
HEIGHT = f"{random.randint(100, 200)}"
AGE = f"{random.randint(20,70)}"

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
BEARER_TOKEN = os.environ['BEARER_TOKEN']
SHEET_ENDPOINT = os.environ['SHEET_ENDPOINT']
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("Tell which exercise you did today?: ")

header = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY
}

parameters = {
    'query': exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
data = response.json()

headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}


exercise_data = data["exercises"]

for i in range(0, len(exercise_data)):
    date = datetime.now().strftime('%d/%m/%Y')
    time = datetime.now().strftime('%H:%M:%S')
    exercise_name = exercise_data[i]['name'].title()
    duration = round(exercise_data[i]["duration_min"])
    calories_burned = round(exercise_data[i]["nf_calories"])

    parameters = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise_name,
                "duration": duration,
                "calories": calories_burned
            }
    }

    response = requests.post(url=SHEET_ENDPOINT, json=parameters, headers=headers)
    response.raise_for_status()
    print(response.text)
