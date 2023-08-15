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
        # todo classification

        # Create new JSON object
        forecast_json = {}
        for i in range(len(dates)):

            forecast_json[dates[i]] = {
                "min_temp": min_temps[i],
                "max_temp": max_temps[i],
                "rain_sum": rain_sums[i],
                "wind_speed": wind_speeds[i],
            }

        return forecast_json
    except:
        pass


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
