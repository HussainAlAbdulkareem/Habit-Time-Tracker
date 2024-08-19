import requests
from dotenv import load_dotenv
import os
import datetime

start_hour = int(datetime.datetime.now().strftime("%I"))
start_minute = round(int(datetime.datetime.now().strftime("%M")) / 60, 2)
start_time = start_hour + start_minute

total = 0
done = False
while not done:
    quit = input("Press Space/y/q to stop the program. \n")
    if quit == "" or quit == "y" or quit == "q":
        done = True
        end_hour = int(datetime.datetime.now().strftime("%I"))
        end_minute = round(int(datetime.datetime.now().strftime("%M")) / 60, 2)
        end_time = end_hour + end_minute

        total = round(end_time - start_time, 2)
        print(total)

load_dotenv()
sheets_endpoint = f"https://api.sheety.co/{os.getenv('USERNAME_ID')}/habitTracker/sheet1/2"

curr_hours = requests.get(sheets_endpoint).json()["sheet1"]["codingTime"]

sheets_params = {
    "sheet1": {
        "codingTime": curr_hours + total
        }
    }
sheets_response = requests.put(sheets_endpoint, json=sheets_params)
print(sheets_response.text)
