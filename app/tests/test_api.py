from starlette.testclient import TestClient

from app.api import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to MPG Prediction FastAPI"}
