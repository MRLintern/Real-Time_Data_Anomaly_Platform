from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

#####
# Testing the hyperparameters extraction
#####
def test_model_info():
    response = client.get("/model_information")
    assert response.status_code == 200

#####
# Testing the prediction
#####
def test_prediction():
    response = client.post(
        "/prediction",
        json={
            "feature_vector": [0.1234, 0.1234],
            "score": True
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "is_inlier": True,
        "anomaly_score": -0.5968904587109694
    }

 
