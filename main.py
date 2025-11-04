import requests
from datetime import datetime
import smtplib
import time
EMAIL = "aabduqodirova28@gmail.com"
PASSWORD = "1223abcd()" #You put your app password here.
MY_LAT = 41.299496 # Your latitude
MY_LONG = 69.240074 # Your longitude

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

time_now = datetime.now()
now = time_now.hour

while True:
    time.sleep(60)
    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5:
        if now > sunset or now < sunrise:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user= EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg= f"Subject: Time to look up!\n\nHey, ISS is above you!")




