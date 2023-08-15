from fastapi import FastAPI
import requests

from geopy.geocoders import Nominatim


app = FastAPI()




@app.get("/forecasts")
def get_forecasts(city: str):
    pass

def get_weather_forecasts(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min,rain_sum,windspeed_10m_max",
        "timezone": "auto",
        "forecast_days": 5
    }

    response = requests.get(url, params=params)
    data = response.json()
    print(data)



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


if __name__ == "__main__":
    coordinates = get_coordinates("Wurzburg")
    print(coordinates)
    print(get_weather_forecasts(49.79, 9.93))
