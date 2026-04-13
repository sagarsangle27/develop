from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "API working"}


def test_score():

    payload = {
        "name": "Sagar",
        "age": 28,
        "skills": ["python", "ml"]
    }

    response = client.post("/score", json=payload)

    assert response.status_code == 200
    assert response.json()["score"] == 20


def test_predict():

    payload = {
        "name": "Sagar",
        "age": 30,
        "skills": ["python"]
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert response.json()["prediction"] == 60000