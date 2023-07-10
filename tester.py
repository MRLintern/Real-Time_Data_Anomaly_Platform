import pandas as pd
import requests
import time
import random
import sys
import json

df = pd.read_csv(
    "./jupyter/notebooks/test.csv",
    header=0
)

# Iterate over every row and send request to model
percentage_chance = 0.25

for _, row in df.iterrows():
    payload = {
        "feature_vector": row.values.tolist(),
        "score": False
    }

    if random.random() < percentage_chance:
        payload["score"] = True

    print(payload)
    try:
        response = requests.post(
            "http://localhost:8000/prediction",
            json=payload
        )
        response.raise_for_status()
    except Exception as err:
        print(f"An error has occurred: {err}")
    else:
        print("Success!")
    time.sleep(0.05)


# Get the model hyperparameters
try:
    response = requests.get(
        "http://localhost:8000/model_information"
    )
    response.raise_for_status()
except Exception as err:
    print(f"An error has occurred: {err}")
else:
    print("Success!")
