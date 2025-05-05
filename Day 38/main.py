import requests
from datetime import datetime
APP_ID = "508022d3"
APP_KEY = "992d963585e1218c3e6c53595a72bad0"
BEARER_TOKEN = "tacotuesday"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/2c421bd56502b283265aacb755fccccd/myWorkouts/workouts"
text = input("What exercise did you do?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}


parameters = {
    "query": text,
    "weight_kg": 100,
    "height_cm": 180,
    "age": 34
}
bearer_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"

}



response = requests.post(exercise_endpoint, json=parameters, headers=headers)
data = response.json()
exercise_data = data["exercises"]

print(exercise_data)




today_date = datetime.now().strftime("%Y/%m/%d")
now_time = datetime.now().strftime("%X")

for exercise in exercise_data:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        sheety_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.json())