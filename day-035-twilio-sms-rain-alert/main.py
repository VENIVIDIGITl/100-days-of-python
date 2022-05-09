import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")  # Your Twilio account sid
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")  # Your Twilio account auth token
twilio_number = os.environ.get("TWILIO_NUMBER")  # Your Twilio number
recipient_number = os.environ.get("MY_NUMBER")  # Your number (verified with twilio)

MY_LAT = 0  # Your latitude
MY_LONG = 0  # Your longitude
API_KEY = os.environ.get("OWM_API_KEY")  # Your Open Weather Map API Key
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

print(response.status_code)

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today! Remember to bring an umbrella! ☂️",
            from_=twilio_number,
            to=recipient_number
        )

    print(message.status)
