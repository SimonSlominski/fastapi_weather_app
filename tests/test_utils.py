import pytest
from app.utils import get_coordinates

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