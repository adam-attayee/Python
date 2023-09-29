#program checks if the ISS is right above you and sends an email notification if true. 

import requests
from datetime import datetime
import smtplib

MY_EMAIL = ""
MY_APP_PASSWORD = ""
MY_LAT = 43.651890
MY_LONG = -79.381706

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

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

# If position is within +5 or -5 degrees of the ISS position and its dark, send an email that says "look up"

if (MY_LONG-5 <= iss_longitude <= MY_LONG+5) and (MY_LAT-5 <= iss_latitude <= MY_LAT+5) and (sunset < time_now or time_now < sunrise):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_APP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg="Subject:look up\n\nThe ISS is right above you in the sky!")
