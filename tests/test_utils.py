import requests_mock

from app.utils import get_coordinates, get_weather_forecasts

def test_get_coordinates_valid_city():
    city = "London"
    lat, lon = get_coordinates(city)
    # These are rough values, as geolocation coordinates can slightly vary.
    assert 51 <= lat <= 52
    assert -1 <= lon <= 1

def test_get_coordinates_invalid_city():
    city = "NonExistentCity123"  # Example of a fictional city.
    result = get_coordinates(city)
    assert result is None

def test_get_coordinates_empty_string():
    city = ""  # Empty string.
    result = get_coordinates(city)
    assert result is None

def test_get_coordinates_none():
    city = None  # None scenario.
    result = get_coordinates(city)
    assert result is None

def test_get_weather_forecasts_success():
    with requests_mock.Mocker() as m:
        mock_response = {
            'daily': {
                'time': ['2023-06-01'],
                'temperature_2m_max': [25],
                'temperature_2m_min': [15],
                'rain_sum': [5],
                'windspeed_10m_max': [10],
            },
        }
        m.get('https://api.open-meteo.com/v1/forecast', json=mock_response)

        result = get_weather_forecasts(44.93, 7.54)
        expected_result = {
            '2023-06-01': {
                'min_temp': 15,
                'max_temp': 25,
                'rain_sum': 5,
                'wind_speed': 10,
                'classification': 'rainy',
            },
        }

        assert result == expected_result

def test_get_weather_forecasts_failure():
    with requests_mock.Mocker() as m:
        m.get('https://api.open-meteo.com/v1/forecast', status_code=500)

        result = get_weather_forecasts(44.93, 7.54)
        expected_result = {"Error": "Failed to fetch weather data."}

        assert result == expected_result