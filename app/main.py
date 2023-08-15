from fastapi import FastAPI

from utils import get_coordinates, get_weather_forecasts

app = FastAPI()




@app.get("/forecasts")
def get_forecasts(city: str):
    coordinates = get_coordinates(city)
    latitude, longitude = coordinates
    forecasts = get_weather_forecasts(latitude, longitude)
    print(type(forecasts))
