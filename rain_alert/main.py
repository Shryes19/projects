import requests
from twilio.rest import Client
import smtplib

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "bd317af2ad484abaf48e6b8d105c7785"
MY_EMAIL = "shryesPython19@gmail.com"
MY_PASSWORD = "vrrsuydjhnzxleub"

parameters = {
    "lat": 20.593683,
    "lon": 78.962883,
    "appid": api_key,
    "cnt": 4,
}

responce = requests.get(OWM_endpoint, params=parameters)
responce.raise_for_status()
weather_data = responce.json()


will_rain = False
for hour_day in weather_data["list"]:
    condition_code = (hour_day["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella")
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL,password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs="shryes107@gmail.com",msg="Subject:RAIN RAIN\n\nIt's going to "
                                                                               "rain today. Remember to bring an "
                                                                               "umbrella")



