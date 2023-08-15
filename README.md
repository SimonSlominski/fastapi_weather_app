<h1 align="center">FastAPI Weather App</h1>

---

## 📝 Table of Contents
- [About](#about)
- [Usage](#usage)
- [Getting Started](#getting_started)


## 🧐 About <a name = "about"></a>
<p align="left"> 
This FastAPI application is specifically designed for a friend's company and implemented for their internal use. The Weather Forecast API is part of their initiative to leverage weather data to better anticipate customer demand and optimise their operations.<br> 

This repository contains a FastAPI application that provides the weather forecasts for the next 5 days in a specified city.

To get started with the API, please refer to the 'Getting Started' section.
</p>


___
## 🎈 Usage <a name="usage"></a>
The API is simple to use: send a GET request with the city's name, and you will receive the daily weather forecasts for the next 5 days. The forecast includes essential weather data such as minimum and maximum temperature, rain amount, wind speed, and a classification of the weather conditions (e.g., stormy, rainy, windy or sunny).
___

## 🏁 Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Ensure the following is installed to your system venv:

```
python>=3.8
fastapi
uvicorn
requests
pytest
geopy
```

### Installing

#### Step 1. Clone the repository
```
git clone <repository URL>
```

#### Step 2. Running an app locally
Go to the main project directory that contains the "app" and "tests" folders and run the following command:
```
 uvicorn app.main:app --host 0.0.0.0 --port 8080 
```

#### Step 3. Test API using browser
Open the web browser. You can then access the API by sending GET requests to URLs like
```
http://localhost:8080/forecasts?city=<city_name>

http://localhost:8080/forecasts?city=Berlin
```

#### Step 4. Test API with Swagger
Open the web browser and type in http://localhost:8080/docs#/ <br>

This opens a local instance of the docsy-example homepage. You will see an endpoint named GET /forecasts. After selecting "Try it out," you can enter the city name in the "city" field to receive a forecast for the next 5 days.
