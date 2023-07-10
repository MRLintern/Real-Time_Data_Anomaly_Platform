# Testing model API
This curl commands can be used to test the service and user all the endpoints available.

## Predictions without scores
```
curl -X 'POST' \
  'http://localhost:8000/prediction' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feature_vector": [
    0.1234,
    0.1234

  ],
  "score": false
}'
```

## Predictions with scores
```
curl -X 'POST' \
  'http://localhost:8000/prediction' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feature_vector": [
    0.1234,
    0.1234

  ],
  "score": true
}'
```

## Getting the hyperparameters
```
curl -X 'GET' \
  'http://localhost:8000/model_information' \
  -H 'accept: application/json'
```
