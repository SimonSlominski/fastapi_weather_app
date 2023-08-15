from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_valid_city_forecasts():
    response = client.get("/forecasts?city=New York")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "2023-08-19" in data
    assert "min_temp" in data["2023-08-19"]
