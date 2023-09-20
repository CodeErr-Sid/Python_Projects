import time
import requests
from datetime import datetime
import smtplib

MY_MAIL = "siddiquetestemail@gmail.com"
MY_PASS = "kdox juvy mjln unxt"
RECEPIENT_MAIL = "siddiqueofl@gmail.com"
MY_LAT = 13.082680
MY_LONG = 80.270721


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_position = (iss_longitude, iss_latitude)

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
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
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_MAIL, MY_PASS)
            connection.sendmail(from_addr=MY_MAIL,
                                to_addrs=RECEPIENT_MAIL,
                                msg=f"Subject:LOOK UP😀!\n\nTHE INTERNATIONAL SPACE STATION IS ABOVE YOU!")
