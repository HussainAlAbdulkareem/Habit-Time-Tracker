import requests
from dotenv import load_dotenv
import os

load_dotenv()
sheets_endpoint = f"https://api.sheety.co/{os.getenv('USERNAME_ID')}/habitTracker/sheet1/2"

start_hours = requests.get(sheets_endpoint).json()["sheet1"]["codingTime"]
print(start_hours)

sheets_params = {
    "sheet1": {
        "codingTime": start_hours + 10
        }
    }
sheets_response = requests.put(sheets_endpoint, json=sheets_params)
print(sheets_response.text)
