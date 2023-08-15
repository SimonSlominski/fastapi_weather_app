from fastapi import FastAPI

from geopy.geocoders import Nominatim


app = FastAPI()




@app.get("/forecasts")
def get_forecasts(city: str):
    pass

def get_weather_forecasts():
    pass

def get_coordinates(city):
    geolocator = Nominatim(user_agent="get_coordinates")

    try:
        location = geolocator.geocode(city)
        if location:
            latitude = location.latitude
            longitude = location.longitude
            return latitude, longitude
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    print(get_coordinates("Berlin"))
    print(get_coordinates("Wurzburg"))
