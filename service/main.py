import sklearn
import numpy as np
from joblib import dump, load
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional, Dict
from prometheus_client import make_asgi_app, Counter, Histogram
import time


# Define input object model
class InputItem(BaseModel):
    feature_vector: List[float]
    score: bool

# Define output object model
class OutputItem(BaseModel):
    is_inlier: bool
    anomaly_score: Optional[float] = None



clf = load('model.joblib')
app = FastAPI()

###########################
# Prometheus export metrics
###########################
app_prometheus = make_asgi_app()
app.mount("/metrics", app_prometheus)

# Counters
counter_prediction = Counter("predictions", "Counts the number of predictions")
counter_hyperparameters = Counter("hyperparameters", "Counts the number of \
        requests to get the hyperparameters.")
# Histograms
model_prediction_response = Histogram("request_prediction_response", "Histogram \
        with info about the prediction response.")
score_samples_prediction = Histogram("request_prediction_score",
        "Histogram to track prediction scores."
)
request_prediction_latency = Histogram("request_prediction_latency",
        "Histogram to track prediction latency."
)

@app.post("/prediction", response_model=OutputItem)
async def prediction(item: InputItem):
    start = time.time()
    # Init the response object
    item_out = {}

    # Always compute prediction
    pred_not_bool = clf.predict(np.array(item.feature_vector).reshape(1, -1))
    item_out["is_inlier"] = "true" if pred_not_bool == 1 else "false"
    model_prediction_response.observe(pred_not_bool)

    # If score is needed then compute score and add it to the item
    if item.score == 1:
        scores = clf.score_samples(np.array(item.feature_vector).reshape(1, -1))
        item_out["anomaly_score"] = scores
        score_samples_prediction.observe(scores)

    counter_prediction.inc()
    end = time.time()
    request_prediction_latency.observe(end - start)
    return item_out


@app.get("/model_information")
async def model_info():
    counter_hyperparameters.inc()
    return clf.get_params()
