from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "msg" in response.json()

def test_predict():
    response = client.post("/predict", json={"complaint_text": "This product caused nausea"})
    assert response.status_code == 200
    assert "result" in response.json()
