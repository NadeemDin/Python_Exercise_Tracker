import requests
from datetime import datetime


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

GENDER = "Male"
WEIGHT_KG = 82
HEIGHT_CM = 173
AGE = 28

APP_ID = """get app_id from exercise_endpoint and paste here as string"""
API_KEY ="""get api_key from exercise_endpoint and paste here as string"""

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint_add = """visit https://sheety.co/ and obtain a link for the google sheet you wish to write to"""


exercise_text = str(input("What did you do?: "))

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}

request_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": 27
}

response = requests.post(exercise_endpoint,json=request_parameters, headers=headers)
result = response.json()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": exercise["name"],
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
    }
    }

sheet_response = requests.post(sheety_endpoint_add, json=sheet_inputs)

print(sheet_response.text)