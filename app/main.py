from fastapi import FastAPI, HTTPException

from utils import get_coordinates, get_weather_forecasts


app = FastAPI()



@app.get("/forecasts")
def get_forecasts(city: str):
    coordinates = get_coordinates(city)
    if not coordinates:
        raise HTTPException(status_code=404, detail=f"Coordinates for {city} not found.")

    latitude, longitude = coordinates
    forecasts = get_weather_forecasts(latitude, longitude)

    return forecasts
