import requests
import os
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
aip_key = "6cd75c2f8e0efdb5cbe7b9d3bcbbbc25"
account_sid = "ACa6b94891b9b7ce4010064bf5373003dc"
auth_token = "efad1b49746384c5b9d6b992b144c4af"

weather_params = {
    "lat": 40.060994,
    "lon": -83.053249,
    "appid": aip_key,
    "exclude": "current,minutely,daily"
}


response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_date in weather_slice:
    condition_code = hour_date["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain🌧️️ today.Bring an umbrella!☔️",
        from_="+17473023823",
        to="+16147722442"
    )
    print(message.status)