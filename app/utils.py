import requests
from geopy.geocoders import Nominatim

from app.config import RAIN_THRESHOLD, WIND_THRESHOLD


def get_coordinates(city):
    geolocator = Nominatim(user_agent="get_coordinates")

    try:
        location = geolocator.geocode(city)
        if location:
            latitude = round(location.latitude, 2)
            longitude = round(location.longitude, 2)
            return latitude, longitude
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None

def classify_weather(rain_sum, wind_speed):
    if rain_sum >= RAIN_THRESHOLD and wind_speed >= WIND_THRESHOLD:
        return "stormy"
    elif rain_sum >= RAIN_THRESHOLD:
        return "rainy"
    elif wind_speed >= WIND_THRESHOLD:
        return "windy"
    else:
        return "sunny"

def get_weather_forecasts(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min,rain_sum,windspeed_10m_max",
        "timezone": "auto",
        "forecast_days": 5
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract required data from the response
        dates = data['daily']['time']
        max_temps = data['daily']['temperature_2m_max']
        min_temps = data['daily']['temperature_2m_min']
        rain_sums = data['daily']['rain_sum']
        wind_speeds = data['daily']['windspeed_10m_max']

        # Create new JSON object
        forecast_json = {}
        for i in range(len(dates)):
            classification = classify_weather(rain_sums[i], wind_speeds[i])
            forecast_json[dates[i]] = {
                "min_temp": min_temps[i],
                "max_temp": max_temps[i],
                "rain_sum": rain_sums[i],
                "wind_speed": wind_speeds[i],
                "classification": classification
            }

        return forecast_json
    except Exception as e:
        print("Error:", e)
        return {"Error": "Failed to fetch weather data."}
