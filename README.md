### Data Platform for Real-Time Anomaly Detection

### Introduction

<br>
This is a personal project in which I have created a made-up-company.
<br />

A start-up called AnomalousDex Inc., specialises in building personalised end-to-end data products
that employ Machine Learning models for anomaly detection, web services and monitoring tools to
find unusual cases lingering in company platforms.

<br>
The company has no customers yet so they need to create a sample data platform to show to
potential customers.
<br />

<br>
The data platform consists of three main components:

* A service that serves the anomaly detection model.
* The monitoring platform `Prometheus`.
* `Grafana` (a tool that excels at visualising monitoring dashboards).

The anomaly detector will be an Isolated Forest model, trained with a curated and real dataset provided
by the author's organisation; taken from online. This dataset is used in daily work to detect anomalous users.
As part of the model development, the anomalous decision boundary is visualised to better understand its decision.
This service, along with `Prometheus` and `Grafana`, will run inside multiple Docker components.
To deploy them, Docker Compose will be used. This is a tool for defining and running multiple `Docker` images.
<br />

### Project Outline

* Setting up the Docker Environment.
* Analysing and Visualising the Anomalous Dataset.
* Training an Anomaly Detection Model.
* Deploying the Model on a `FastAPI` Web Service.
* Setting up the Monitoring Stack (`Prometheus` and `Grafana`).
* Integrating the Metrics Collection Functionality in the Web Service.
* Testing the Model and Dashboard.

### Tools/Libraries Used

* `Python`.
* `pandas`.
* `Docker`.
* `Docker Compose`.
* `Prometheus`.
* `Caddy`.
* `Grafana`.
* `Jupyter`.
* `FastAPI`.
* `scikit-learn`.
* `Plotly`.
* `prometheus_client`.
