# Python image; only contains the minimal packages needed to run Python.

FROM python:3.7-slim

# create src directory inside the container

RUN mkdir -p /src

# WORKDIR /home/user/Desktop/Real-Time_Data_Anomaly_Platform/jupyter/src
WORKDIR /src

# install jupyter notebook

RUN pip install notebook

# specify the command that starts the jupyter server

CMD ["jupyter", "notebook", "--port= 8888", "--no-browser" , "--ip= 0.0.0.0", "--allow-root"]

