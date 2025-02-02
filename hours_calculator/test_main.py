from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_check_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "success"

def test_calculate_hours():
    response = client.get("/hours/12/2025")
    assert response.status_code == 200
    assert response.json() == {"peak_hour": 322, "non_peak_hour": 422}