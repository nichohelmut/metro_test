from starlette.testclient import TestClient

from api import app

client = TestClient(app)

data = {
    "Cylinders": 5,
    "Displacement": 100,
    "Horsepower": 100,
    "Weight": 2500,
    "Acceleration": 15,
    "Model_Year": 77,
    "Europe": 1,
    "Japan": 0,
    "USA": 0
}


# healthcheck
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to MPG Prediction Tool"}


# checks that value is not outlandish
def test_predict_mpg():
    response = client.post("/predict/", json=data)
    assert response.status_code == 200
    assert 50 > float(response.json()[0].split(" ")[-1]) > 0
