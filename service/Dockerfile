FROM python:3.9-slim

RUN mkdir service

WORKDIR /service

COPY main.py Pipfile Pipfile.lock model.joblib ./

RUN pip install pipenv

RUN pipenv install

CMD [pipenv run uvicorn main:app --host 0.0.0.0 --port 8000]
