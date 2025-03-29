# import requests
# from datetime import datetime
# import smtplib
# import time
#
# my_email = "shryesPython19@gmail.com"
# password = "vrrsuydjhnzxleub"
# MY_LAT =  20.593683# Your latitude
# MY_LONG = 78.962883 # Your longitude
#
# def is_iss_overhead():
#     responce = requests.get(url="http://api.open-notify.org/iss-now.json")
#     responce.raise_for_status()
#     data = responce.json()
#
#     iss_latitude = float(data["iss_position"]["latitude"])
#     iss_longitude = float(data["iss_position"]["longitude"])
#
#     if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
#             return True
#
# def is_night():
#     parameters = {
#         "lat" : MY_LAT,
#         "lng" : MY_LONG,
#         "formatted" : 0
#     }
#     response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
#     response.raise_for_status()
#     data = response.json()
#     sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
#     sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
#
#     time_now = datetime.now().hour
#
#     if time_now >= sunset or time_now <= sunrise:
#         return True
#
#
# while True:
#     time.sleep(60)
#     if is_night() and is_iss_overhead():
#         print("HIIIIII")
#         connection = smtplib.SMTP("smtp.gmail.com")
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="shryes107@gmail.com",
#             msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
#         )


import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "shryesPython19@gmail.com"
MY_PASSWORD = "vrrsuydjhnzxleub"
MY_LAT =  20.593683# Your latitude
MY_LONG = 78.962883 # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="shryes107@gmail.com",
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )


